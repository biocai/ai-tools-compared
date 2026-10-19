# GSC 收录 & 索引请求跟踪表 (ai-tools-compared.com)

> 更新: 2026-10-06 | 数据源: GSC 本地Chrome CDP (profile持久登录)
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
| 2026-10-06 | **13(报告滞后) / 实查≥25** | ~64 | +2: best-ai-writing-tools-2026转正(顽固页仅剩best-ai-coding-assistant-free-2026,今日已重请求DONE) ; 新文coze-vs-botpress发布3天即收录(速度量级提升) ; 报告数字仍13滞后 ; **AdSense确认收款信息仍未填(首页警告条)** |

## 核心 URL 状态跟踪

| URL | 状态(09-23复查) | 请求索引 | 备注 |
|---|---|---|---|
| deepseek-vs-claude.html | **已收录**(10-04三连确认) | ✅ 09-18+09-23+09-30 | 顽固4周终破冰, 10-04三次独立运行均already-indexed |
| claude-vs-gemini.html | **已收录**(10-04确认) | ✅ 09-18+09-23+09-30 | 09-30重请求见效 |
| chatgpt-vs-claude-for-writing.html | **已收录**(10-04确认) | ✅ 09-18+09-23+09-30 | 09-30重请求见效 |
| best-ai-chatbots-2026.html | **已收录**(10-04确认) | ✅ 09-18+09-23+09-30 | **listicle首次破冰** |
| best-ai-writing-tools-2026.html | **已收录**(10-06确认) | ✅ 09-18+09-23+09-30+10-06 | 10-04时READY未发成,10-06一查已收录 |
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

### 10-06 周检详情（效果报告 + sitemap重提交 + 首次拿到Top网页表）
- **效果(近3月 vs 09-16基线)**: 曝光 1570→**1840 (+17%)** | 排名 67→**62.9 (升4位)** | 点击 1→1 | CTR 0.1%
- **Top网页(首次提取成功)**: 首页 527曝光 / midjourney-vs-dalle **494** / chatgpt-vs-claude-vs-gemini **239+全站唯一点击** / chatgpt-vs-jasper-vs-copyai 223 / suno-vs-udio 157 / cursor-vs-github-copilot 128 / photoroom 42+22 / claude-code-vs-cursor 19；另有 www. 前缀重复URL曝光(photoroom 42/midjourney 20/首页1) → canonical生效中
- **Top查询(147词)**: 品牌词 ai tool comparison 系列成主力(60/59/25/21/19/15) | midjourney vs dalle 43 | suno vs udio 系 31 | **chatgpt vs copy.ai 排名7.4(最靠前) / copy.ai vs chatgpt 排名15.5** — copyai 对比文有冲首页潜力
- **sitemap**: 线上 106 URL vs GSC 10-01 仅读 97 → **已重提交成功**(提交日期更新为10-06)。⚠️ sc-domain属性下必须填完整URL `https://ai-tools-compared.com/sitemap.xml`，相对路径报「站点地图地址无效」
- **未索引原因分布(13/76口径)**: 已发现未抓取 **60**(09-16为35, 新内容发布快于抓取) / 已抓取未索引 8 / 自动重定向 6 / 备用网页(规范) 2
- **新坑解决**: GSC网页tab合成点击全部失效的根因=Chrome窗口被遮挡时CDP输入被丢弃 → **必须先 `Page.bringToFront`** 再 `Input.dispatchMouseEvent`(坑13根因,已验证国家/网页tab均可切)

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

## 2026-10-16 VPN恢复补跑 + 10-13批中期验证（3天）

**欠账清零**: script-writing / cursor-vs-replit / ideogram-vs-flux 三条10-13 QUOTA欠账全部 DONE（今晨配额重置后）。CDP无tab坑18复现，/json/new恢复

**10-13批12条验证（发布+请求后3天，规律窗口4-7天）**:
- **已收录 5条(42%)**: aragon-vs-headshotpro-vs-photoai / best-ai-agents-ecommerce / best-ai-website-builders / deepseek-vs-grok / surfer-vs-neuronwriter
- 仍未收录 7条，今日已重请求: best-ai-agents-self-publishing / coding-tools-chrome-extensions / photo-animation / image-to-video / seedance-vs-veo / chatgpt-vs-sudowrite / coding-assistant(第6轮)
- 累计收录估 30+（10-06基线25 + 本批5）
- fail:fill 间歇出现（本轮4条），同URL重跑即好——疑似GSC面板加载竞态，无需修脚本

## 2026-10-13 周检（119篇时代，14新文全未收录→已请求）

**GSC概览(滞后口径)**: 11已编入/107未编入（此数字滞后≥11天，10-06时13/76实查25+，仅作趋势记录）
**效果报告(近3月)**: 点击1（chatgpt-vs-claude-vs-gemini 唯一点击，256展示） | 网页维度前10行合计1951+展示（对比10-08全站1860 → 创新高）
**Top网页**: 首页566 / midjourney-vs-dalle 504+20(www) / chatgpt-vs-claude-vs-gemini 256(唯一点击) / chatgpt-vs-jasper-vs-copyai 223 / suno-vs-udio 158 / cursor-vs-github-copilot 139 / photoroom 42(www)+23 / claude-code-vs-cursor 20 — 与10-06排名基本一致，10-08改title的两篇曝光未见跳变（正常，title生效需重新抓取）
**sitemap**: 线上120 URL vs GSC发现118，滞后2条，10-06刚重提交过，本次不重复提交

**收录实查（14新文+顽固页）**:
| URL | 状态 | 请求 |
|---|---|---|
| aragon-vs-headshotpro-vs-photoai | 未收录 | ✅ 10-13 DONE |
| best-ai-agents-ecommerce-2026 | 未收录 | ✅ 10-13 DONE |
| best-ai-agents-self-publishing-2026 | 未收录 | ✅ 10-13 DONE |
| best-ai-coding-tools-chrome-extensions-2026 | 未收录 | ✅ 10-13 DONE(首轮fail:fill重跑成功) |
| best-ai-photo-animation-tools-2026 | 未收录 | ✅ 10-13 DONE |
| best-ai-script-writing-2026 | 未收录 | ⏳ QUOTA，15:00后补 |
| best-ai-website-builders-2026 | 未收录 | ✅ 10-13 DONE |
| best-image-to-video-ai-2026 | 未收录 | ✅ 10-13 DONE |
| chatgpt-vs-sudowrite | 未收录 | ✅ 10-13 DONE |
| cursor-vs-replit | 未收录 | ⏳ 配额STOP，15:00后补 |
| deepseek-vs-grok | 未收录 | ✅ 10-13 DONE |
| ideogram-vs-flux | 未收录 | ⏳ 配额STOP，15:00后补 |
| seedance-vs-veo | 未收录 | ✅ 10-13 DONE |
| surfer-vs-neuronwriter | 未收录 | ✅ 10-13 DONE |
| best-ai-coding-assistant-free-2026 | 未收录 | ✅ 10-13 第5轮重请求 |

**规律修正**: "新文3天免请求收录"不成立——本批10-06后新文（最老5-7天）实查全部READY未收录，且8条为best-of listicle（历来收录慢）。对比文（aragon/chatgpt-vs-sudowrite/deepseek-vs-grok/seedance/surfer/cursor-vs-replit）也未自动收录 → 新文仍需主动请求
**配额**: 今日12条DONE后触顶（QUOTA弹窗确认），15:00太平洋零点重置。剩余队列: script-writing / cursor-vs-replit / ideogram-vs-flux

## 2026-10-08 — 工程优化日（AdSense拒审后首轮冲刺）

**GSC 3个月数据**: 1点击 / 1860曝光 / CTR 0.1% / 平均排名 #62.8

**排名最好页面（CTR优化目标，已完成title/desc重写并部署）**:
| 页面 | 曝光 | 排名 | 动作 |
|---|---|---|---|
| photoroom-vs-flair-vs-pebblely | 65 (www+非www) | #6.4/#17.9 | title加品牌词（原title无任何品牌名！） |
| claude-code-vs-cursor | 19 | #31.6 | "30-Day Test, One Clear Winner" |
| suno-vs-udio | 157 | #35.5 | "50-Track Test Shows a Clear Winner" |
| cursor-vs-github-copilot | 132 | #41.8 | "200-Hour Test, Clear Winner" |

**外链合规**: 12个官方站外链补 rel="noopener nofollow"（3文件），全站裸外链清零，已上线。

**内容审计**: 109篇全站扫描 — 最薄2320词/中位3498词，0薄内容，0模板化结构。内容质量非拒因，印证"低价值内容=热度不足"判断。

**www重复收录**: www 301→非www已生效，GSC双版本数据为历史残留，等Google合并信号即可。

**下一步**: 外链建设引流（backlink skill）→ UV≥10/日稳定后重交AdSense。

## 2026-10-19 周一补检（VPN恢复，用户手连）
- 发布cron停3天根因: glm-5.3周配额429(10-17 00:00起5连挂)，09:34重置后手动触发，127篇10:22上线复活
- 批跑9条全DONE(配额9/12): 10-13批7条老账重请求第7轮(self-publishing/chrome-extensions/photo-animation/image-to-video/sudowrite/seedance/coding-assistant) + 新文2篇(web-scrapers#125/antigravity-vs-cursor#126)
- ⚠️ 7条老账今晨实查全READY未收录 — 10-16重请求后3天转化0/7，历史规律窗口4-7天，验收期10-20~10-23，coding-assistant已第7轮顽固
- photo-animation首轮fail:fill重跑即DONE(第3次验证此坑无需修)
- 效果报告: 总曝光2160(10-13时1951,+209) 总点击仍1 平均排名63.1
- 发现: perplexity-vs-chatgpt-vs-gemini-search流量登顶(连续2日5UV)但不在GSC曝光Top表 → 流量来自AI助手引荐非Google搜索，GEO路线起效
- AdSense: 维持"需要注意(低价值内容)" ads.txt在线(未找到=假警报) — 策略不变，UV稳定10-20+/日再重交
- git push欠账d2055ff已清，origin/main同步
