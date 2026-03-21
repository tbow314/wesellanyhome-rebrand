# Go Live on Vercel — DNS Transfer Steps

## For Mario Rudolph
**Your site is ready to go live. Follow these exact steps to activate it.**

---

## Step 1: Log Into Your Wix Account
1. Go to **wix.com** and sign in
2. Open your **wesellanyhome.com** site

---

## Step 2: Find Domain Settings
1. Click **Settings** (bottom left sidebar)
2. Click **Domains**
3. Find **wesellanyhome.com** in the list
4. Click on it to open domain settings

---

## Step 3: Update Nameservers
You'll see a section called **"Nameservers"** or **"DNS"**

### REMOVE these (current Wix nameservers):
- `ns12.wixdns.net`
- `ns13.wixdns.net`

### ADD these (Vercel nameservers):
- `ns1.vercel-dns.com`
- `ns2.vercel-dns.com`

**⚠️ IMPORTANT:** Only add TWO nameservers. Do NOT add ns3 or ns4.

---

## Step 4: Save & Wait
1. Click **Save**
2. Wait 24-48 hours for changes to propagate
3. Your site will automatically switch to live on Vercel when propagation completes

---

## Done!
Once it goes live, your site at **wesellanyhome.com** will point to Vercel instead of Wix.

**Questions?** Contact Tyler (BowenAIstrategygroup@gmail.com)
