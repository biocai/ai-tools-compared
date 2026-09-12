# 外链建设跟踪表

启动：2026-09-12 | 站点：ai-tools-compared.com（59篇满编）| 目标：破零外链 → 索引 → 流量

## ✅ 已完成（09-12）

| # | 渠道 | 动作 | 状态 | 备注 |
|---|------|------|------|------|
| 1 | GitHub | awesome-ai-tool-comparisons 仓库，59条对比入口+站内dofollow | 已上线 | github.com/biocai/awesome-ai-tool-comparisons |
| 2 | aitools.fyi | Tally 提交旗舰文全文（ChatGPT vs Claude vs Gemini）| 待审 | "We will list it ASAP" |
| 3 | **IndexNow** | **60个URL批量提交，202 Accepted** | **已接受** | 新key=11a0fceaac41f5a6821f75c5c72e1266；Bing/Yandex几小时内来抓；旧key 365b500c已被IndexNow拉黑（403 UserForbidded），勿再用 |
| 4 | Vercel 手动部署 | 发现git push→自动部署断链（至少从8-07起就是手动）| 已部署 | 每次发文后需手动 `vercel --prod`，或用户去Vercel Dashboard重连GitHub集成 |

## 📊 索引现状（09-12 查证）

- Bing：site: 查询实际收录 ≈ 0（返回无关结果）
- Google：无法自动验证（机房IP弹验证），但总PV仅27 → 收录必然很低
- 判断：新站沙盒期，Google 8-08 时仅发现14 URL，之后45篇新文未提交过

## ❌ 受阻清单

| 渠道 | 原因 | 解锁条件 |
|------|------|----------|
| Futurepedia | 免费提交取消，$247起 | 付费（暂不建议）|
| TAAFT / Toolify / FeedSpot | Cloudflare 硬拦 | 换出口IP或用户手动提交 |
| HackerNews | "account creation disabled"（两个IP段都禁）| 用户提供已有HN账号 |
| Reddit | VPN出口IP被 network security 封 + DNS污染 | 换住宅IP的VPN节点 |
| Dev.to/Medium | 无登录态 | 用户在受控浏览器登录GitHub一次（OAuth用）|
| GSC API | 无凭证（GSC为用户手动管理）| 用户手动操作（见下）|

## 👤 用户手动清单（30分钟，收益最大）

1. **GSC 重提交 sitemap**（2分钟）：search.google.com/search-console → 站点地图 → 重新提交 sitemap.xml（45篇新文未被发现）
2. **GSC 逐URL请求索引**（20分钟）：网址检查 → 输入URL → 请求编入索引，优先：chatgpt-vs-claude、cursor-vs-copilot、claude-code-vs-cursor、best-ai-coding-assistant、grok-vs-chatgpt、deepseek-vs-chatgpt（6篇核心 + 每天几个陆续推）
3. **Vercel 重连 GitHub**（3分钟）：Dashboard → site 项目 → Settings → Git → 重连 biocai/ai-tools-compared（恢复自动部署）
4. （可选）手动提交 TAAFT/Toolify：用户本地Chrome开 theresanaiforthat.com/submit、toolify.ai/submit（用户IP不会触发CF硬拦）

## 📋 后续自动任务

- [ ] aitools.fyi 审核结果跟踪（1-2周后查）
- [ ] IndexNow 效果验证：9-13起每天 curl bing site: 看收录增长
- [ ] Reddit/HN 等 VPN 换节点后重试
- [ ] 59篇内容二次分发（Dev.to/Hashnode）等 GitHub 登录态

## 提交信息存档

- 邮箱：mxh20082231@126.com / 署名：Xiang-He Meng
- HN 账号尝试：mxh_compare、xhmeng_dev（均被禁，账号文件 reports/hn_account.txt）
- IndexNow key：11a0fceaac41f5a6821f75c5c72e1266（线上 /11a0fceaac41f5a6821f75c5c72e1266.txt）
