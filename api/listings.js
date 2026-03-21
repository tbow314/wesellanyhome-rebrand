// Vercel Serverless Function — serves listings from data/listings.json
const fs   = require('fs');
const path = require('path');

module.exports = async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Cache-Control', 'public, s-maxage=3600, stale-while-revalidate=7200');

  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'GET')     return res.status(405).json({ error: 'Method not allowed' });

  try {
    const filePath = path.join(process.cwd(), 'data', 'listings.json');
    const data     = JSON.parse(fs.readFileSync(filePath, 'utf8'));
    return res.status(200).json(data);
  } catch (err) {
    console.error('Listings error:', err.message);
    return res.status(500).json({ error: 'Could not load listings' });
  }
};
