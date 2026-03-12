# We Sell Any Home - Skills Inventory

**Updated:** March 2026
**Purpose:** Track available AI agent skills for SEO, marketing, and GEO optimization

---

## Overview

The We Sell Any Home project has access to **two complementary skill sets**:

1. **Marketing Skills** (`marketingskills/`) - General marketing, CRO, content, copywriting, SEO
2. **GEO-SEO Skills** (`geoseo-skills/`) - AI search optimization, citability scoring, brand scanning, platform analysis

Together, these provide comprehensive coverage from traditional SEO to emerging AI search optimization.

---

## 1. Marketing Skills Suite

**Repository:** `marketingskills/` (GitHub: coreyhaines31/marketingskills)
**Version:** v2.0+
**Purpose:** Traditional marketing automation, CRO, SEO, content strategy, copywriting, paid ads

### Primary Skills by Category

#### SEO & Content (Foundation)
| Skill | Trigger | Best For |
|-------|---------|----------|
| `seo-audit` | User asks "audit" or "SEO review" | Comprehensive SEO analysis of website |
| `ai-seo` | User asks about "AI search" or "LLM" ranking | Optimizing for ChatGPT, Claude, Perplexity |
| `site-architecture` | "restructure site" or "URL structure" | Planning site hierarchy and navigation |
| `schema-markup` | "schema" or "structured data" | Adding JSON-LD for search engines |
| `programmatic-seo` | "generate pages at scale" or "templates" | Creating 15 neighborhood guides efficiently |
| `content-strategy` | "content plan" or "what to write" | Planning content roadmap |

#### Copywriting & Content Creation
| Skill | Trigger | Best For |
|-------|---------|----------|
| `copywriting` | "write copy" or "homepage text" | Creating marketing page text |
| `copy-editing` | "edit this copy" or "improve wording" | Polishing existing content |
| `cold-email` | "cold email" or "outreach" | B2B email sequences |
| `email-sequence` | "email campaign" or "automation" | Lifecycle email flows |
| `social-content` | "social media" or "LinkedIn post" | Multi-platform content creation |

#### Conversion Optimization
| Skill | Trigger | Best For |
|-------|---------|----------|
| `page-cro` | "optimize page" or "conversions" | Improving landing page performance |
| `signup-flow-cro` | "signup optimization" | Registration flow improvement |
| `form-cro` | "form optimization" (non-signup) | Lead capture form improvement |
| `popup-cro` | "modal" or "popup" | Overlay/banner optimization |

#### Paid & Analytics
| Skill | Trigger | Best For |
|-------|---------|----------|
| `paid-ads` | "Google Ads" or "Meta ads" | Paid advertising campaigns |
| `ad-creative` | "ad variations" or "creative tests" | Bulk ad generation |
| `ab-test-setup` | "A/B test" or "experiment" | Testing & experimentation design |
| `analytics-tracking` | "GA4" or "tracking setup" | Event tracking implementation |

#### Strategy & Monetization
| Skill | Trigger | Best For |
|-------|---------|----------|
| `marketing-ideas` | "ideas" or "what should we do" | Creative campaign brainstorming |
| `marketing-psychology` | "psychology" or "behavioral" | Persuasion & customer psychology |
| `pricing-strategy` | "pricing" or "monetization" | Price optimization |
| `launch-strategy` | "launch" or "product release" | Product/feature announcements |

#### Growth & Retention
| Skill | Trigger | Best For |
|-------|---------|----------|
| `referral-program` | "referral" or "affiliate" | Word-of-mouth programs |
| `free-tool-strategy` | "calculator" or "free tool" | Lead generation tools |
| `churn-prevention` | "retention" or "cancellation" | Customer retention strategies |

#### Sales & RevOps
| Skill | Trigger | Best For |
|-------|---------|----------|
| `revops` | "lead pipeline" or "scoring" | Sales operations & lead management |
| `sales-enablement` | "sales deck" or "pitch" | Sales collateral creation |
| `competitor-alternatives` | "competitor" or "comparison" | Competitive positioning pages |

---

## 2. GEO-SEO Skills Suite

**Repository:** `geoseo-skills/` (GitHub: zubair-trabzada/geo-seo-claude)
**Version:** 1.0+
**Purpose:** AI search optimization, GEO audit, citability scoring, platform-specific analysis, brand scanning

### Core Commands

| Command | What It Does | Best For |
|---------|-------------|----------|
| `/geo audit <url>` | Full GEO + SEO audit with parallel subagents | Comprehensive AI search readiness assessment |
| `/geo quick <url>` | 60-second GEO visibility snapshot | Quick health check |
| `/geo citability <url>` | Score content for AI citation readiness | Evaluating if content will be cited by LLMs |
| `/geo crawlers <url>` | Check AI crawler access (robots.txt analysis) | Verify GPTBot, ClaudeBot, PerplexityBot, etc. can access |
| `/geo llmstxt <url>` | Analyze or generate llms.txt file | Create/validate emerging llms.txt standard |
| `/geo brands <url>` | Scan brand mentions across platforms | Find where brand is mentioned (YouTube, Reddit, etc.) |
| `/geo platforms <url>` | Platform-specific optimization | Optimize for ChatGPT vs Perplexity vs Google AI Overviews |
| `/geo schema <url>` | Structured data analysis & generation | Check/improve JSON-LD schema |
| `/geo technical <url>` | Technical SEO audit | Analyze Core Web Vitals, SSR, mobile, security |
| `/geo content <url>` | Content quality & E-E-A-T assessment | Evaluate expertise, authority, trustworthiness |
| `/geo report <url>` | Generate client-ready markdown report | Create professional GEO report |
| `/geo report-pdf` | Generate professional PDF report | Create PDF with charts & visualizations |

### Scoring Methodology

GEO score is calculated from 6 weighted categories:

| Category | Weight | Key Factors |
|----------|--------|------------|
| AI Citability & Visibility | 25% | Content blocks optimized for AI citation (134-167 words, fact-rich, self-contained) |
| Brand Authority Signals | 20% | Brand mentions across YouTube, Reddit, Wikipedia, LinkedIn (3x stronger than backlinks) |
| Content Quality & E-E-A-T | 20% | Expertise, Experience, Authority, Trustworthiness signals |
| Technical Foundations | 15% | Core Web Vitals, mobile responsiveness, SSL security, SSR capability |
| Structured Data | 10% | JSON-LD schema completeness and accuracy |
| Platform Optimization | 10% | ChatGPT-specific, Google AIO-specific, Perplexity-specific optimizations |

### Architecture

**Parallel Subagents** (run simultaneously for speed):
- `geo-ai-visibility.md` - Citability scoring, crawler analysis, llms.txt, brand scanning
- `geo-platform-analysis.md` - Platform-specific optimization (ChatGPT, Perplexity, Google AIO)
- `geo-technical.md` - Technical SEO foundations
- `geo-content.md` - Content quality & E-E-A-T evaluation
- `geo-schema.md` - Structured data analysis and generation

**Specialized Sub-Skills**:
- geo-audit, geo-citability, geo-crawlers, geo-llmstxt, geo-brand-mentions
- geo-platform-optimizer, geo-schema, geo-technical, geo-content
- geo-report (markdown), geo-report-pdf (professional PDF with charts)

---

## 3. Skill Integration & Usage Strategy

### For We Sell Any Home Project

#### Phase 1: Site Audit (GEO-FIRST)
Use **GEO-SEO Skills** first to understand AI search readiness:
```
/geo audit https://wesellanyhome.com
→ Generates GEO Score, citability assessment, crawler access, brand presence
```

#### Phase 2: Detailed Analysis (Marketing Skills)
Use **Marketing Skills** for specific optimization areas:
- `seo-audit` for keyword rankings & traditional SEO issues
- `ai-seo` for LLM citation optimization
- `schema-markup` to validate/improve JSON-LD
- `content-strategy` for blog/guide planning

#### Phase 3: Implementation (Hybrid)
- Use **programmatic-seo** to generate 15 neighborhood guide variations
- Use **schema-markup** to enhance structured data
- Use **content-strategy** for content calendar
- Use **copywriting** for hero sections and CTAs

#### Phase 4: Validation (GEO-FIRST)
After implementation, run `/geo audit` again to verify improvements:
- Citability scores improved?
- AI crawler access optimal?
- Brand mentions increasing?
- Content E-E-A-T signals stronger?

---

## 4. Specific Skills for Neighborhood Guides

The 15 Pittsburgh neighborhood guides need optimization across multiple dimensions:

### Step 1: Content Optimization
- **`ai-seo` skill** - Ensure content is citability-optimized for ChatGPT, Claude, Perplexity
- **`content-strategy` skill** - Plan guide structure and key topics
- **`copywriting` skill** - Write hero section and CTAs

### Step 2: Technical Setup
- **`schema-markup` skill** - Add Organization, LocalBusiness, BreadcrumbList schemas
- **`programmatic-seo` skill** - Generate templates for remaining 12 guides

### Step 3: SEO Audit
- **`seo-audit` skill** - Keyword rankings, on-page SEO, technical SEO check
- **`site-architecture` skill** - Internal linking strategy (guides → main site → tools)

### Step 4: GEO Validation
- **`/geo citability` command** - Score each guide for AI citation readiness
- **`/geo report <url>` command** - Generate comprehensive GEO report

---

## 5. Recommended Audit Workflow

### For We Sell Any Home Website

**Step 1: Quick Baseline (5 minutes)**
```
/geo quick https://wesellanyhome.com
```
→ Snapshot of current GEO health

**Step 2: Comprehensive Audit (15 minutes)**
```
/geo audit https://wesellanyhome.com
```
→ Full GEO Score, parallel subagent analysis, actionable report

**Step 3: Neighborhood Guide Analysis (2 minutes each)**
```
/geo citability https://wesellanyhome.com/neighborhoods/shadyside
/geo citability https://wesellanyhome.com/neighborhoods/downtown
/geo citability https://wesellanyhome.com/neighborhoods/lawrenceville
```
→ Score each guide for AI citation readiness

**Step 4: Platform-Specific Optimization (5 minutes)**
```
/geo platforms https://wesellanyhome.com
```
→ ChatGPT readiness vs. Google AIO vs. Perplexity optimization

**Step 5: Technical Validation (5 minutes)**
```
/geo technical https://wesellanyhome.com
```
→ Core Web Vitals, mobile, security, SSR check

**Step 6: Brand Scanning (5 minutes)**
```
/geo brands https://wesellanyhome.com
```
→ Find mentions on YouTube, Reddit, LinkedIn, Wikipedia

**Step 7: Schema Review (3 minutes)**
```
/geo schema https://wesellanyhome.com
```
→ Validate and improve JSON-LD markup

**Step 8: Professional Report Generation (2 minutes)**
```
/geo report https://wesellanyhome.com
```
→ Generates markdown report (for internal use)

```
/geo report-pdf https://wesellanyhome.com
```
→ Generates PDF report (for client delivery)

---

## 6. Key Metrics to Track

After audits, track these metrics over time:

**GEO-Specific (New)**
- GEO Score (target: 75+/100)
- Citability Score (target: 85+ for guides)
- AI Crawler Access (GPTBot, ClaudeBot, PerplexityBot = allowed)
- Brand Mention Count (especially on YouTube, Reddit, LinkedIn)
- Platform Optimization Score (ChatGPT, Google AIO, Perplexity)

**Traditional SEO (Existing)**
- Keyword Rankings (track top 20 keywords weekly)
- Organic Traffic (Google Analytics)
- Pages Indexed (Google Search Console)
- Backlink Count & Quality
- Core Web Vitals (LCP, FID, CLS)

**Conversion (Business)**
- Form Submissions (organic traffic)
- Phone Calls (organic traffic)
- Leads Qualified
- Sales Attributed to Organic/AI

---

## 7. Next Steps

1. ✅ Add both skill repositories as submodules
2. ✅ Document skills inventory (this file)
3. **→ Run `/geo audit` on main website** (comprehensive baseline)
4. **→ Run `/geo citability` on neighborhood guides** (citability scoring)
5. **→ Use `seo-audit` for keyword rankings** (traditional SEO baseline)
6. **→ Generate `/geo report-pdf`** (comprehensive audit report)
7. **→ Address top 10 issues** from GEO & SEO audits
8. **→ Re-run audits** to verify improvements

---

## 8. Commands Quick Reference

### GEO-SEO Commands
```bash
# Quick checks
/geo quick https://wesellanyhome.com

# Detailed audits
/geo audit https://wesellanyhome.com
/geo citability https://wesellanyhome.com/neighborhoods/shadyside
/geo platforms https://wesellanyhome.com
/geo technical https://wesellanyhome.com
/geo schema https://wesellanyhome.com
/geo brands https://wesellanyhome.com
/geo crawlers https://wesellanyhome.com
/geo llmstxt https://wesellanyhome.com

# Reports
/geo report https://wesellanyhome.com
/geo report-pdf https://wesellanyhome.com
```

### Marketing Skills (Examples)
```bash
/seo-audit https://wesellanyhome.com
/ai-seo [for AI search optimization]
/schema-markup [for JSON-LD validation]
/programmatic-seo [for template generation]
/content-strategy [for content planning]
```

---

## Support & Resources

- **Marketing Skills Repo:** `./marketingskills/README.md`
- **GEO Skills Repo:** `./geoseo-skills/README.md`
- **Product Marketing Context:** `./clients/wesellanyhome/product-marketing-context.md`
- **SEO Strategy:** `./clients/wesellanyhome/SEO-AI-RANKING-STRATEGY.md`
- **Neighborhood Template:** `./clients/wesellanyhome/NEIGHBORHOOD-GUIDE-TEMPLATE.md`

---

**Last Updated:** March 11, 2026
**Status:** Skills integrated and ready for audit phase
