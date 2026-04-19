"""IndexNow ping — notify Bing (and ChatGPT via Bing) of content changes.

Usage:
  python scripts/indexnow-ping.py                      # pings every URL in public/sitemap.xml
  python scripts/indexnow-ping.py --since 2026-04-19   # only URLs with lastmod >= this date
  python scripts/indexnow-ping.py --url https://...    # ping a single URL (repeatable)
  python scripts/indexnow-ping.py --dry-run            # print payload, no POST

Works for any site — reads config from INDEXNOW_CONFIG below.

Why this matters:
  ChatGPT web search queries run through Bing. If Bing doesn't see fresh content,
  ChatGPT can't cite it. IndexNow is Bing's explicit low-latency indexing channel
  (30-day average → minutes). Run this after every meaningful content push.
"""
import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path

# Per-host config. Pick based on the first <loc> in the sitemap.
INDEXNOW_CONFIG = {
    "www.bowenaistrategygroup.com": {
        "key": "bowenai-indexnow-2026",
        "keyLocation": "https://www.bowenaistrategygroup.com/bowenai-indexnow-2026.txt",
    },
    "bowenaistrategygroup.com": {
        "key": "bowenai-indexnow-2026",
        "keyLocation": "https://www.bowenaistrategygroup.com/bowenai-indexnow-2026.txt",
    },
    "wesellanyhome.com": {
        "key": "a1b2c3d4e5f6g7h8",
        "keyLocation": "https://www.wesellanyhome.com/a1b2c3d4e5f6g7h8.txt",
        "canonical_host": "www.wesellanyhome.com",
    },
    "www.wesellanyhome.com": {
        "key": "a1b2c3d4e5f6g7h8",
        "keyLocation": "https://www.wesellanyhome.com/a1b2c3d4e5f6g7h8.txt",
        "canonical_host": "www.wesellanyhome.com",
    },
}

ENDPOINTS = [
    "https://www.bing.com/indexnow",
    "https://api.indexnow.org/indexnow",
    "https://yandex.com/indexnow",
]


def parse_sitemap(path: Path):
    """Return list of (url, lastmod) tuples from sitemap.xml."""
    text = path.read_text(encoding="utf-8")
    entries = []
    for m in re.finditer(r"<url>(.*?)</url>", text, re.DOTALL):
        block = m.group(1)
        loc = re.search(r"<loc>([^<]+)</loc>", block)
        mod = re.search(r"<lastmod>([^<]+)</lastmod>", block)
        if loc:
            entries.append((loc.group(1).strip(), mod.group(1).strip() if mod else ""))
    return entries


def host_from_url(url: str) -> str:
    m = re.match(r"https?://([^/]+)", url)
    return m.group(1) if m else ""


def ping(host: str, key: str, key_location: str, urls, dry_run=False):
    payload = {
        "host": host,
        "key": key,
        "keyLocation": key_location,
        "urlList": urls,
    }
    body = json.dumps(payload).encode("utf-8")
    print(f"[IndexNow] host={host} urls={len(urls)}")
    if dry_run:
        print(json.dumps(payload, indent=2))
        return
    for endpoint in ENDPOINTS:
        req = urllib.request.Request(
            endpoint,
            data=body,
            method="POST",
            headers={"Content-Type": "application/json; charset=utf-8"},
        )
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                status = resp.status
                body_text = resp.read().decode("utf-8", errors="replace")[:200]
            print(f"  {endpoint}: HTTP {status} {body_text}")
        except urllib.error.HTTPError as e:
            print(f"  {endpoint}: HTTP {e.code} {e.reason}")
        except Exception as e:
            print(f"  {endpoint}: {type(e).__name__}: {e}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sitemap", default="public/sitemap.xml")
    ap.add_argument("--since", help="Only URLs with lastmod >= this date (YYYY-MM-DD)")
    ap.add_argument("--url", action="append", default=[], help="Single URL (repeatable)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    urls = []
    if args.url:
        urls = list(args.url)
    else:
        sitemap_path = Path(args.sitemap)
        if not sitemap_path.exists():
            print(f"sitemap not found: {sitemap_path}", file=sys.stderr)
            sys.exit(1)
        entries = parse_sitemap(sitemap_path)
        if args.since:
            urls = [u for u, m in entries if m and m >= args.since]
        else:
            urls = [u for u, _ in entries]

    if not urls:
        print("No URLs to ping.")
        sys.exit(0)

    host = host_from_url(urls[0])
    if host not in INDEXNOW_CONFIG:
        print(f"No IndexNow config for host '{host}'. Add one to INDEXNOW_CONFIG.", file=sys.stderr)
        sys.exit(1)

    cfg = INDEXNOW_CONFIG[host]
    # Rewrite URLs to canonical host if specified (Bing requires host == URL host)
    canonical = cfg.get("canonical_host", host)
    if canonical != host:
        urls = [u.replace(f"://{host}", f"://{canonical}", 1) for u in urls]

    # Bing rejects payloads >10k URLs; chunk to be safe.
    for i in range(0, len(urls), 5000):
        chunk = urls[i : i + 5000]
        ping(canonical, cfg["key"], cfg["keyLocation"], chunk, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
