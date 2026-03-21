# Email Integration Process — We Sell Any Home

## Problem Solved
Form submissions now send via Resend API through Vercel serverless function instead of Netlify Forms.

## Architecture
```
HTML Form (index.html)
  ↓ POST to /api/contact
Vercel Serverless Function (api/contact.js)
  ↓ uses Resend API
Resend Email Service
  ↓ sends to CONTACT_TO + CONTACT_BCC
Client inbox + Your inbox (BCC)
```

## Implementation Steps

### 1. Form Setup (index.html)
- Change form from `name="lead-capture" netlify` to `action="/api/contact" method="POST"`
- Add hidden field: `<input type="hidden" name="formType" value="lead" />`
- Form fields collected: `name`, `email`, `phone`, `area`, `county`, `neighborhood`, `intent`, `message`

### 2. Serverless Function (api/contact.js)
Already configured—reads environment variables and sends via Resend:
- **CONTACT_TO**: Recipients (comma-separated)
- **CONTACT_BCC**: Your blind copy addresses (comma-separated)
- **CONTACT_FROM**: Sender address (e.g., noreply@bowenaistrategygroup.com)
- **RESEND_API_KEY**: Resend API key

### 3. Deploy
```bash
vercel --prod
```

## Troubleshooting: BCC Not Working

**Most likely cause**: Resend requires **verified domain** to use BCC. Currently using `onboarding@resend.dev` (sandbox).

**Fix**:
1. Update CONTACT_FROM to use your actual domain (e.g., `noreply@bowenaistrategygroup.com`)
2. Verify the domain in Resend dashboard
3. Once verified, BCC will start working

**Check logs**:
```bash
vercel logs https://www.wesellanyhome.com
```

Look for Resend API errors in function logs (line 94-96 of contact.js logs any failures).

## Testing
1. Submit pre-approval form
2. Check client receives email at CONTACT_TO
3. Check your inbox receives BCC copy
4. If no BCC, check Resend domain verification status

## Reference for Future Projects
Use this same pattern for all client sites:
- Form → `/api/contact` endpoint
- Serverless function handles all email logic
- Environment variables control recipients
- One reusable function across all projects
