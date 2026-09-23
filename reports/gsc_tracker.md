# GSC 收录 & 索引请求跟踪表 (ai-tools-compared.com)

> 更新: 2026-09-23 | 数据源: GSC 本地Chrome CDP (profile持久登录)
> 基线(09-16周检): 已收录 10 / 未收录 65 (35 已发现未抓取 + 已抓取未索引若干) | 近3月 1570曝光 / 1点击 / 平均排名67

## 站点级状态
| 日期 | 已收录 | 未收录 | 备注 |
|---|---|---|---|
| 2026-09-16 | 10 | 65 | sitemap已重提交 |
| 2026-09-18 | 10 | 65 | 概览页编制索引图表未变(收录更新有滞后) |
| 2026-09-22 | - | - | 周检cron跑了但结果丢失(投递失败+未写表) |
| 2026-09-23 | - | - | 11条核心URL全量复查: 0条被SKIP → 全部仍未收录 |

## 核心 URL 状态跟踪

| URL | 状态(09-23复查) | 请求索引 | 备注 |
|---|---|---|---|
| deepseek-vs-claude.html | 未收录 | ✅ 09-18 + 09-23 重请求 | 新旗舰文 |
| claude-vs-gemini.html | 未收录 | ✅ 09-18 + 09-23 重请求 | |
| chatgpt-vs-claude-for-writing.html | 未收录 | ✅ 09-18 + 09-23 重请求 | |
| best-ai-chatbots-2026.html | 未收录 | ✅ 09-18 + 09-23 重请求 | |
| best-ai-writing-tools-2026.html | 未收录 | ✅ 09-18 + 09-23 重请求 | |
| kling-vs-hailuo-vs-vidu.html | 未收录 | ✅ 09-18 + 09-23 重请求 | |
| claude-code-vs-cursor.html | 未收录(已抓取过) | ✅ 09-21 + 09-23 重请求 | 09-18 10:57 被Googlebot抓取 |
| best-ai-coding-assistant-free-2026.html | 未收录 | ✅ 09-21 + 09-23 重请求 | |
| grok-vs-chatgpt.html | 未收录 | ✅ 09-21 + 09-23 重请求 | |
| deepseek-vs-chatgpt.html | 未收录 | ✅ 09-21 + 09-23 重请求 | |
| chatgpt-vs-claude-vs-gemini.html | 未收录(有曝光) | ✅ 09-21 + 09-23 重请求 | 有曝光但面板仍示未收录 |
| cursor-vs-github-copilot.html | 已收录(有曝光117) | 跳过 | |

## 配额与节奏
- GSC"请求编入索引"配额: 实测≈6条/天(09-18: 6条成功+第7条被拒; 09-21: 5条全成功未触顶)
- **09-23 新发现: 11条连发(含同URL重请求)未触发配额拦截 → 重请求不计配额或上限更高**
- 配额重置: 太平洋时间零点 = 北京时间 15:00
- 当前队列: 已清空。11条核心URL已于09-23全量重请求，观察3-12天后09-30周检复盘

## 工具链
- 驱动脚本: /Users/mxh/.hermes/scripts/gsc_request_indexing.py (v2, 日志落盘 reports/gsc_index_requests.log)
- 依赖: 本地Chrome CDP :9222 (启动: gsc_cdp 同款命令, profile=~/.hermes-gsc-profile) + ZoogVPN 连通Google
