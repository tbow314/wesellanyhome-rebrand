# Email Delivery Setup Guide — We Sell Any Home

## Problem
Forms using Netlify's `netlify` attribute don't work when deployed to Vercel. The form submissions fail silently because Vercel uses serverless functions, not Netlify's form handler.

## Solution
Route form submissions through a Vercel serverless function (`/api/contact.js`) that integrates with Resend for email delivery.

---

## Implementation Steps

### 1. Update the Form Element
Change from Netlify forms to POST to the serverless function:

**Before:**
```html
<form id="leadForm" name="lead-capture" method="POST" netlify class="flex flex-wrap gap-2 items-center justify-center" novalidate>
```

**After:**
```html
<form id="leadForm" action="/api/contact" method="POST" class="flex flex-wrap gap-2 items-center justify-center" novalidate>
```

### 2. Add Form Type Identifier
Include a hidden field to identify which form type is being submitted:
```html
<input type="hidden" name="formType" value="lead" />
```

**Form type values:**
- `lead` — Pre-approval/lead capture forms
- `contact` — General contact forms
- `guide` — Neighborhood guide requests

### 3. Verify the Serverless Function
Check that `/api/contact.js` exists and is properly configured. It should:
- Accept POST requests with form data
- Extract fields: `name`, `email`, `phone`, `area`, `county`, `neighborhood`, `intent`, `message`, `formType`
- Build an HTML email template
- Call Resend API to send emails
- Return JSON response with `{ success: true }` or error

### 4. Configure Environment Variables
The following environment variables must be set in Vercel:

| Variable | Purpose | Example |
|----------|---------|---------|
| `RESEND_API_KEY` | Resend API authentication | `re_xyz...` |
| `CONTACT_TO` | Recipient email(s) | `mario@wesellanyhome.com` |
| `CONTACT_BCC` | BCC email(s) for agency | `agency@bowenaistrategygroup.com` |
| `CONTACT_FROM` | Sender email address | `We Sell Any Home <noreply@bowenaistrategygroup.com>` |

**To set environment variables:**
```bash
vercel env add RESEND_API_KEY
vercel env add CONTACT_TO
vercel env add CONTACT_BCC
vercel env add CONTACT_FROM
```

Or configure in Vercel Dashboard → Project Settings → Environment Variables

### 5. Deploy to Production
```bash
vercel --prod
```

Wait for the deployment to complete and show "Aliased: https://www.wesellanyhome.com"

### 6. Verify Environment Variables
```bash
vercel env ls
```

Confirm all 4 required variables show as "Encrypted" and are available in Production, Preview, and Development environments.

---

## Testing the Form

1. Visit https://www.wesellanyhome.com
2. Locate the pre-approval form (below the "Start Your Preapproval" button in hero section)
3. Fill in test data:
   - Name: "Test User"
   - Email: "test@example.com" (your test email)
   - Area: Select any area
   - Intent: Select any option
4. Click "Submit"
5. Check email for the submission confirmation

**Expected result:** Email arrives at the `CONTACT_TO` address with the form data formatted in an HTML table, plus BCC to `CONTACT_BCC`.

---

## Troubleshooting

### Form submits but no email received
- ✓ Check environment variables are set: `vercel env ls`
- ✓ Verify RESEND_API_KEY is valid (get from https://resend.com)
- ✓ Check CONTACT_TO and CONTACT_FROM emails are correct
- ✓ Check Resend account for any delivery failures
- ✓ Run `vercel logs <deployment-url>` to see function errors

### Form shows error message
- ✓ Check browser console for the error response
- ✓ Verify form is POSTing to `/api/contact` (not `/api/contact.js`)
- ✓ Ensure all form fields have correct `name` attributes
- ✓ Check `/api/contact.js` file exists in project root or `/api/` directory

### Deployment shows environment variable warnings
- ✓ This is normal — Vercel shows encrypted values as "Encrypted"
- ✓ Re-run `vercel env pull` locally to update `.env.local` for testing

---

## Form Field Reference

### Standard Form Fields
| Field Name | Type | Required | Example Value |
|-----------|------|----------|----------------|
| `name` | text | Yes | "John Smith" |
| `email` | email | Yes | "john@example.com" |
| `phone` | tel | No | "(412) 555-1234" |
| `area` | select | No | "Pittsburgh" |
| `county` | text | No | "Allegheny" |
| `neighborhood` | text | No | "Mt. Lebanon" |
| `intent` | select | No | "Buy" |
| `message` | textarea | No | "Looking for a 3-bed home..." |
| `formType` | hidden | Yes | "lead" / "contact" / "guide" |

---

## API Response Format

**Success Response:**
```json
{
  "success": true
}
```

**Error Response:**
```json
{
  "error": "Email delivery failed"
}
```

---

## Common Email Customizations

### Change Recipient Email
```bash
vercel env rm CONTACT_TO
vercel env add CONTACT_TO
# Enter new email address
vercel --prod  # Redeploy
```

### Add Multiple Recipients
Set `CONTACT_TO` as comma-separated list:
```
mario@wesellanyhome.com,agent2@wesellanyhome.com,agent3@wesellanyhome.com
```

### Update Email Subject Line
The email subject is auto-generated based on `formType`:
- `lead` → "🏠 New Pre-Approval Request — [Name]"
- `contact` → "🏠 New Contact Form — [Name]"
- `guide` → "🏠 New Neighborhood Guide Request — [Name]"

To customize, edit `/api/contact.js` around line 27:
```javascript
const formLabels = {
  lead:    'Pre-Approval Request',
  contact: 'Contact Form',
  guide:   'Neighborhood Guide Request',
};
```

---

## Files Involved

- **`index.html`** — Form HTML with `action="/api/contact"` and `formType` hidden field
- **`api/contact.js`** — Vercel serverless function that handles email delivery via Resend
- **`.env.local`** — Local environment variables (pull with `vercel env pull`)
- **Vercel Dashboard** — Production environment variables configuration

---

## Quick Reference Commands

```bash
# Pull environment variables locally
vercel env pull

# Deploy to production
vercel --prod

# View environment variables
vercel env ls

# Check deployment logs
vercel logs https://www.wesellanyhome.com

# Inspect latest deployment
vercel inspect
```

---

**Last Updated:** March 19, 2026
**Status:** ✅ Deployed and verified
**Next Steps:** Test form on production site and monitor for email delivery
