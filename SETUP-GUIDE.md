# AI Tools Compared — 网站注册部署步骤

> 每一步都在你自己的 Chrome 浏览器中操作
> 按顺序执行，完成后打个勾

---

## Step 1: 注册域名（Cloudflare）

**为什么选 Cloudflare**：.com 域名最低价（约 $9.77/年），免费 WHOIS 隐私，DNS 直接配 Vercel。

1. [ ] 打开 https://dash.cloudflare.com/sign-up
2. [ ] 注册 Cloudflare 账号（邮箱+密码）
3. [ ] 登录后，左侧菜单 → **Domain Registration** → **Register Domains**
4. [ ] 搜索 `ai-tools-compared.com`，确认可用
5. [ ] 添加到购物车，结算（绑定信用卡/支付宝）
6. [ ] 注册完成后记录：
   - 域名：ai-tools-compared.com
   - 注册商：Cloudflare
   - 到期时间：2027年（1年）

**如果 Cloudflare 注册不了**（区域限制），备选方案：
- **Spaceship** (https://www.spaceship.com/) — $8.88/年 .com
- **Porkbun** (https://porkbun.com/) — $9.56/年 .com
- **Namecheap** (https://www.namecheap.com/) — $9.98/年 .com

---

## Step 2: 配置 Cloudflare DNS（指向 Vercel）

1. [ ] Cloudflare Dashboard → 左侧 **Websites** → **Add a site**
2. [ ] 输入 `ai-tools-compared.com`，选择 **Free** 计划
3. [ ] 添加以下 DNS 记录（这是 Vercel 要求的）：

| 类型 | 名称 | 内容 | 代理状态 |
|------|------|------|---------|
| A | @ | 76.76.21.21 | DNS only（灰色云朵） |
| CNAME | www | cname.vercel-dns.com | DNS only（灰色云朵） |

⚠️ **重要**：代理状态必须是 **DNS only（灰色云朵）**，不能开橙色云朵（Cloudflare 代理），否则 Vercel SSL 会冲突。

4. [ ] DNS 记录添加完成后等待生效（通常几分钟）

---

## Step 3: 部署到 Vercel

### 3.1 创建 GitHub 仓库

在终端执行（我已经帮你初始化了 Git）：

```bash
cd /Volumes/work/AI工具测评
# 添加站点文件
git add site/ PROJECT-PLAN.md
git commit -m "feat: initial site with ChatGPT vs Claude vs Gemini article"

# 创建远程仓库并推送
gh repo create ai-tools-compared --public --source=. --push
```

### 3.2 Vercel 部署

1. [ ] 打开 https://vercel.com/signup → 用 **GitHub 登录**
2. [ ] 登录后 → **Add New** → **Project**
3. [ ] 导入 GitHub 仓库 `biocai/ai-tools-compared`
4. [ ] 配置 Framework Preset: **Other**
5. [ ] Root Directory: `/`（根目录）
6. [ ] Build Command: 留空
7. [ ] Output Directory: `site`
8. [ ] 点击 **Deploy**
9. [ ] 等待部署完成，获得默认域名：`ai-tools-compared-xxx.vercel.app`
10. [ ] 访问确认首页正常显示

---

## Step 4: 绑定自定义域名

1. [ ] Vercel Dashboard → 进入项目 → **Settings** → **Domains**
2. [ ] 输入 `ai-tools-compared.com`，点击 Add
3. [ ] 再输入 `www.ai-tools-compared.com`，点击 Add
4. [ ] Vercel 会显示需要的 DNS 记录（应该和 Step 2 一样）
5. [ ] 如果 DNS 已经配好，Vercel 会自动验证
6. [ ] 等待 SSL 证书签发（1-5分钟）
7. [ ] 访问 https://ai-tools-compared.com 确认生效

---

## Step 5: Google Search Console

1. [ ] 打开 https://search.google.com/search-console
2. [ ] 点击 **添加资源** → 选择 **网域** → 输入 `ai-tools-compared.com`
3. [ ] 验证方式选 **DNS 记录验证**
4. [ ] Google 会给出一个 TXT 记录，类似：
   ```
   google-site-verification=xxxxxxxxxxxxxxxx
   ```
5. [ ] 回到 Cloudflare DNS，添加这条 TXT 记录：
   - 类型：TXT
   - 名称：@
   - 内容：`google-site-verification=xxxxxxxxxxxxxxxx`
6. [ ] 回到 Search Console 点击验证
7. [ ] 验证成功后，提交首页 URL：
   - 左侧 **网址检查** → 输入 `https://ai-tools-compared.com/` → 点击 **请求编入索引**

---

## Step 6: Google Analytics 4

1. [ ] 打开 https://analytics.google.com → 创建账号
2. [ ] 账号名称：AI Tools Compared
3. [ ] 媒体资源名称：ai-tools-compared.com
4. [ ] 时区：China (GMT+8)
5. [ ] 选择平台：网站
6. [ ] 输入网址：https://ai-tools-compared.com
7. [ ] 创建后获取 **Measurement ID**（格式：G-XXXXXXXXXX）
8. [ ] 把以下代码添加到所有 HTML 文件的 `<head>` 中（我来帮你加，告诉我 Measurement ID）：

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

---

## Step 7: Bing Webmaster Tools

1. [ ] 打开 https://www.bing.com/webmasters → 用 Microsoft/Google 账号登录
2. [ ] 添加站点 → 输入 `https://ai-tools-compared.com`
3. [ ] 验证方式选 DNS
4. [ ] Bing 会给出 TXT 记录，添加到 Cloudflare DNS
5. [ ] 验证通过

---

## Step 8: robots.txt + sitemap.xml

部署后需要创建这两个文件（我来生成，你确认 Vercel 部署成功后告诉我）：

- `/Volumes/work/AI工具测评/site/robots.txt`
- `/Volumes/work/AI工具测评/site/sitemap.xml`

---

## Step 9: 法律页面（AdSense 必需）

AdSense 申请必须有这4个页面，我来创建：

1. [ ] `/site/about.html` — About Us
2. [ ] `/site/privacy.html` — Privacy Policy
3. [ ] `/site/terms.html` — Terms of Service
4. [ ] `/site/contact.html` — Contact

---

## 执行顺序总结

```
Step 1 → Step 2 → Step 3.1(Git) → Step 3.2(Vercel) → Step 4(域名绑定)
→ Step 5(GSC) → Step 6(GA) → Step 7(Bing) → Step 8(robots+sitemap)
→ Step 9(法律页面)
```

**需要手动操作的部分**：Step 1-2, 3.2, 4, 5, 6, 7（浏览器注册+配置）
**我来帮你完成的部分**：Step 3.1(Git推送), 8(生成文件), 9(法律页面), 首页改版

---

*创建时间：2026年7月29日*
