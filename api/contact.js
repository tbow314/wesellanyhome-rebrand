// Vercel Serverless Function — handles all form submissions via Resend
// Reusable across all client sites — recipients controlled via env vars:
//   RESEND_API_KEY   — your Resend API key (same across all projects)
//   CONTACT_FROM     — sender address e.g. noreply@bowenaistrategygroup.com
//   CONTACT_TO       — comma-separated recipient emails
//   CONTACT_BCC      — comma-separated BCC emails (your agency address)

module.exports = async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  const { name, email, phone, area, county, neighborhood, intent, message, formType } = req.body || {};

  if (!name || !email) {
    return res.status(400).json({ error: 'Name and email are required' });
  }

  const formLabels = {
    lead:    'Pre-Approval Request',
    contact: 'Contact Form',
    guide:   'Neighborhood Guide Request',
  };
  const label = formLabels[formType] || 'Website Inquiry';

  const now = new Date().toLocaleString('en-US', {
    timeZone: 'America/New_York',
    dateStyle: 'medium',
    timeStyle: 'short',
  });

  const rows = [
    ['Name',          name],
    ['Email',         `<a href="mailto:${email}" style="color:#1a2660">${email}</a>`],
    phone        ? ['Phone',        phone]                            : null,
    area         ? ['Area',         area]                             : null,
    county       ? ['County',       county]                           : null,
    neighborhood ? ['Neighborhood', neighborhood]                     : null,
    intent       ? ['Interest',     intent]                           : null,
    message      ? ['Message',      message.replace(/\n/g, '<br>')] : null,
  ]
    .filter(Boolean)
    .map(([lbl, val]) => `
      <tr>
        <td style="padding:10px 12px;border-bottom:1px solid #f3f4f6;color:#6b7280;font-size:13px;white-space:nowrap;width:140px;">${lbl}</td>
        <td style="padding:10px 12px;border-bottom:1px solid #f3f4f6;font-size:14px;color:#111827;">${val}</td>
      </tr>`)
    .join('');

  const html = `
    <div style="font-family:Inter,Arial,sans-serif;max-width:600px;margin:0 auto;background:#f9fafb;padding:24px;">
      <div style="background:#0a0f2e;border-radius:10px 10px 0 0;padding:22px 24px;">
        <h1 style="color:#f5c842;margin:0;font-size:18px;font-weight:700;">🏠 New ${label}</h1>
        <p style="color:#9ca3af;margin:4px 0 0;font-size:13px;">We Sell Any Home · wesellanyhome.com</p>
      </div>
      <div style="background:#fff;border:1px solid #e5e7eb;border-top:none;border-radius:0 0 10px 10px;overflow:hidden;">
        <table style="width:100%;border-collapse:collapse;">${rows}</table>
        <div style="padding:16px 24px;background:#f9fafb;border-top:1px solid #f3f4f6;">
          <p style="margin:0;color:#374151;font-size:13px;">
            Reply directly to this email to reach <strong>${name}</strong> at ${email}.
          </p>
        </div>
      </div>
      <p style="text-align:center;color:#9ca3af;font-size:11px;margin-top:14px;">
        Submitted ${now} ET · wesellanyhome.com
      </p>
    </div>`;

  try {
    const toList  = (process.env.CONTACT_TO  || '').split(',').map(s => s.trim()).filter(Boolean);
    const bccList = (process.env.CONTACT_BCC || '').split(',').map(s => s.trim()).filter(Boolean);
    const from    = process.env.CONTACT_FROM || 'We Sell Any Home <noreply@bowenaistrategygroup.com>';

    const response = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${process.env.RESEND_API_KEY}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        from,
        to:       toList,
        bcc:      bccList,
        reply_to: email,
        subject:  `🏠 New ${label} — ${name}`,
        html,
      }),
    });

    const resBody = await response.json();
    if (!response.ok) {
      console.error('Resend error:', response.status, JSON.stringify(resBody));
      return res.status(500).json({ error: 'Email delivery failed', detail: resBody });
    }

    console.log('Resend success:', resBody.id);
    return res.status(200).json({ success: true });
  } catch (err) {
    console.error('Mail error:', err.message);
    return res.status(500).json({ error: 'Email delivery failed' });
  }
};
