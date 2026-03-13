# We Sell Any Home - Skills Inventory & SEO Audit Capabilities

**Generated:** March 13, 2026
**Site:** https://wesellanyhome.vercel.app
**Purpose:** Document available SEO and GEO (Generative Engine Optimization) skills for We Sell Any Home's Pittsburgh real estate website

---

## Overview

This document catalogs two major skill repositories available for optimizing the We Sell Any Home website:
1. **geo-seo-claude** (11 specialized skills for AI search optimization)
2. **marketingskills** (existing marketing automation skills)

All skills are Git submodules in the claudecookbook repository at `/skills/`.

---

## GEO-SEO-Claude Skills (11 Available)

**Repository:** https://github.com/zubair-trabzada/geo-seo-claude.git
**Purpose:** Optimize for AI search engines (ChatGPT, Claude, Perplexity, Gemini, Google AI Overviews) while maintaining traditional SEO foundations

### Why GEO Matters for Real Estate

| Metric | Value | Relevance |
|--------|-------|-----------|
| GEO services market | $850M+ (projected $7.3B by 2031) | Growing buyer search behavior |
| AI-referred traffic growth | +527% YoY | Buyers use ChatGPT/Perplexity for neighborhood research |
| AI traffic converts vs organic | 4.4x higher | Better buyer intent |
| Gartner: traditional search drop by 2028 | -50% | Must optimize now |
| Brand mentions vs backlinks for AI | 3x stronger correlation | Build brand authority in AI era |

---

## 11 Available Skills

### 1. **geo-audit** ⭐ PRIMARY SKILL
Orchestrates comprehensive website GEO audit across 6 dimensions with parallel subagents. Produces composite GEO Score (0-100) with prioritized action plan.

**Use:** `/geo audit https://wesellanyhome.vercel.app`
**Duration:** 15-20 minutes
**Real Estate Application:** Comprehensive ranking assessment for neighborhood guides + agent visibility in AI search

---

### 2. **geo-citability** - AI Citation Readiness
Analyzes content to determine probability of citation across AI platforms. AI prefers 134-167 word passages that are self-contained, fact-rich, and directly answer questions.

**Real Estate Application:** Optimize agent bios and neighborhood guides for AI quotation

---

### 3. **geo-brand-mentions** - Authority Scanning
Scans 10+ platforms for brand mentions (YouTube, Reddit, Wikipedia, LinkedIn, Facebook, Twitter, TikTok, Instagram, Medium, Quora, Google Maps, Yelp).

**Finding:** Unlinked brand mentions correlate 3x more strongly with AI visibility than backlinks

**Real Estate Application:** Monitor where "We Sell Any Home" appears; identify Reddit, YouTube, and local Facebook group opportunities

---

### 4. **geo-crawlers** - AI Crawler Access
Checks robots.txt and headers to ensure site allows 14+ AI crawlers (GPTBot, ClaudeBot, PerplexityBot, etc.)

**Real Estate Application:** Verify Vercel site enables all major AI crawlers; prevent accidental blocking

---

### 5. **geo-schema** - Structured Data for AI
Detects existing JSON-LD and generates missing schemas based on business type.

**Real Estate Application:** Add LocalBusiness, Person (agents), Article (guides), Place (neighborhoods), AggregateOffer (pricing) schemas

---

### 6. **geo-platform-optimizer** - AI Platform-Specific
Audits against platform requirements: Google AI Overviews, ChatGPT, Perplexity, Gemini, Bing Copilot.

**Key Finding:** Only 11% of domains cited by both ChatGPT and Google AI Overviews

**Real Estate Application:** Tailor neighborhood guides for each platform's preferences

---

### 7. **geo-technical** - Technical SEO for AI
Audits crawlability, indexability, security, performance, server-side rendering, HTTPS, sitemap quality.

**Critical:** AI crawlers do not execute JavaScript (must be server-side rendered)

**Real Estate Application:** Verify Vercel deployment meets AI requirements

---

### 8. **geo-content** - Content Quality & E-E-A-T
Evaluates Experience, Expertise, Authoritativeness, Trustworthiness (now applies to ALL queries per Google Dec 2025).

**Real Estate Application:** Evaluate agent bios for expertise, neighborhood guides for authority, testimonials for trust

---

### 9. **geo-llmstxt** - LLMs.txt Standard
Generates llms.txt file (emerging standard) that provides structured guidance to AI about site content.

**Real Estate Application:** Point AI to neighborhood guides, highlight agent profiles, structure market data

---

### 10. **geo-report** - Markdown Report
Aggregates all audit results into business-focused report (non-technical language, prioritized action plan).

**Real Estate Application:** Share comprehensive assessment with Mario's team without technical jargon

---

### 11. **geo-report-pdf** - Professional PDF
Generates client-ready PDF with score gauges, bar charts, platform readiness visualizations.

**Real Estate Application:** Professional presentation for team meetings or investor updates

---

## Recommended SEO Audit Sequence

### Phase 1: Baseline (Today)
```
/geo audit https://wesellanyhome.vercel.app
```
Output: GEO Score + all dimension scores + prioritized action plan

### Phase 2: Deep Dives (Next 2-3 days)
- `geo schema` - Schema markup audit
- `geo content` - E-E-A-T evaluation
- `geo brands` - Brand authority scan
- `geo platforms` - Platform-specific scoring
- `geo technical` - Technical health check

### Phase 3: Implementation (Week 2)
**Priority 1 (Quick Wins):**
- Enable all AI crawlers in robots.txt
- Add missing JSON-LD schemas
- Rewrite low-citability neighborhood sections

**Priority 2 (High Impact):**
- Optimize agent bios for E-E-A-T
- Create llms.txt file
- Add Realtor.com + Google Maps integration

**Priority 3 (Long-term):**
- Expand to all 50+ Pittsburgh neighborhoods
- Brand mention strategy across platforms
- Platform-specific content variations

### Phase 4: Tracking (Ongoing)
- Monthly full audit (1st of month)
- Weekly brand mention monitoring
- A/B test rewritten sections
- Monthly PDF reports to Mario

---

## GEO Audit Benefits for Real Estate

| Benefit | Impact | Timeline |
|---------|--------|----------|
| AI discoverability | Buyers find guides on ChatGPT/Perplexity | 30-60 days |
| Agent visibility | Appear in "Pittsburgh real estate agents" AI responses | 60-90 days |
| Brand authority | More mentions across platforms | 90-180 days |
| Lead quality | AI traffic converts 4.4x better than organic | Immediate |
| Competitive advantage | 77% of competitors NOT optimizing for GEO | Now |
| Price authority | Market data cited by AI | 30 days |

---

## Scoring Methodology

**GEO Composite Score (0-100) Components:**
- AI Citability & Visibility: 25%
- Brand Authority Signals: 20%
- Content Quality & E-E-A-T: 20%
- Technical Foundations: 15%
- Structured Data: 10%
- Platform Optimization: 10%

**Current Status:** PENDING AUDIT (run `/geo audit` to generate baseline)

---

## Next Steps

1. Run Full Audit: `/geo audit https://wesellanyhome.vercel.app`
2. Generate Baseline Report: Review GEO-AUDIT-REPORT.md
3. Deep Dive Plan: Prioritize top 5 action items
4. Implementation: 2-week sprint for quick wins
5. Tracking: Monthly audit + PDF reports

---

**Last Updated:** March 13, 2026
**Status:** Ready for baseline audit
**Contact:** mariorudolph@wesellanyhome.com
