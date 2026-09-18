# GSC 收录 & 索引请求跟踪表 (ai-tools-compared.com)

> 更新: 2026-09-18 | 数据源: GSC 本地Chrome CDP (profile持久登录)
> 基线(09-16周检): 已收录 10 / 未收录 65 (35 已发现未抓取 + 已抓取未索引若干) | 近3月 1570曝光 / 1点击 / 平均排名67

## 站点级状态
| 日期 | 已收录 | 未收录 | 备注 |
|---|---|---|---|
| 2026-09-16 | 10 | 65 | sitemap已重提交 |
| 2026-09-18 | 10 | 65 | 概览页编制索引图表未变(收录更新有滞后) |

## 核心 URL 状态跟踪

| URL | 状态(09-18实测) | 请求索引(09-18) | 备注 |
|---|---|---|---|
| deepseek-vs-claude.html | 未收录 | ✅ 已请求(确认) | 新旗舰文 |
| claude-vs-gemini.html | 未收录 | ✅ 已请求(确认) | |
| chatgpt-vs-claude-for-writing.html | 未收录 | ✅ 已请求(确认DONE) | v2批跑10:57确认 |
| best-ai-chatbots-2026.html | 未收录 | ✅ 已请求(确认DONE) | |
| best-ai-writing-tools-2026.html | 未收录 | ✅ 已请求(确认DONE) | |
| kling-vs-hailuo-vs-vidu.html | 未收录 | ✅ 已请求(确认DONE) | |
| claude-code-vs-cursor.html | 已抓取-尚未编入索引 | ❌ 配额耗尽 | 09-18 10:57 被Googlebot抓取 |
| best-ai-coding-assistant-free-2026.html | 待查 | ❌ 排队中 | 明日优先 |
| grok-vs-chatgpt.html | 待查 | ❌ 排队中 | |
| deepseek-vs-chatgpt.html | 待查 | ❌ 排队中 | |
| chatgpt-vs-claude-vs-gemini.html | 待查(有曝光,大概率已收录) | ❌ 排队中 | |
| cursor-vs-github-copilot.html | 已收录(有曝光117) | 跳过 | |

## 配额与节奏
- GSC"请求编入索引"每日配额: 实测第7条触发配额弹窗，即≈6条/天(09-18: 6条确认成功+第7条被拒)
- 配额重置: 太平洋时间零点 = 北京时间 15:00
- 明日队列: claude-code-vs-cursor → best-ai-coding-assistant-free-2026 → grok-vs-chatgpt → deepseek-vs-chatgpt → chatgpt-vs-claude-vs-gemini (脚本自动跳过已收录页,不浪费配额)

## 工具链
- 驱动脚本: /Users/mxh/.hermes/scripts/gsc_request_indexing.py (v2, 日志落盘 reports/gsc_index_requests.log)
- 依赖: 本地Chrome CDP :9222 (启动: gsc_cdp 同款命令, profile=~/.hermes-gsc-profile) + ZoogVPN 连通Google
