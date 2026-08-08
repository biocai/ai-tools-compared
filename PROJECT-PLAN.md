# AI Tools Compared — 项目规划文档

> **定位**: AI工具领域的 Wirecutter — 深度横向对比，帮用户做出选型决策
> **域名**: https://ai-tools-compared.com
> **项目路径**: `/Volumes/work/AI工具测评/`
> **站点路径**: `/Volumes/work/AI工具测评/site/`
> **Git仓库**: https://github.com/biocai/ai-tools-compared
> **部署平台**: Vercel（project: shuai5）
> **开始日期**: 2026年7月28日
> **核心指标**: 12个月发布100篇对比文章，M14-16月达到 $2,000/月 AdSense 收入

---

## 一、项目现状

### 1.1 已完成基建

| 项目 | 状态 | 详情 |
|------|------|------|
| 域名注册 | ✅ | ai-tools-compared.com（Cloudflare Registrar，$9.77/年） |
| DNS配置 | ✅ | A记录 + CNAME指向Vercel，灰云模式 |
| SSL证书 | ✅ | Vercel自动签发，HTTPS正常 |
| Vercel部署 | ✅ | CLI已登录，project: shuai5，自动部署 |
| Git仓库 | ✅ | github.com/biocai/ai-tools-compared（public, main分支） |
| GA4统计 | ✅ | 已注入所有页面 |
| 首页 | ✅ | 深色科技风，8大分类，对比卡片（GPT-5.6 Sol / Claude Opus 5 / Gemini 3.6 Flash） |
| 法律页面 | ✅ | About / Privacy / Terms / Contact |
| SEO基础 | ✅ | robots.txt + sitemap.xml |
| 已有文章 | 1篇 | ChatGPT vs Claude vs Gemini 三方对比 |

### 1.2 待完成

| 项目 | 优先级 | 说明 |
|------|--------|------|
| Google Search Console | 🔴 高 | 待用户添加TXT验证记录完成域名验证 |
| AdSense申请 | 🔴 高 | 需GSC验证通过+一定流量+内容量后申请 |
| 文章模板标准化 | 🟡 中 | 需要一套可复用的对比文章HTML模板 |
| 内链体系 | 🟡 中 | 首页→文章→文章间的交叉链接 |
| 外链建设 | 🟢 低 | 内容到位后再做 |

---

## 二、内容策略

### 2.1 八大内容支柱

```
┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│  ① Chatbot  │ │  ② Image   │ │   ③ Video   │ │  ④ Writing  │
│  对话AI     │ │  AI绘画     │ │  AI视频     │ │  AI写作     │
├─────────────┤ ├─────────────┤ ├─────────────┤ ├─────────────┤
│  ⑤ Coding   │ │ ⑥ Product. │ │   ⑦ Audio   │ │  ⑧ Research │
│  AI编程     │ │  效率工具   │ │  AI音频     │ │  AI搜索研究 │
└─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘
```

### 2.2 关键词驱动选题优先级（2026年8月更新）

基于Google Trends、SERP竞争分析、CPC数据和搜索意图评估的选题排序。
**评分公式 = 搜索量(1-10) × CPC(1-10) × (10-竞争度) / 10**

#### Tier 1 — 高流量+高CPC+可竞争（优先写）
| 排名 | 关键词组 | 预估月搜索 | CPC | 竞争 | 推荐文章类型 |
|------|---------|-----------|-----|------|------------|
| 1 | best AI chatbot 2026 | 40K+ | $15-25 | 高 | 榜单文 Top 7 |
| 2 | ChatGPT vs Claude vs Gemini | 30K+ | $12-20 | 高 | 三方对比（已有，需更新） |
| 3 | best free AI tools | 80K+ | $8-15 | 高 | 榜单文 Top 15 |
| 4 | best AI video generator 2026 | 25K+ | $10-18 | 中 | 榜单文 Top 5 |
| 5 | AI voice generator / text to speech | 35K+ | $10-15 | 低 | 对比 ElevenLabs vs Play.ht vs Murf |
| 6 | AI music generator / Suno vs Udio | 20K+ | $8-12 | 低 | 双雄对决 |
| 7 | Midjourney vs Flux vs SD4 | 15K+ | $10-20 | 中 | 三方对比 |
| 8 | AI presentation maker / Gamma vs Tome | 15K+ | $8-15 | 低 | 对比+榜单 |
| 9 | Perplexity vs ChatGPT for search | 12K+ | $10-18 | 中 | 对比 |
| 10 | Cursor vs Windsurf vs Copilot | 10K+ | $15-25 | 中 | 三方对比（已有，需更新） |

#### Tier 2 — 高流量+中CPC（第二批）
| 排名 | 关键词组 | 预估月搜索 | CPC | 竞争 | 推荐文章类型 |
|------|---------|-----------|-----|------|------------|
| 11 | best AI image generator free | 50K+ | $5-10 | 高 | 榜单文 Top 6 |
| 12 | AI meeting assistant / Otter vs Fireflies | 10K+ | $8-12 | 低 | 已有，可更新 |
| 13 | AI resume builder 2026 | 25K+ | $5-10 | 高 | 榜单文 Top 8 |
| 14 | AI email writer / best AI email tool | 15K+ | $8-15 | 低 | 对比 |
| 15 | AI translation / DeepL vs Google Translate | 10K+ | $5-8 | 低 | 对比 |
| 16 | AI data analysis tool / spreadsheet AI | 8K+ | $10-15 | 低 | 对比 |
| 17 | AI photo editor / Photoroom vs Canva | 12K+ | $5-10 | 中 | 已有，可扩展 |
| 18 | AI SEO tool / Surfer vs Semrush | 8K+ | $20-30 | 高 | 已有，可更新 |
| 19 | AI customer support / Intercom vs Zendesk | 6K+ | $15-25 | 高 | 已有，可扩展 |
| 20 | AI note-taking / Notion vs Obsidian | 5K+ | $5-10 | 低 | 已有 |

#### Tier 3 — 长尾+低竞争（第三批，流量潜力大）
| 排名 | 关键词组 | 预估月搜索 | CPC | 竞争 | 推荐文章类型 |
|------|---------|-----------|-----|------|------------|
| 21 | best AI tool for students | 20K+ | $3-8 | 中 | 场景指南 |
| 22 | best AI for small business | 15K+ | $8-15 | 中 | 场景指南 |
| 23 | AI podcast tool / best AI for podcasters | 5K+ | $8-12 | 低 | 榜单文 |
| 24 | AI cover letter generator | 10K+ | $5-10 | 中 | 榜单文 |
| 25 | AI coding assistant free | 15K+ | $10-18 | 中 | 榜单文 |
| 26 | AI video editor / CapCut AI vs Premiere | 8K+ | $5-10 | 低 | 对比 |
| 27 | AI social media manager / AI content scheduler | 6K+ | $8-12 | 低 | 对比 |
| 28 | AI form builder / AI survey tool | 4K+ | $8-15 | 低 | 对比 |
| 29 | AI diagram tool / AI flowchart maker | 3K+ | $5-10 | 低 | 对比 |
| 30 | AI CRM / HubSpot AI vs Salesforce Einstein | 5K+ | $15-25 | 中 | 对比 |

**注意：** "best AI X"榜单文搜索量通常是"X vs Y"对比文的3-5倍，但CPC略低。建议每3篇文章中2篇对比+1篇榜单。

### 2.3 文章类型矩阵

| 类型 | 说明 | 示例 | 占比 |
|------|------|------|------|
| **三方对比** | 3个以上工具的横向评测 | "GPT-5.6 vs Claude Opus 5 vs Gemini 3.6 Flash" | 30% |
| **双雄对决** | 2个竞品的深度PK | "Midjourney v7 vs DALL-E 4: Which Creates Better Art?" | 40% |
| **同类横评** | 同品类TOP5/10榜单 | "Best AI Coding Assistants in 2026 (Top 7 Tested)" | 20% |
| **场景指南** | 基于使用场景的推荐 | "Best AI Tool for Academic Research: A PhD Student's Guide" | 10% |

### 2.3 2026年AI工具全景（对比素材库）

#### Chatbot / 通用AI
- **OpenAI ChatGPT**: GPT-5.6 Sol (flagship), GPT-5.5 (default free), GPT-5.6 Terra/Luna
- **Anthropic Claude**: Opus 5 (flagship, 7/24发布), Sonnet 5, Fable 5
- **Google Gemini**: 3.6 Flash (7/21发布), 3.5 Flash, 3.1 Pro
- **Meta**: Muse Spark 1.1 (7/9发布, 首次收费API)
- **xAI**: Grok 3/4
- **Mistral**: Large / Medium / Small
- **DeepSeek**: V3/R1

#### Image Generation
- **Midjourney**: v7 / v8.1 (最新版)
- **OpenAI**: GPT Image 2 (替代DALL-E，已deprecated)
- **Google**: Imagen 4
- **Stability AI**: Stable Diffusion 4 / SDXL Turbo
- **Adobe**: Firefly 4
- **Ideogram**: v3
- **Flux**: (Black Forest Labs)

#### Video Generation
- **Runway**: Gen-4 (最新旗舰)
- **Kling (快手)**: 可灵 2.0
- **Pika**: 最新版
- **Google**: Veo 3 / Veo 3.1
- **Luma Dream Machine**: 最新版
- **Adobe**: Premiere AI
- ~~OpenAI Sora~~: 已于2026年4月停运，勿再引用

#### AI Writing
- **Jasper**: 最新版
- **Copy.ai**: 最新版
- **Writesonic**: 最新版
- **Grammarly**: AI Writing
- **Notion AI**: 最新版
- **Lex**: 最新版

#### AI Coding
- **GitHub Copilot**: 最新版
- **Cursor**: 最新版
- **Windsurf** (Codeium): 最新版
- **Cline / Continue**: 开源方案
- **Replit**: AI Agent
- **Amazon Q**: Developer
- **Devin**: Cognition AI

#### Productivity
- **Notion AI** vs **Obsidian AI** vs **Logseq AI**
- **Microsoft Copilot** vs **Google Workspace AI**
- **Otter.ai** vs **Fireflies** vs **Fathom**
- **Zapier AI** vs **Make.com AI**

#### AI Audio
- **ElevenLabs**: 最新版
- **OpenAI TTS**: 最新版
- **Suno**: v5
- **Udio**: 最新版
- **Descript**: AI音频编辑

#### AI Research / Search
- **Perplexity AI**: 最新版
- **You.com**: 最新版
- **Google AI Overviews**: 最新版
- **Consensus**: 最新版
- **Elicit**: 最新版
- **Semantic Scholar**: AI增强

---

## 三、内容生产流水线

### 3.1 文章生产SOP

```
选题 → 调研 → 大纲 → 写作 → 配图 → 排版 → 审核 → 发布 → 推送
```

**Step 1 — 选题** (15min)
- 关键词研究（Ahrefs/Ubersuggest/Google Trends）
- 竞品分析（已有文章覆盖情况）
- 搜索量预估（CPC越高优先级越高）
- 记入选题池 Google Sheet

**Step 2 — 调研** (30-60min)
- 实际使用每个工具（注册、测试、记录）
- 收集官方文档、定价、功能对比
- 截图/录屏保存素材
- 查阅Reddit/论坛真实用户反馈

**Step 3 — 大纲** (15min)
- 固定结构（见3.2模板）
- 确定对比维度（至少5个维度）
- 标注每个章节需要的数据/截图

**Step 4 — 写作** (60-90min)
- 用Hermes辅助生成初稿
- 加入个人测试体验（差异化关键）
- 数据驱动（性能测试、定价对比）
- 英文撰写，目标1500-3000词

**Step 5 — 配图** (30min)
- 图片保存目录：`site/images/articles/{文章slug}/`
- HTML用相对路径引用：`/images/articles/{slug}/hero.png`
- 每篇文章3-5张图，类型：
  - Hero banner：对比主题banner（两个工具logo并排等）
  - 数据可视化：benchmark柱状图、pricing对比条形图（Python matplotlib生成）
  - 信息图：决策流程图、优劣势雷达图
  - 功能截图：工具界面实际截图或高质量mockup
  - 对比表格：做成可视化图表而非纯文字表格

**Step 6 — 排版** (15min)
- HTML模板填充
- 内链添加（关联文章）
- Schema标记（FAQ、Review、HowTo）
- 移动端适配检查

**Step 7 — 审核** (15min)
- 事实核查（定价、功能、版本号）
- 代码检查（HTML有效性）
- SEO检查（Title/Meta/H1/Alt）
- AI味检测（humanizer skill）

**Step 8 — 发布** (5min)
- Git commit + push → Vercel自动部署
- 更新sitemap.xml
- 更新首页（最新文章卡片）

### 3.2 文章标准结构

```html
Title: "[Tool A] vs [Tool B]: [Differentiator] in 2026"
  └─ Meta Description: 含主关键词+核心结论（150-160字符）

1. Quick Answer (TL;DR)
   └─ 150字以内，直接给结论

2. At a Glance (对比表)
   └─ 表格：价格/功能/性能/易用性/适用场景

3. [Tool A] Deep Dive
   ├─ Overview + 最新更新
   ├─ Key Features（配截图）
   ├─ Pricing（含免费额度）
   └─ Strengths & Weaknesses

4. [Tool B] Deep Dive
   └─ 同上结构

5. Head-to-Head Comparison
   ├─ 维度1：Output Quality（质量对比）
   ├─ 维度2：Speed & Performance（速度/性能）
   ├─ 维度3：Ease of Use（易用性）
   ├─ 维度4：Pricing & Value（性价比）
   ├─ 维度5：Ecosystem & Integration（生态）
   └─ 维度6：Privacy & Security（隐私安全）

6. Real-World Testing
   └─ 3个标准化测试场景的对比结果

7. The Verdict (最终推荐)
   ├─ Best for [场景A] → 推荐 Tool X
   ├─ Best for [场景B] → 推荐 Tool Y
   └─ Overall Winner → 推荐 Tool Z

8. FAQ
   └─ 3-5个People Also Ask问题
```

---

## 四、12个月发布计划

### 4.1 里程碑总览

```
M1-2  ████░░░░░░░░░░░░  基建完善 + 首批10篇
M3-4  ░░░░████░░░░░░░░  内容扩展 + 20篇（累计30篇）
M5-6  ░░░░░░░░████░░░░  批量生产 + 25篇（累计55篇）
M7-8  ░░░░░░░░░░░░████░  深度长文 + 20篇（累计75篇）
M9-10 ░░░░░░░░░░░░░░████ 补缺更新 + 15篇（累计90篇）
M11-12░░░░░░░░░░░░░░░░██ 更新维护 + 10篇（累计100篇）
```

### 4.2 第一季度详细计划（M1-M3，8月-10月）

#### 8月 — 基建冲刺 + 首批文章（10篇）

**第1周 (7/28-8/3): 基建收尾** ✅ 已完成
- [x] 重写首页（hero/stats/分类/featured/footer）
- [x] 创建统一CSS样式
- [x] 发布11篇文章（2篇新增：Notion/Obsidian/Logseq + Copilot/Gemini Workspace）

**第2周 (8/4-8/10): Audio专题（填补空白支柱）**
- [ ] ElevenLabs vs Play.ht vs Murf: AI Voice Generation Compared
- [ ] Suno vs Udio: AI Music Generation Showdown
- [ ] Best AI Tool for Podcasters (Top 5 Tested)

**第3周 (8/11-8/17): Research + 高流量榜单**
- [ ] Perplexity vs ChatGPT vs Gemini: AI Search Compared
- [ ] NotebookLM vs ChatGPT vs Claude for Research
- [ ] Best Free AI Tools 2026 (Top 15 Worth Using) — **高流量榜单文**

**第4周 (8/18-8/24): Image + Chatbot更新**
- [ ] Midjourney v7 vs Flux Pro vs SD4: AI Image Battle
- [ ] Best AI Chatbot 2026 (Top 7 Tested) — **高流量榜单文**
- [ ] ChatGPT vs Claude vs Gemini → 更新至最新模型（GPT-5.6/Claude Opus 5）

#### 9月 — Video + Writing + 电商（12篇）

**第1周: Video专题（3篇）**（Sora已停运，替换为活跃工具）
- [ ] Runway Gen-4 vs Kling 2.0 vs Luma: AI Video Generation Battle
- [ ] Pika vs Veo 3.1: Best AI Video for Social Media
- [ ] Best AI Video Generator 2026 (Top 5 Tested) — **高流量榜单文**

**第2周: Writing专题（3篇）**
- [ ] Jasper vs Copy.ai vs Writesonic: AI Content Writing Compared
- [ ] Grammarly AI vs ProWritingAid: Writing Assistant Compared
- [ ] Best AI Writing Tool for Bloggers (Top 6 Tested)

**第3周: Presentation + 电商（3篇）**
- [ ] Gamma vs Tome vs Beautiful.ai: AI Presentation Maker Compared
- [ ] Best AI Resume Builder 2026 (Top 8 Tested) — **高流量榜单文**
- [ ] DeepL vs Google Translate vs ChatGPT: AI Translation Compared

**第4周: 场景指南（3篇）**（首次引入场景指南类型）
- [ ] Best AI Tools for Students in 2026 (Top 10) — **场景指南**
- [ ] Best AI for Small Business (Top 8) — **场景指南**
- [ ] Best AI Email Writer 2026 (Top 6 Tested)

#### 10月 — 深度覆盖 + 更新（8篇）

**第1周: Coding + Data（3篇）**
- [ ] Windsurf vs Cursor vs Copilot Agent: AI Coding Triple Threat
- [ ] ChatGPT vs Claude for Coding: Developer's Choice 2026
- [ ] Best Free AI Coding Assistant (Top 5)

**第2周: SEO + CRM + 社媒（3篇）**
- [ ] Best AI SEO Tool 2026 (Top 6) — **更新已有Surfer文章**
- [ ] HubSpot AI vs Salesforce Einstein: AI CRM Compared
- [ ] Best AI Social Media Manager (Top 5 Tested)

**第3-4周: 旧文更新（2篇）**
- [ ] ChatGPT vs Claude vs Gemini → 更新最新模型
- [ ] Cursor vs GitHub Copilot → 更新最新版本

### 4.3 后续季度节奏

| 季度 | 目标篇数 | 累计 | 重点方向 |
|------|---------|------|---------|
| Q1 (8-10月) | 30篇 | 30 | 8大分类全覆盖，建立基础内容库 |
| Q2 (11-1月) | 25篇 | 55 | 深度长文、子话题扩展、竞品新版本对比 |
| Q3 (2-4月) | 25篇 | 80 | 场景指南、年度榜单、特定行业应用 |
| Q4 (5-7月) | 20篇 | 100 | 全面更新旧文、新模型对比、年度回顾 |

### 4.4 选题优先级规则（2026年8月修订）

1. **关键词数据驱动**：优先从 §2.2 关键词优先级表选题，不靠直觉
2. **文章类型均衡**：每3篇中2篇对比 + 1篇榜单/场景指南（当前100%对比→目标60%对比/30%榜单/10%场景指南）
3. **CPC > $10 的关键词优先**（Chatbot、Coding、Image生成、SEO）
4. **空白支柱优先填**：Audio（0篇）、Research（0篇）已列入8月计划
5. **新模型/新工具发布时抢首发**（7天内发文，SEO红利最大）
6. **"免费"关键词高搜索量**（best free AI X 搜索量是付费版的3-5倍），每批至少1篇免费向
7. **已有文章的"VS"变体**（A vs B 写完，再写 A vs C、B vs C）
8. **节日/季节性选题**（Q4 Black Friday deals、新年最佳AI工具）
9. **长尾场景指南**（Best AI tool for students/small business/podcasters）

---

## 五、SEO策略

### 5.1 页面SEO要素

每个文章页面必须包含：
- `<title>` — "[Tool A] vs [Tool B]: [Benefit] in 2026" (50-60字符)
- `<meta name="description">` — 含核心关键词+结论 (150-160字符)
- `<h1>` — 与title一致或略长
- `<h2>` — 每个对比维度
- 图片 `<alt>` — 描述性文字
- Schema标记：`FAQPage` + `Article` + `Review`
- 内链：至少3个指向站内其他文章
- 外链：1-2个指向权威来源（官方文档、研究论文）

### 5.2 技术SEO

- [x] robots.txt
- [x] sitemap.xml（需随文章发布自动更新）
- [ ] 每篇文章添加 canonical URL
- [ ] Open Graph / Twitter Card meta标签
- [ ] Core Web Vitals 优化（图片懒加载、字体预加载）
- [ ] HTTPS（已配置）
- [ ] 移动端响应式（需验证）

### 5.3 长期SEO打法

1. **话题集群（Topic Clusters）**: 每个支柱一个pillar文章 + 多个cluster文章
2. **定期更新**: 每季度更新一次旧文（SEO加分项）
3. **FAQ富摘要**: 每篇文章5个FAQ → 争取Google Featured Snippet
4. **数据驱动**: 发布原创测试数据 → 获取引用和外链
5. **User Signals**: 高质量内容 → 低跳出率 → 高停留时间 → 排名提升

---

## 六、变现策略

### 6.1 收入模型

```
                    AdSense（主）
                   /
流量 → 页面浏览 → → Affiliate（辅）
                   \
                    Sponsored（远期）
```

### 6.2 收入预测

| 阶段 | 时间 | 文章数 | 月UV | RPM预估 | 月收入 |
|------|------|--------|------|---------|--------|
| 冷启动 | M1-3 | 30 | 500 | $5 | $25 |
| 增长期 | M4-6 | 55 | 3,000 | $10 | $300 |
| 加速期 | M7-9 | 75 | 10,000 | $15 | $1,500 |
| 成熟期 | M10-12 | 100 | 20,000 | $20 | $4,000 |
| 稳定期 | M13+ | 100+ | 30,000 | $25 | $7,500 |

**关键假设**：
- AI工具类CPC $5-30，RPM $15-40（验证后可能更高）
- 前3个月主要靠长尾关键词自然流量
- 单篇爆文可贡献500-2000 UV/月

### 6.3 AdSense申请时间线

- **M2（9月）**: 申请AdSense（需GSC验证+15+篇内容+一定流量）
- **M3**: 通过审核，开始投放广告
- **M4+**: 优化广告位置，A/B测试

### 6.4 远期变现扩展

- **Affiliate Marketing**: 工具推荐链接（OpenAI API、Cursor Pro等）
- **Sponsored Content**: 品牌合作（M6+，月收入$500+后）
- **Newsletter**: AI工具周报，积累Email列表

---

## 七、技术架构

### 7.1 当前架构

```
Markdown/HTML ──→ Git Push ──→ Vercel Auto Deploy ──→ CDN
                                                     ↓
                                    ai-tools-compared.com
```

### 7.2 文件结构（目标状态）

```
/Volumes/work/AI工具测评/
├── PROJECT-PLAN.md              ← 本文档
├── CONTENT-CALENDAR.md          ← 内容日历（待创建）
├── TEMPLATE-ARTICLE.html        ← 文章模板（待创建）
├── site/
│   ├── index.html               ← 首页
│   ├── about.html
│   ├── privacy.html
│   ├── terms.html
│   ├── contact.html
│   ├── robots.txt
│   ├── sitemap.xml
│   ├── css/
│   │   └── style.css            ← 统一样式（从内联CSS抽离）
│   ├── images/
│   │   ├── logos/               ← 工具Logo
│   │   ├── screenshots/        ← 测试截图
│   │   └── og/                  ← Open Graph图片
│   └── articles/
│       ├── chatgpt-vs-claude-vs-gemini.html
│       ├── gpt56-vs-claude-opus5.html
│       ├── midjourney-vs-dalle4.html
│       ├── cursor-vs-copilot.html
│       └── ... (100篇目标)
├── research/                    ← 调研素材
│   ├── tool-database.json       ← 工具数据库
│   └── pricing-data/            ← 定价信息
└── drafts/                      ← 文章草稿
```

### 7.3 待办技术改进

- [ ] 创建 `site/css/style.css` 统一样式（当前是内联CSS）
- [ ] 创建文章HTML模板（一键生成新文章骨架）
- [ ] 创建 `site/images/` 目录结构
- [ ] sitemap.xml 自动生成脚本
- [ ] 首页文章列表动态更新（或半自动）

---

## 八、每周执行节奏

### 8.1 固定节奏

| 日期 | 任务 | 时间 |
|------|------|------|
| 周一 | 选题+调研 | 1-2h |
| 周二-周三 | 写作2篇文章 | 2-3h/篇 |
| 周四 | 配图+排版+审核+发布 | 1-2h |
| 周五 | 更新旧文1篇 + SEO检查 | 1h |
| 周末 | 可选：额外文章或下周准备 | — |

**目标产出**: 每周 2篇新文章 + 1篇旧文更新

### 8.2 月度检查清单

- [ ] 更新sitemap.xml
- [ ] 检查Google Search Console索引状态
- [ ] 查看GA4流量数据，分析热门文章
- [ ] 根据数据调整下月选题优先级
- [ ] 更新工具数据库（新版本/新定价）

---

## 九、关键风险与应对

| 风险 | 可能性 | 影响 | 应对策略 |
|------|--------|------|---------|
| AI工具更新频繁，文章快速过时 | 高 | 高 | 每月更新1-2篇旧文；标题加年份"2026" |
| Google SEO算法变化 | 中 | 中 | 关注核心：高质量内容+用户体验+EEAT |
| AdSense申请被拒 | 中 | 高 | 先积累内容（15+篇）和流量再申请；被拒后根据反馈修改 |
| 竞争对手增多 | 高 | 中 | 深度对比（非目录站）+原创测试数据 = 护城河 |
| 流量增长慢于预期 | 中 | 高 | 增加发布频率；尝试Reddit/社媒引流 |
| GFW屏蔽vercel.app子域名 | 已解决 | — | 已绑定自定义域名 |

---

## 十、成功指标

### 10.1 内容指标

- [ ] M3: 30篇文章上线
- [ ] M6: 55篇文章上线
- [ ] M12: 100篇文章上线
- [ ] 每篇文章平均 2,000+ 词
- [ ] 90%文章有FAQ Schema标记

### 10.2 流量指标

- [ ] M3: 500 UV/月
- [ ] M6: 3,000 UV/月
- [ ] M9: 10,000 UV/月
- [ ] M12: 20,000 UV/月

### 10.3 收入指标

- [ ] M3: AdSense通过审核
- [ ] M6: $300/月
- [ ] M9: $1,500/月
- [ ] M12: $4,000/月

---

## 十一、立即行动（本周）

1. **完成Search Console验证** — 用户去GSC添加域名，获取TXT记录添加到Cloudflare DNS
2. **创建文章HTML模板** — 可复用的对比文章骨架
3. **重写已有文章** — ChatGPT vs Claude vs Gemini → 更新为最新模型
4. **写第2篇新文章** — 从选题池中挑最高优先级的
5. **抽离CSS到独立文件** — 提升代码可维护性

---

*文档创建时间: 2026年7月30日*
*最后更新: 2026年7月30日*
