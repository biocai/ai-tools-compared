#!/usr/bin/env python3
"""IndexNow 批量推送 ai-tools-compared.com 全部 sitemap URL。
背景：09-13 前 key 文件线上 404，所有历史 ping 均失败，本次全量补推。
"""
import json, re, urllib.request, urllib.error

KEY = "a1b2c3d4e5f6478291a3b4c5d6e7f809"
HOST = "ai-tools-compared.com"

# 取线上 sitemap 全部 URL
req = urllib.request.Request(f"https://{HOST}/sitemap.xml", headers={"User-Agent": "Mozilla/5.0"})
xml = urllib.request.urlopen(req, timeout=15).read().decode()
urls = re.findall(r"<loc>(.*?)</loc>", xml)
print(f"sitemap URL 数: {len(urls)}")

body = json.dumps({"host": HOST, "key": KEY, "keyLocation": f"https://{HOST}/{KEY}.txt", "urlList": urls}).encode()

for endpoint in [f"https://api.indexnow.org/indexnow", f"https://www.bing.com/indexnow"]:
    r = urllib.request.Request(endpoint, data=body, method="POST",
                               headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(r, timeout=20) as resp:
            print(f"{endpoint} -> HTTP {resp.status}")
    except urllib.error.HTTPError as e:
        print(f"{endpoint} -> HTTP {e.code} {e.read().decode()[:120]}")
    except Exception as e:
        print(f"{endpoint} -> ERR {e}")
