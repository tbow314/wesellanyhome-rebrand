// Vercel Serverless Function — returns live stats from env vars
// Update SALES_COUNT and SALES_LAST_12 in Vercel dashboard to auto-redeploy
module.exports = function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Cache-Control', 's-maxage=60');
  res.status(200).json({
    salesCount:   process.env.SALES_COUNT    || '171',
    salesLast12:  process.env.SALES_LAST_12  || '20',
  });
};
