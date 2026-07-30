# iOS自动化内容站 — 90天逐日执行计划

> 项目名称：ShortcutsJournal
> 项目路径：`/Volumes/work/ios-automation-content/`
> 站点路径：`/Volumes/work/ios-automation-content/site/`
> 变现目标：Google AdSense + Amazon Affiliate
> 起始日期：2026年7月28日

---

## Phase 0：基建期（Day 1-3）
### 完成后状态：域名已注册、站点框架上线、基础SEO配置完成

**Day 1（7月28日 周一）— 域名注册 + 托管配置**
- [ ] 查询域名可用性（首选 `shortcutsjournal.com`，备选 `iosshortcutshub.com`、`shortcutsguide.com`）
- [ ] 在 Cloudflare Registrar 注册域名（$10.44/年，含免费WHOIS隐私+SSL）
- [ ] 如果域名不可用，在 Spaceship 或 Porkbun 注册
- [ ] 在 Cloudflare 注册账号，添加域名到 Cloudflare
- [ ] 配置 DNS 记录（A记录指向 Cloudflare Pages 或 Vercel）
- [ ] 记录所有账号密码到安全位置

**Day 2（7月29日 周二）— 站点技术搭建**
- [ ] 确定技术方案：纯静态HTML（已有首页）或 Hugo/Next.js
  - 建议：先用纯HTML，内容到30篇再迁移Hugo（避免过早折腾框架）
- [ ] 在 Cloudflare Pages 创建项目，连接 Git 仓库或直接上传
- [ ] 配置构建设置（如用Hugo则配build command）
- [ ] 验证 HTTPS 证书生效
- [ ] 配置 Cloudflare 缓存规则（静态资源长缓存）
- [ ] 测试站点的移动端响应式效果
- [ ] 配置 Cloudflare Email Routing（免费邮箱转发 hello@shortcutsjournal.com）

**Day 3（7月30日 周三）— SEO 基础配置 + 数据追踪**
- [ ] 注册 Google Search Console，验证域名所有权（DNS验证）
- [ ] 注册 Google Analytics 4，安装追踪代码
- [ ] 注册 Bing Webmaster Tools，验证域名
- [ ] 生成并提交 sitemap.xml（手动或脚本生成）
- [ ] 配置 robots.txt（允许所有抓取，指向sitemap）
- [ ] 在首页添加 Analytics 代码
- [ ] 在 Search Console 提交首页URL请求索引

---

## Phase 1：骨架期（Day 4-10）
### 目标：8个支柱分类页 + 3篇入门指南 = 11篇核心页面
### 这些页面是整个站点的SEO地基，必须优先完成

**Day 4（7月31日 周四）— 关键词研究 + 内容日历**
- [ ] 用 Ahrefs Free Keyword Generator（https://ahrefs.com/free-seo-tools/keyword-generator）研究以下seed keywords：
  - "iOS shortcuts"
  - "iPhone shortcuts"
  - "Apple Shortcuts"
  - "iOS automation"
  - "Shortcuts app"
- [ ] 用 Google Keyword Planner 补充搜索量数据（需登录Google Ads账号，不用投广告）
- [ ] 用 Google Trends 对比趋势：确认 "shortcuts" 相关词的搜索趋势方向
- [ ] 整理出 100+ 个长尾关键词，按 KD（难度）排序
- [ ] 将关键词分配到8个分类中，每个分类10-15个关键词
- [ ] 输出：`/Volumes/work/ios-automation-content/keyword-research.md`

**Day 5（8月1日 周五）— 4个分类支柱页（上）**
- [ ] 写 Productivity 分类页 `/shortcuts/productivity/index.html`
  - 含：分类介绍、子分类、Top 10 shortcuts列表、相关指南链接
  - 目标词：iOS shortcuts for productivity
- [ ] 写 Social Media 分类页 `/shortcuts/social-media/index.html`
  - 含：Instagram保存、视频下载、批量操作、内容管理
  - 目标词：iOS shortcuts for social media
- [ ] 写 Photo & Video 分类页 `/shortcuts/photo-video/index.html`
  - 含：格式转换、批量处理、水印、GIF制作
  - 目标词：iPhone shortcuts for photos
- [ ] 写 Communication 分类页 `/shortcuts/communication/index.html`
  - 含：自动回复、翻译、定时发送、通话管理
  - 目标词：iOS shortcuts for communication
- [ ] 每篇 ~1500-2000字，配内部链接
- [ ] 提交4个URL到 Search Console

**Day 6（8月2日 周六）— 4个分类支柱页（下）**
- [ ] 写 Home Automation 分类页 `/shortcuts/home-automation/index.html`
  - 含：Smart Home、地理围栏、场景联动
  - 目标词：iOS shortcuts home automation
- [ ] 写 Health & Fitness 分类页 `/shortcuts/health-fitness/index.html`
  - 含：喝水提醒、睡眠追踪、运动记录
  - 目标词：iPhone shortcuts health fitness
- [ ] 写 Travel & Maps 分类页 `/shortcuts/travel-maps/index.html`
  - 含：航班追踪、汇率换算、导航、停车
  - 目标词：iOS shortcuts for travel
- [ ] 写 Finance 分类页 `/shortcuts/finance/index.html`
  - 含：记账、账单提醒、汇率换算、投资
  - 目标词：iOS shortcuts for finance
- [ ] 提交4个URL到 Search Console

**Day 7（8月3日 周日）— 3篇入门指南**
- [ ] 写 "Getting Started with iOS Shortcuts: Complete Beginner Guide" `/guides/getting-started/index.html`
  - ~2500字，配截图：什么是Shortcuts、安装方法、第一个Shortcut
  - 目标词：how to use iOS shortcuts, getting started with shortcuts app
- [ ] 写 "How to Create Your First iOS Shortcut" `/guides/create-first-shortcut/index.html`
  - ~2000字，图文Step-by-step：创建→添加动作→测试→保存→运行
  - 目标词：how to create a shortcut on iPhone
- [ ] 写 "iOS Automations Explained: Time, Location & Event Triggers" `/guides/automations-explained/index.html`
  - ~2000字：Shortcuts vs Automations区别、触发类型详解、实际案例
  - 目标词：iOS automations, iPhone automation triggers
- [ ] 提交3个URL到 Search Console
- [ ] 更新首页的指南链接指向新页面

**Day 8（8月4日 周一）— 内链建设 + 首页优化**
- [ ] 审查所有11个页面，确保：
  - 每个分类页链接到相关指南（至少2个）
  - 每个指南链接到相关分类（至少2个）
  - 所有页面有面包屑导航
  - 所有页面有侧边栏"Related Shortcuts"
- [ ] 更新首页，将分类卡片和指南链接改为指向真实页面
- [ ] 检查所有内部链接无404
- [ ] 确保8个分类 + 3个指南 = 11个页面全部可通过首页2次点击到达

**Day 9（8月5日 周二）— 3篇具体Shortcuts教程（首批）**
- [ ] 从370+中文快捷指令中挑选3个最实用的，翻译+改写为英文教程：
- [ ] 写 "Ultimate Morning Routine Shortcut" `/shortcuts/productivity/morning-routine/index.html`
  - 模板：What it does → Who it's for → Prerequisites → Install link → Step-by-step → Customize → Troubleshoot → Related
  - 目标词：morning routine shortcut iPhone
- [ ] 写 "Auto Text Reply While Driving" `/shortcuts/communication/auto-reply-driving/index.html`
  - 目标词：auto reply text driving iPhone shortcut
- [ ] 写 "Batch Convert HEIC to JPG" `/shortcuts/photo-video/heic-to-jpg/index.html`
  - 目标词：convert HEIC to JPG iPhone shortcut
- [ ] 每篇 ~1200-1500字，含iCloud下载链接占位符

**Day 10（8月6日 周三）— 首批博客文章 + 社交账号**
- [ ] 写博客 "Best iOS Shortcuts for 2026: 20 Must-Have Automations" `/blog/best-ios-shortcuts-2026/index.html`
  - ~3000字，年度合集文，链接到已写教程
  - 目标词：best iOS shortcuts 2026, best iPhone shortcuts
- [ ] 注册 Twitter/X 账号 @ShortcutsJournal
- [ ] 注册 Pinterest 账号，创建 Board：iOS Shortcuts, Productivity, iPhone Tips
- [ ] 发第一条推文：介绍网站上线 + 链接到 Getting Started 指南
- [ ] 在 Pinterest 发布5-10个Pin（Shortcuts截图+教程链接）
- [ ] 提交所有新URL到 Search Console

---

## Phase 2：内容扩展期（Day 11-30）
### 目标：从11篇扩展到40篇，平均每天1.5篇
### 策略：每天2篇Shortcuts教程 + 每5天1篇深度指南/博客

**Day 11（8月7日 周四）— Shortcuts教程 x2**
- [ ] "Save Instagram Photos Without Screenshot" `/shortcuts/social-media/save-instagram/index.html`
  - 高搜索量关键词：save instagram photos iPhone
- [ ] "Focus Timer & Pomodoro Shortcut" `/shortcuts/productivity/pomodoro-timer/index.html`

**Day 12（8月8日 周五）— Shortcuts教程 x2**
- [ ] "Daily Expense Tracker" `/shortcuts/finance/expense-tracker/index.html`
- [ ] "Water Drinking Reminder" `/shortcuts/health-fitness/water-reminder/index.html`

**Day 13（8月9日 周六）— Shortcuts教程 x2**
- [ ] "I'm Home Geofence Automation" `/shortcuts/home-automation/arrive-home/index.html`
- [ ] "YouTube Video Downloader Shortcut" `/shortcuts/social-media/download-youtube/index.html`

**Day 14（8月10日 周日）— Shortcuts教程 x2**
- [ ] "Smart Photo Organizer by Location" `/shortcuts/photo-video/organize-photos/index.html`
- [ ] "Quick Currency Converter" `/shortcuts/travel-maps/currency-converter/index.html`

**Day 15（8月11日 周一）— 深度指南 + 周回顾**
- [ ] 写指南 "Apple Intelligence + Shortcuts: What's New in iOS 26" `/guides/apple-intelligence-shortcuts/index.html`
  - 时效性内容，抢占iOS 26新功能搜索流量
  - 目标词：Apple Intelligence shortcuts, iOS 26 new shortcuts features
- [ ] 周回顾：检查 Search Console 的索引状态和初始数据
- [ ] 更新内链：新文章互相链接，链接到支柱页
- [ ] 检查 Analytics 数据（如已有流量）

**Day 16（8月12日 周二）— Shortcuts教程 x2**
- [ ] "Create Custom Ringtones from Any Song" `/shortcuts/productivity/custom-ringtone/index.html`
- [ ] "Translate Text on the Fly" `/shortcuts/communication/translate-shortcut/index.html`

**Day 17（8月13日 周三）— Shortcuts教程 x2**
- [ ] "Track Screen Time & App Usage Report" `/shortcuts/health-fitness/screen-time-report/index.html`
- [ ] "Bulk Rename Photos" `/shortcuts/photo-video/bulk-rename/index.html`

**Day 18（8月14日 周四）— Shortcuts教程 x2**
- [ ] "Schedule Text Messages" `/shortcuts/communication/schedule-text/index.html`
- [ ] "WiFi Auto-Connect at Specific Locations" `/shortcuts/home-automation/wifi-automation/index.html`

**Day 19（8月15日 周五）— Shortcuts教程 x2**
- [ ] "Save Tweets / X Posts as Bookmarks" `/shortcuts/social-media/save-tweets/index.html`
- [ ] "Sleep Tracking with Health App" `/shortcuts/health-fitness/sleep-tracker/index.html`

**Day 20（8月16日 周六）— 深度博客 + 社交推广**
- [ ] 写博客 "Shortcuts vs IFTTT vs Tasker: Which Automation Tool Is Best?" `/blog/shortcuts-vs-ifttt/index.html`
  - 对比评测类文章，长尾词：shortcuts vs ifttt
- [ ] 在 Reddit r/shortcuts 发一个有用的帖子（介绍一个免费shortcut + 链接教程）
  - 注意：不要spam，提供真实价值
- [ ] 在 Pinterest 再发布5个Pin
- [ ] 更新所有新URL到 sitemap

**Day 21-25（8月17日-21日）— 每天Shortcuts教程 x2（共10篇）**
- [ ] Day21: "Clipboard History Manager" + "Find My iPhone Quick Actions"
- [ ] Day22: "Auto-Add Calendar Events from Email" + "QR Code Generator & Scanner"
- [ ] Day23: "Battery Health Monitor" + "Download TikTok Videos Without Watermark"
- [ ] Day24: "Create GIF from Live Photos" + "Voice Memo Transcription"
- [ ] Day25: "Parking Location Saver" + "Multi-Step Workout Logger"

**Day 26（8月22日 周五）— 深度指南 + 周回顾**
- [ ] 写指南 "Best iOS Shortcuts for Students: 15 Automations for School" `/guides/shortcuts-for-students/index.html`
  - 人群细分内容，精确长尾：iOS shortcuts for students
- [ ] 审查所有已发布页面，修复404链接
- [ ] 检查 Search Console 中的 coverage report，解决索引问题

**Day 27-30（8月23日-26日）— 每天Shortcuts教程 x2（共6篇）**
- [ ] Day27: "Auto-Reply to Specific Contacts" + "Music Discovery Assistant"
- [ ] Day28: "Screenshot to PDF Converter" + "Flight Status Tracker"
- [ ] Day29: "Daily Gratitude Journal" + "Contact Group Manager"
- [ ] Day30: "Tip Calculator with Split Bill" + "Reading List Manager"

> **Phase 2 结束状态**：约40篇文章（11支柱+3指南+1博客+25教程）
> 预期 Google 索引：20-30页
> 预期自然搜索流量：50-200 visits/day（开始有少量流量进来）

---

## Phase 3：深化期（Day 31-45）
### 目标：从40篇扩展到65篇 + 开始内容优化
### 策略：每天2篇教程 + 每7天1篇深度内容

**Day 31（8月27日 周三）— 数据驱动内容调整**
- [ ] 分析 Search Console 数据：
  - 哪些页面已开始获得展示/点击？
  - 哪些关键词有展示但排名低（需要优化）？
  - 发现新的关键词机会？
- [ ] 根据数据调整后续内容优先级
- [ ] 对表现最好的3个页面进行优化（添加FAQ schema、改善标题）

**Day 32-38（8月28日-9月3日）— 每天Shortcuts教程 x2（共14篇）**
- [ ] Day32: "Dark Mode Toggle Shortcut" + "Automatically Silence Phone at Work"
- [ ] Day33: "Recipe Ingredient to Grocery List" + "Watermark Photos in Bulk"
- [ ] Day34: "Speed Dial Widget" + "Custom Safari Start Page"
- [ ] Day35: "Backup Contacts to iCloud" + "Bitcoin Price Checker"
- [ ] Day36: "Save WhatsApp Status Photos" + "Step Counter Daily Goals"
- [ ] Day37: "Voice Controlled Smart Home" + "Markdown Note Creator"
- [ ] Day38: "Battery Saver Mode Automation" + "Email Unsubscriber"

**Day 39（9月4日 周五）— 深度指南 + 外链建设开始**
- [ ] 写指南 "Best iOS Shortcuts for Remote Workers: Work From Home Automations" `/guides/shortcuts-remote-workers/index.html`
- [ ] 开始外链建设：
  - 在 Hacker News 提交一篇深度指南（标题要吸引技术用户）
  - 在 Product Hunt 提交网站（如果够成熟）
  - 在相关科技博客评论区留有价值评论（不要spam）
- [ ] 更新 sitemap

**Day 40-45（9月5日-10日）— 每天Shortcuts教程 x2（共12篇）**
- [ ] Day40: "Automatic Do Not Disturb Schedule" + "Share WiFi Password via QR"
- [ ] Day41: "Log Work Hours with Timesheet" + "Instagram Story Downloader"
- [ ] Day42: "Create Calendar Event from Clipboard" + "AirPods Pro Battery Checker"
- [ ] Day43: "Weather-Based Clothing Suggester" + "Stock Price Quick Check"
- [ ] Day44: "Save TikTok Audio as Ringtone" + "Meal Prep Planner"
- [ ] Day45: "Duplicate Contact Cleaner" + "Custom Notification Sounds"

> **Phase 3 结束状态**：约65篇文章
> 预期 Google 索引：40-50页
> 预期日流量：200-500 visits/day

---

## Phase 4：加速期（Day 46-60）
### 目标：从65篇扩展到95篇 + 准备AdSense申请
### 策略：每天2-3篇 + 质量监控

**Day 46-60（9月11日-25日）— 每天内容产出**
- [ ] 每天发布 2-3 篇 Shortcuts 教程（共30-35篇）
- [ ] 每7天发布 1 篇深度博客/指南（共2篇）
- [ ] 建议博客选题：
  - "How iOS Shortcuts Work with Apple Watch: Complete Guide"
  - "Best Shortcuts for Content Creators and YouTubers"
- [ ] 每3天检查一次 Search Console 数据
- [ ] 每5天更新一次 sitemap
- [ ] 每7天在 Pinterest 发布一批新 Pin
- [ ] 每7天在 Reddit 发布1个有价值帖子
- [ ] 开始寻找 guest post 机会（小型科技博客）

**每周固定任务**（Phase 4每周重复）：
- 周一：检查上周 Analytics + Search Console 数据
- 周三：修复SEO问题（404、索引错误、标题优化）
- 周五：社交推广 + 新Pin发布
- 周日：下周内容计划 + 关键词补充研究

> **Phase 4 结束状态**：约95篇文章
> 预期日流量：500-1000 visits/day
> 可以开始准备 AdSense 申请

---

## Phase 5：变现准备期（Day 61-75）
### 目标：达到AdSense申请标准 + 优化变现页面
### 策略：补高质量内容 + 申请AdSense

**Day 61-65（9月26日-30日）— AdSense准备**
- [ ] 确保所有页面包含：
  - Privacy Policy 页面
  - About Us 页面
  - Contact 页面
  - Terms of Service 页面
  - DMCA / Copyright 页面
- [ ] 确保内容质量：
  - 检查所有文章无拼写/语法错误
  - 确保每篇有原创内容（不是简单翻译）
  - 确保有 E-E-A-T 信号（Experience, Expertise, Authoritativeness, Trustworthiness）
- [ ] 添加作者信息页面（About → 作者简介）
- [ ] 确保100+篇已发布

**Day 66（10月1日 周三）— 申请 Google AdSense**
- [ ] 提交 AdSense 申请
- [ ] 等待审核（通常1-4周）
- [ ] 如果被拒，根据拒绝原因修改后重新申请

**Day 67-75（10月2日-10日）— 持续内容产出**
- [ ] 每天继续发布 1-2 篇教程（AdSense审核期间不能停更）
- [ ] 重点写高搜索量的教程（参考 Search Console 数据）
- [ ] 优化已有高流量页面的变现布局
- [ ] 注册 Amazon Associates 账号（作为备用变现）
- [ ] 在含产品推荐的教程中添加 Amazon affiliate 链接

> **Phase 5 结束状态**：约110篇文章
> 预期日流量：800-1500 visits/day
> AdSense 状态：审核中/已批准

---

## Phase 6：增长期（Day 76-90）
### 目标：巩固流量 + 优化收入 + 建立内容飞轮
### 策略：数据驱动 + 内容更新 + 多渠道引流

**Day 76-90（10月11日-25日）— 每日节奏**

**每天必做（15分钟）**：
- [ ] 检查 Analytics 昨日数据
- [ ] 检查 Search Console 新出现的查询词
- [ ] 在社交媒体分享1条内容

**每周任务**：
| 星期 | 任务 | 时间 |
|------|------|------|
| 周一 | 数据复盘 + 内容策略调整 | 30min |
| 周二-周四 | 写3-4篇教程 | 各1-2h |
| 周五 | 深度指南/博客 + 社交推广 | 2h |
| 周六 | 内容优化（更新旧文章、修复SEO问题） | 1h |
| 周日 | 下周计划 + 关键词研究 | 30min |

**外链建设**（Phase 6）：
- [ ] 每周联系1-2个科技博客，提出 guest post
- [ ] 在 r/shortcuts、r/iphone、r/ios 持续参与讨论
- [ ] 在 Quora 回答 iOS shortcuts 相关问题，链接到文章
- [ ] 在 YouTube 评论中分享相关教程（自然不spam）

**内容更新策略**：
- [ ] 每2周回顾Top 10流量页面，更新过时信息
- [ ] 为高流量页面添加 FAQ section（提升搜索展示面积）
- [ ] 为高流量页面添加 Related Shortcuts 模块（增加页面浏览量）

> **Day 90 状态**：约150篇文章
> 预期日流量：1500-3000 visits/day
> 预期月AdSense收入：$50-150

---

## 每日时间分配模板（内容产出日）

假设每天投入 **2小时**：

| 时间 | 任务 | 预估时长 |
|------|------|---------|
| 开始 | 检查 Analytics/Search Console | 10min |
| 核心工作 | 写 2 篇 Shortcuts 教程 | 80min |
| SEO | 内链、meta优化、提交Search Console | 15min |
| 社交 | 分享到 Twitter/Pinterest | 10min |
| 收尾 | 更新内容日历、记录进度 | 5min |

---

## 内容质量标准（每篇必须满足）

1. 字数：教程 1200-1500字，指南 2000-3000字，博客 2500-4000字
2. 标题格式：`[Action] iOS Shortcut: [What It Does] (Step-by-Step Guide)`
3. 必须包含：meta description、H1-H3层级、内部链接≥3条
4. 必须包含：iCloud Shortcuts 下载链接（或占位符）
5. 必须包含：Related Shortcuts 推荐模块
6. AI内容必须经过 humanizer 处理，确保自然可读
7. 截图/GIF：初期用文字描述代替，后续逐步补充真实截图

---

## 关键里程碑

| 里程碑 | 预计日期 | 标准 |
|--------|---------|------|
| 域名上线 | Day 3 | HTTPS生效，首页可访问 |
| 11篇骨架完成 | Day 10 | 8分类+3指南 |
| 40篇文章 | Day 30 | 开始有自然搜索流量 |
| 65篇文章 | Day 45 | 首批关键词进入Top 30 |
| 95篇文章 | Day 60 | 准备AdSense申请 |
| AdSense申请 | Day 66 | 100+篇高质量内容 |
| 150篇文章 | Day 90 | 月收入目标 $100+ |

---

## 风险应对

| 如果... | 那么... |
|---------|---------|
| AdSense被拒 | 补充Privacy/About/Terms页面，提高内容质量，30天后重申 |
| 流量增长慢 | 加大Pinterest/Reddit推广，写更多时效性内容（iOS新功能） |
| 写不出内容 | 回到370+中文快捷指令翻译改编，或搜索Reddit热点话题 |
| 没时间写 | 用AI生成初稿→humanize去AI味→手动审核发布，效率可提升3x |
| iCloud链接失效 | 定期（每2周）检查下载链接有效性 |
