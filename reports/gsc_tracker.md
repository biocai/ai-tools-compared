# GSC 收录 & 索引请求跟踪表 (ai-tools-compared.com)

> 更新: 2026-09-23 | 数据源: GSC 本地Chrome CDP (profile持久登录)
> 基线(09-16周检): 已收录 10 / 未收录 65 (35 已发现未抓取 + 已抓取未索引若干) | 近3月 1570曝光 / 1点击 / 平均排名67

## 站点级状态
| 日期 | 已收录 | 未收录 | 备注 |
|---|---|---|---|
| 2026-09-16 | 10 | 65 | sitemap已重提交 |
| 2026-09-18 | 10 | 65 | 概览页编制索引图表未变(收录更新有滞后) |
| 2026-09-22 | - | - | 周检cron跑了但结果丢失(投递失败+未写表) |
| 2026-09-23 | - | - | 11条核心URL全量复查: 0条被SKIP → 全部仍未收录(**误判,见09-25勘误**) |
| 2026-09-25 | **13** | 76 | +3收录! 09-21批次转化: chatgpt-vs-claude-vs-gemini / claude-code-vs-cursor / grok-vs-chatgpt (抓取均09-21) |
| 2026-09-30 | **13(报告滞后) / 实查≥17** | ~72 | 报告数字未刷新但实查+4收录(见下) ; VPN断5天后补跑周检 ; 8条顽固页全部重请求DONE |
| 2026-10-04 | **13(报告滞后) / 实查≥23** | ~66 | **顽固页大破冰**: 6条集体转正(deepseek-vs-claude三连确认+claude-vs-gemini/chatgpt-vs-claude-for-writing/best-ai-chatbots-2026/kling-vs-hailuo-vs-vidu/deepseek-vs-chatgpt) ; 09-30重请求批次见效 ; 仅剩2条顽固 |

## 核心 URL 状态跟踪

| URL | 状态(09-23复查) | 请求索引 | 备注 |
|---|---|---|---|
| deepseek-vs-claude.html | **已收录**(10-04三连确认) | ✅ 09-18+09-23+09-30 | 顽固4周终破冰, 10-04三次独立运行均already-indexed |
| claude-vs-gemini.html | **已收录**(10-04确认) | ✅ 09-18+09-23+09-30 | 09-30重请求见效 |
| chatgpt-vs-claude-for-writing.html | **已收录**(10-04确认) | ✅ 09-18+09-23+09-30 | 09-30重请求见效 |
| best-ai-chatbots-2026.html | **已收录**(10-04确认) | ✅ 09-18+09-23+09-30 | **listicle首次破冰** |
| best-ai-writing-tools-2026.html | 未收录 | ✅ 09-18+09-23+09-30+10-04(READY) | listicle, 顽固 |
| kling-vs-hailuo-vs-vidu.html | **已收录**(10-04确认) | ✅ 09-18+09-23+09-30 | 09-30重请求见效 |
| ~~claude-code-vs-cursor.html~~ | → 见下方"已收录"行 | | |
| best-ai-coding-assistant-free-2026.html | 未收录 | ✅ 09-21+09-23+09-30+10-04(DONE) | listicle, 顽固 |
| ~~grok-vs-chatgpt.html~~ | → 见下方"已收录"行 | | |
| deepseek-vs-chatgpt.html | **已收录**(10-04确认) | ✅ 09-21+09-23+09-30 | 09-30重请求见效 |
| chatgpt-vs-claude-vs-gemini.html | **已收录**(09-25确认) | ✅ 09-21 | 09-23误判: 旧SKIP关键词没跟上GSC新文案; **09-30首个搜索点击+227曝光** |
| cursor-vs-github-copilot.html | **已收录**(09-30实查确认) | 跳过 | 有曝光123 |
| claude-code-vs-cursor.html | **已收录**(09-25确认,抓取09-21) | - | 09-21批次转化 |
| grok-vs-chatgpt.html | **已收录**(09-25确认,抓取09-21) | - | 09-21批次转化 |
| midjourney-vs-dalle.html | **已收录**(09-30实查确认) | - | 曝光488, 全站第2 |
| chatgpt-vs-jasper-vs-copyai.html | **已收录**(09-30实查确认) | - | 曝光211 |
| suno-vs-udio.html | **已收录**(09-30实查确认) | - | 曝光144 |
| photoroom-vs-flair-vs-pebblely.html | **已收录**(09-30实查确认) | - | 曝光59 |

### 09-30 实查发现
- **报告滞后**: 编制索引报告仍显示13/76, 但实时检查5条高曝光页全部已收录 → 实际收录≥17, 报告数字滞后约1周
- **转化规律**: "X vs Y"工具对比文转化快(chatgpt-vs-claude-vs-gemini/midjourney-vs-dalle等), **best-of listicle和deepseek系8条反复请求均不转化** → 疑似内容类型被降权, 考虑给这些页加内链/外链
- **首个点击**: chatgpt-vs-claude-vs-gemini.html 拿到全站第一个Google搜索点击(近3月总曝光1790, 140个查询词, 平均排名63.6)

### 09-25 勘误与脚本修复
- **bug**: GSC新界面文案改为"网址已收录到 Google/网页已编入索引"，旧关键词"网址已位于 Google 上"匹配不到 → 已收录页面被误判为未收录并重复请求(浪费但无害,重请求不计配额)
- **修复**: status() 增加新关键词, 已验证: 已收录URL正确SKIP, 未收录URL正常DONE
- **结论**: 09-23"11条全部未收录"系误判, 实际当时至少3条已收录; 09-23的重请求多为冗余

## 配额与节奏
- GSC"请求编入索引"配额: 实测≈6条/天(09-18: 6条成功+第7条被拒; 09-21: 5条全成功未触顶)
- **09-23 新发现: 11条连发(含同URL重请求)未触发配额拦截 → 重请求不计配额或上限更高**
- 配额重置: 太平洋时间零点 = 北京时间 15:00
- 当前队列: 已清空。11条核心URL已于09-23全量重请求，观察3-12天后09-30周检复盘

## 工具链
- 驱动脚本: /Users/mxh/.hermes/scripts/gsc_request_indexing.py (v2, 日志落盘 reports/gsc_index_requests.log)
- 依赖: 本地Chrome CDP :9222 (启动: gsc_cdp 同款命令, profile=~/.hermes-gsc-profile) + ZoogVPN 连通Google
