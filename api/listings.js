// Vercel Serverless Function — serves live listings data
// Source of truth: Vercel Blob (updated daily by /api/sync-zillow cron)
// Falls back to /data/listings.json if Blob not yet populated

const fs   = require('fs');
const path = require('path');
const { list } = require('@vercel/blob');

module.exports = async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  // Cache for 1 hour — cron refreshes daily anyway
  res.setHeader('Cache-Control', 'public, s-maxage=3600, stale-while-revalidate=7200');

  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'GET')     return res.status(405).json({ error: 'Method not allowed' });

  try {
    let data;

    // Try Vercel Blob first (live data updated by daily cron)
    try {
      const { blobs } = await list({ prefix: 'listings-data.json' });
      if (blobs.length > 0) {
        const resp = await fetch(blobs[0].url);
        data = await resp.json();
      }
    } catch { /* fall through to local file */ }

    // Fallback to static file if Blob not populated yet
    if (!data) {
      const filePath = path.join(process.cwd(), 'data', 'listings.json');
      const raw      = fs.readFileSync(filePath, 'utf8');
      data           = JSON.parse(raw);
    }

    // Optional query param: ?type=active|sold|reviews|all (default: all)
    const { type = 'all' } = req.query || {};

    if (type === 'active') {
      return res.status(200).json({
        meta: data._meta,
        listings: data.active_listings,
      });
    }
    if (type === 'sold') {
      return res.status(200).json({
        meta: data._meta,
        listings: data.sold_listings,
      });
    }
    if (type === 'reviews') {
      return res.status(200).json({
        meta: data._meta,
        reviews: data.reviews,
      });
    }

    // Default: return everything
    return res.status(200).json(data);

  } catch (err) {
    console.error('Listings fetch error:', err.message);
    return res.status(500).json({ error: 'Could not load listings data' });
  }
};
