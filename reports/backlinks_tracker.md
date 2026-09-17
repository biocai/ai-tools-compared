# 外链建设跟踪表

启动：2026-09-12 | 站点：ai-tools-compared.com（68篇）| 目标：破零外链 → 索引 → 流量

## ✅ 已完成（09-12）

| # | 渠道 | 动作 | 状态 | 备注 |
|---|------|------|------|------|
| 1 | GitHub | awesome-ai-tool-comparisons 仓库，59条对比入口+站内dofollow | 已上线 | github.com/biocai/awesome-ai-tool-comparisons |
| 2 | aitools.fyi | Tally 提交旗舰文全文（ChatGPT vs Claude vs Gemini）| ~~待审~~ **判死** | 博客停更（仅6篇且多为2023旧文），09-17查未上榜 |
| 3 | **IndexNow** | 60个URL批量提交 | 已接受 | 旧key已弃用；**现用key=329e929222c19fc8121b90e93aa7a9e0**（09-16轮换，09-16已全量重推69 URL，双端点202）|
| 4 | Vercel 手动部署 | git push→自动部署断链 | 已部署 | 每次发文后需手动 `vercel --prod`，或用户去Vercel Dashboard重连GitHub集成 |

## ✅ 已完成（09-17）

| # | 渠道 | 动作 | 状态 | 备注 |
|---|------|------|------|------|
| 5 | GitHub | awesome repo 59→68条（9篇新文：writing×3、LLM×3、video×1、character×1、UGC×1）| 已推送 | commit 6bc49ed；git clone超时，走 gh api contents PUT 直更 |
| 6 | GSC 基线 | 索引10/未37；sitemap重提交63→69；周检cron全自动（CDP）| 闭环 | 基线见 09-16 体检；下次周检 09-22 周二 10:00 |

## ⏳ 待办（09-17，被 VPN 阻塞）

- [ ] **GSC 逐URL请求索引**（核心6篇：chatgpt-vs-claude、cursor-vs-copilot、claude-code-vs-cursor、best-ai-coding-assistant、grok-vs-chatgpt、deepseek-vs-chatgpt）— 需 ZoogVPN 连通 + Chrome CDP；GSC 每日配额约10-12次，分批做
- [ ] VPN 断线时 Reddit/HN/GSC 全线不可做

## ❌ 受阻清单

| 渠道 | 原因 | 解锁条件 |
|------|------|----------|
| Futurepedia | 免费提交取消，$247起 | 付费（暂不建议）|
| TAAFT / Toolify / FeedSpot | Cloudflare 硬拦 | 换出口IP或用户手动提交 |
| HackerNews | "account creation disabled"（两个IP段都禁）| 用户提供已有HN账号 |
| Reddit | VPN出口IP被 network security 封 + DNS污染 | 换住宅IP的VPN节点 |
| Dev.to/Medium | 无登录态 | 用户在受控浏览器登录GitHub一次（OAuth用）|
| aitools.fyi | 博客停更，提交石沉大海 | 无（渠道死亡）|

## 📋 后续自动任务

- [ ] GSC 周检 cron 9c8a2425ef36（周二10:00）观察收录 10/68 增长
- [ ] Reddit/HN 等 VPN 换节点后重试
- [ ] 68篇内容二次分发（Dev.to/Hashnode）等 GitHub 登录态
- [ ] 下次部署时顺手删线上旧 IndexNow key 文件（11a0fce/365b500c）

## 提交信息存档

- 邮箱：mxh20082231@126.com / 署名：Xiang-He Meng
- HN 账号尝试：mxh_compare、xhmeng_dev（均被禁，账号文件 reports/hn_account.txt）
- IndexNow key：329e929222c19fc8121b90e93aa7a9e0（线上 /329e929222c19fc8121b90e93aa7a9e0.txt；旧 key 11a0fce、365b500c 已废弃勿用）
