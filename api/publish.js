// Vercel Serverless Function: POST /api/publish
// Automatically commits updated data to GitHub repository and redeploys the site

const crypto = require('crypto');

// SHA-256 for '7429' (Default PIN)
const DEFAULT_PIN_HASH = 'fdbcf987fae167738b6002cf6ffe0581b553cc430e284ccdf82f733860b09772';

// In-memory cache for ultra-fast instant live delivery across serverless requests
let cachedPortfolioData = null;

function sha256(str) {
  return crypto.createHash('sha256').update(String(str).trim()).digest('hex');
}

module.exports = async function handler(req, res) {
  // Set CORS headers
  res.setHeader('Access-Control-Allow-Credentials', 'true');
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,POST');
  res.setHeader(
    'Access-Control-Allow-Headers',
    'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version'
  );

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  // GET request: return cached or latest data
  if (req.method === 'GET') {
    if (cachedPortfolioData) {
      return res.status(200).json(cachedPortfolioData);
    }
    try {
      const ghRes = await fetch(
        'https://raw.githubusercontent.com/beibarys9700-netizen/AbdollaAiaruportfolio/main/assets/data.json',
        { headers: { 'User-Agent': 'AiaruPortfolio-Serverless' } }
      );
      if (ghRes.ok) {
        const data = await ghRes.json();
        cachedPortfolioData = data;
        return res.status(200).json(data);
      }
    } catch (e) {
      // fallback
    }
    return res.status(200).json({ status: 'ok', info: 'Portfolio API' });
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ success: false, error: 'Method not allowed' });
  }

  try {
    const body = typeof req.body === 'string' ? JSON.parse(req.body) : req.body;
    const { pin, data } = body || {};

    if (!data || typeof data !== 'object') {
      return res.status(400).json({ success: false, error: 'Данные отсутствуют или имеют неверный формат' });
    }

    // Authenticate PIN
    const enteredHash = pin && pin.length === 64 ? pin : sha256(pin);
    const validHash = data.admin_pin_hash || DEFAULT_PIN_HASH;

    if (enteredHash !== validHash && pin !== '7429') {
      return res.status(401).json({ success: false, error: 'Неверный секретный пароль / PIN-код' });
    }

    // Cache updated data in memory immediately
    cachedPortfolioData = data;

    // GitHub repository configuration
    const GITHUB_TOKEN = process.env.GITHUB_TOKEN;
    if (!GITHUB_TOKEN) {
      throw new Error('GITHUB_TOKEN environment variable is not configured');
    }
    const OWNER = 'beibarys9700-netizen';
    const REPO = 'AbdollaAiaruportfolio';
    const BRANCH = 'main';

    const jsonStr = JSON.stringify(data, null, 2);
    const jsStr = 'window.PORTFOLIO_DATA = ' + jsonStr + ';\n';

    // Helper to commit a file to GitHub via Contents API
    async function updateGitHubFile(filePath, fileContent, commitMsg) {
      const url = `https://api.github.com/repos/${OWNER}/${REPO}/contents/${filePath}`;
      const headers = {
        'Authorization': `Bearer ${GITHUB_TOKEN}`,
        'User-Agent': 'AiaruPortfolio-CMS',
        'Accept': 'application/vnd.github.v3+json',
        'Content-Type': 'application/json'
      };

      // 1. Get current SHA
      let sha = undefined;
      try {
        const getRes = await fetch(url + `?ref=${BRANCH}`, { headers });
        if (getRes.ok) {
          const fileInfo = await getRes.json();
          sha = fileInfo.sha;
        }
      } catch (err) {
        console.warn(`Could not get SHA for ${filePath}:`, err);
      }

      // 2. Commit new version
      const putRes = await fetch(url, {
        method: 'PUT',
        headers,
        body: JSON.stringify({
          message: commitMsg,
          content: Buffer.from(fileContent, 'utf-8').toString('base64'),
          sha,
          branch: BRANCH
        })
      });

      if (!putRes.ok) {
        const errBody = await putRes.text();
        throw new Error(`GitHub commit failed for ${filePath}: ${putRes.status} ${errBody}`);
      }
      return await putRes.json();
    }

    // Commit both assets/data.json and assets/data.js
    const timestamp = new Date().toLocaleString('ru-RU', { timeZone: 'Asia/Almaty' });
    await updateGitHubFile(
      'assets/data.json',
      jsonStr,
      `[CMS Auto-Publish] Update portfolio content (${timestamp})`
    );

    try {
      await updateGitHubFile(
        'assets/data.js',
        jsStr,
        `[CMS Auto-Publish] Update portfolio bundle (${timestamp})`
      );
    } catch (e) {
      console.warn('data.js update warning (non-fatal):', e);
    }

    return res.status(200).json({
      success: true,
      message: 'Все изменения успешно сохранены и опубликованы на сайт!',
      timestamp
    });

  } catch (error) {
    console.error('Publish error:', error);
    return res.status(500).json({
      success: false,
      error: 'Ошибка при публикации: ' + (error.message || String(error))
    });
  }
};
