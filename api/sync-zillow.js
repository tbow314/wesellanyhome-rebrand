// Vercel Cron Function — runs daily at 8am ET
// Fetches Mario's Zillow profile, extracts stats, saves to Vercel Blob
// Triggered by: vercel.json cron schedule OR manual GET /api/sync-zillow

const { put } = require('@vercel/blob');
const path = require('path');
const fs   = require('fs');

const ZILLOW_PROFILE_URL = 'https://www.zillow.com/profile/marioarudolph';
const BLOB_KEY = 'listings-data.json';

module.exports = async function handler(req, res) {
  // Allow manual trigger or cron (Vercel sends GET for crons)
  if (req.method !== 'GET') return res.status(405).json({ error: 'Method not allowed' });

  // Verify cron secret to prevent unauthorized triggers
  const cronSecret = process.env.CRON_SECRET;
  if (cronSecret) {
    const authHeader = req.headers.authorization;
    if (authHeader !== `Bearer ${cronSecret}`) {
      return res.status(401).json({ error: 'Unauthorized' });
    }
  }

  try {
    console.log('Fetching Zillow profile…');

    const html = await fetchWithRetry(ZILLOW_PROFILE_URL);
    const stats = extractStats(html);

    console.log('Extracted stats:', stats);

    // Load existing listings.json as base (fallback to local file)
    let base;
    try {
      const filePath = path.join(process.cwd(), 'data', 'listings.json');
      base = JSON.parse(fs.readFileSync(filePath, 'utf8'));
    } catch {
      base = { active_listings: [], sold_listings: [], reviews: [] };
    }

    // Merge fresh stats into _meta
    base._meta = {
      ...base._meta,
      ...stats,
      last_synced: new Date().toISOString(),
    };

    // Save to Vercel Blob
    const blob = await put(BLOB_KEY, JSON.stringify(base), {
      access: 'public',
      contentType: 'application/json',
      addRandomSuffix: false,
    });

    console.log('Saved to Blob:', blob.url);

    return res.status(200).json({
      ok: true,
      stats,
      blob_url: blob.url,
      synced_at: base._meta.last_synced,
    });

  } catch (err) {
    console.error('Sync error:', err.message);
    return res.status(500).json({ error: err.message });
  }
};

// ── Fetch with browser-like headers ──────────────────────────────────────────
async function fetchWithRetry(url, retries = 2) {
  const headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
  };

  for (let i = 0; i <= retries; i++) {
    try {
      const resp = await fetch(url, { headers });
      if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
      return await resp.text();
    } catch (err) {
      if (i === retries) throw err;
      await new Promise(r => setTimeout(r, 1500 * (i + 1)));
    }
  }
}

// ── Parse stats from Zillow page HTML ────────────────────────────────────────
function extractStats(html) {
  const stats = {};

  // Try __NEXT_DATA__ JSON blob first (most reliable)
  const nextDataMatch = html.match(/<script id="__NEXT_DATA__"[^>]*>([\s\S]*?)<\/script>/);
  if (nextDataMatch) {
    try {
      const nextData = JSON.parse(nextDataMatch[1]);
      const agentData = findDeep(nextData, 'agentMetrics') || findDeep(nextData, 'profileData');
      if (agentData) {
        stats.total_sales          = agentData.totalSales      || agentData.totalTransactions || null;
        stats.sales_last_12_months = agentData.recentSales     || agentData.salesLast12Months  || null;
        stats.avg_sale_price       = agentData.avgSalePrice    || agentData.averageSalePrice   || null;
        stats.zillow_rating        = agentData.rating          || agentData.reviewScore        || null;
        stats.review_count         = agentData.reviewCount     || agentData.totalReviews       || null;
      }
    } catch { /* fall through to regex */ }
  }

  // Regex fallbacks for key numbers
  if (!stats.total_sales) {
    const m = html.match(/(\d+)\s*(?:total\s*)?(?:sales|transactions|homes?\s*sold)/i);
    if (m) stats.total_sales = parseInt(m[1]);
  }
  if (!stats.zillow_rating) {
    const m = html.match(/(\d+\.?\d*)\s*(?:out of 5|stars?|★)/i);
    if (m) stats.zillow_rating = parseFloat(m[1]);
  }
  if (!stats.avg_sale_price) {
    const m = html.match(/\$([0-9,]+(?:\.\d+)?)[Kk]?\s*(?:avg|average|median)/i);
    if (m) {
      const raw = m[1].replace(/,/g, '');
      stats.avg_sale_price = m[0].toLowerCase().includes('k') ? parseFloat(raw) * 1000 : parseInt(raw);
    }
  }

  return stats;
}

// ── Recursive deep search for a key in nested object ─────────────────────────
function findDeep(obj, key) {
  if (!obj || typeof obj !== 'object') return null;
  if (obj[key] !== undefined) return obj[key];
  for (const v of Object.values(obj)) {
    const found = findDeep(v, key);
    if (found !== null) return found;
  }
  return null;
}
