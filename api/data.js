// Vercel Serverless Function: GET /api/data
// Returns current live portfolio JSON data

module.exports = async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS');
  res.setHeader('Cache-Control', 's-maxage=10, stale-while-revalidate=59');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  try {
    const ghRes = await fetch(
      'https://raw.githubusercontent.com/beibarys9700-netizen/AbdollaAiaruportfolio/main/assets/data.json',
      { headers: { 'User-Agent': 'AiaruPortfolio-Data-API' } }
    );
    if (ghRes.ok) {
      const data = await ghRes.json();
      return res.status(200).json(data);
    }
  } catch (err) {
    console.error('Fetch error:', err);
  }

  // Fallback to local file if available in serverless bundle
  try {
    const fs = require('fs');
    const path = require('path');
    const localPath = path.join(process.cwd(), 'assets', 'data.json');
    if (fs.existsSync(localPath)) {
      const localData = JSON.parse(fs.readFileSync(localPath, 'utf8'));
      return res.status(200).json(localData);
    }
  } catch (e) {}

  return res.status(404).json({ error: 'Data not found' });
};

