/**
 * GEO Content Refresh Script — WeSellAnyHome
 *
 * Updates the "last updated" date in llms.txt, validates all GEO assets,
 * regenerates sitemap dates, and outputs a summary checklist.
 *
 * Run: npx ts-node scripts/geo-content-refresh.ts
 * Or:  npm run geo-refresh
 */

import * as fs from "fs";
import * as path from "path";

const ROOT = path.resolve(__dirname, "..");
const today = new Date().toISOString().split("T")[0];

const GEO_ASSETS = [
  { path: "public/robots.txt", description: "robots.txt (AI crawler directives)" },
  { path: "public/llms.txt", description: "llms.txt (LLM-readable site summary)" },
  { path: "public/sitemap.xml", description: "sitemap.xml (search engine sitemap)" },
  { path: "index.html", description: "Homepage with JSON-LD schema" },
  { path: "faq.html", description: "FAQ page with FAQPage schema" },
  { path: "neighborhoods/allegheny-county.html", description: "Allegheny County landing page" },
  { path: "neighborhoods/washington-county.html", description: "Washington County landing page" },
  { path: "neighborhoods/westmoreland-county.html", description: "Westmoreland County landing page" },
  { path: "neighborhoods/butler-county.html", description: "Butler County landing page" },
  { path: "neighborhoods/mt-lebanon.html", description: "Mt. Lebanon neighborhood page" },
  { path: "neighborhoods/bethel-park.html", description: "Bethel Park neighborhood page" },
  { path: "neighborhoods/upper-st-clair.html", description: "Upper St. Clair neighborhood page" },
  { path: "neighborhoods/north-hills.html", description: "North Hills neighborhood page" },
  { path: "neighborhoods/monroeville.html", description: "Monroeville neighborhood page" },
  { path: "neighborhoods/canonsburg.html", description: "Canonsburg neighborhood page" },
  { path: "public/pittsburgh-real-estate-faq.html", description: "Pittsburgh Real Estate FAQ (extended)" },
  { path: "public/pittsburgh-real-estate-guide.html", description: "Pittsburgh Real Estate Guide" },
  { path: "pittsburgh-housing-market-2026.html", description: "Pittsburgh Housing Market 2026" },
  { path: "pittsburgh-real-estate-statistics-2026.html", description: "Pittsburgh Real Estate Statistics 2026" },
  { path: "local-intel/article-1-mt-lebanon-honest-guide.html", description: "Local Intel: Mt. Lebanon Guide" },
  { path: "local-intel/article-2-upper-st-clair-vs-mt-lebanon.html", description: "Local Intel: USC vs Lebo" },
  { path: "local-intel/article-3-pittsburgh-neighborhoods-best-value-2026.html", description: "Local Intel: Best Value Neighborhoods" },
  { path: "local-intel/article-4-moving-to-pittsburgh-guide.html", description: "Local Intel: Moving to Pittsburgh" },
  { path: "local-intel/article-5-washington-county-homebuyers.html", description: "Local Intel: Washington County Guide" },
];

function updateLlmsTxtDate(): void {
  const llmsPath = path.join(ROOT, "public/llms.txt");
  let content = fs.readFileSync(llmsPath, "utf-8");
  content = content.replace(/Last updated: \d{4}-\d{2}-\d{2}/, `Last updated: ${today}`);
  fs.writeFileSync(llmsPath, content, "utf-8");
  console.log(`  Updated llms.txt date to ${today}`);
}

function updateSitemapDates(): void {
  const sitemapPath = path.join(ROOT, "public/sitemap.xml");
  let content = fs.readFileSync(sitemapPath, "utf-8");
  content = content.replace(/<lastmod>\d{4}-\d{2}-\d{2}<\/lastmod>/g, `<lastmod>${today}</lastmod>`);
  fs.writeFileSync(sitemapPath, content, "utf-8");
  console.log(`  Updated sitemap.xml dates to ${today}`);
}

function validateAssets(): { found: string[]; missing: string[] } {
  const found: string[] = [];
  const missing: string[] = [];

  for (const asset of GEO_ASSETS) {
    const fullPath = path.join(ROOT, asset.path);
    if (fs.existsSync(fullPath)) {
      found.push(asset.description);
    } else {
      missing.push(`${asset.description} (${asset.path})`);
    }
  }

  return { found, missing };
}

function main(): void {
  console.log("========================================");
  console.log("  WeSellAnyHome GEO Content Refresh");
  console.log(`  Date: ${today}`);
  console.log("========================================\n");

  console.log("1. Updating llms.txt date...");
  updateLlmsTxtDate();

  console.log("\n2. Updating sitemap.xml dates...");
  updateSitemapDates();

  console.log("\n3. Validating GEO assets...\n");
  const { found, missing } = validateAssets();

  for (const item of found) {
    console.log(`  [OK] ${item}`);
  }
  for (const item of missing) {
    console.log(`  [MISSING] ${item}`);
  }

  console.log("\n========================================");
  console.log("  SUMMARY");
  console.log("========================================");
  console.log(`  Files validated: ${found.length + missing.length}`);
  console.log(`  Files found:     ${found.length}`);
  console.log(`  Files missing:   ${missing.length}`);
  console.log(`  Date updated:    ${today}`);

  const nextRun = new Date();
  nextRun.setMonth(nextRun.getMonth() + 1);
  console.log(`  Next run:        ${nextRun.toISOString().split("T")[0]}`);
  console.log("========================================\n");

  if (missing.length > 0) {
    console.log("  WARNING: Missing files detected. Create them before deploying.");
    process.exit(1);
  } else {
    console.log("  All GEO assets validated. Ready for deployment.");
  }
}

main();
