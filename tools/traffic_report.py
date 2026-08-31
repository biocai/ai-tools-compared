#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ai-tools-compared.com 流量日报 — 数据源：Vercel Web Analytics API"""
import json, urllib.request, urllib.parse, os, sys
from datetime import date, timedelta

SITE = '/Volumes/work/AI工具测评'
PID = 'prj_Km5jWVjJlvAFqHnBqkDimZrW81Vs'
SLUG = 'biocai'

def get_token():
    # 优先环境变量，其次 vercel CLI 会话文件
    if os.environ.get('VERCEL_TOKEN'):
        return os.environ['VERCEL_TOKEN']
    p = os.path.expanduser('~/Library/Application Support/com.vercel.cli/auth.json')
    if not os.path.exists(p):
        raise SystemExit('未找到 Vercel 登录凭证(CLI 曾因凭证失效删除 auth.json)。请在终端跑一次 vercel login 重新登录, 之后的日报会自动恢复。')
    d = json.load(open(p))
    # vca_ token 是短期访问令牌(约1个月过期)，过期后需 CLI 用 refreshToken 刷新。
    # 检查 expiresAt，临近/已过期就跑一次 `vercel whoami` 触发 CLI 自动刷新再读。
    import subprocess, time
    exp = d.get('expiresAt')
    if not exp or exp - time.time() < 3600:
        try:
            subprocess.run(['vercel', 'whoami'], capture_output=True, timeout=30)
            d = json.load(open(p))  # 重新读刷新后的token
        except Exception:
            pass
    # 2026-08-30 实测: refresh token 也可能彻底失效, 此时 CLI 会直接删掉 auth.json,
    # 上面的 json.load 抛异常被吞掉后 d 还是旧 token → 打出看不懂的 403 invalidToken。
    # 改为明确报错并给出修复动作。
    exp = d.get('expiresAt')
    if not exp or exp - time.time() < 3600:
        raise SystemExit('Vercel 登录凭证已彻底失效(自动刷新失败)。请在终端跑一次 vercel login 重新登录, 之后的日报会自动恢复。')
    return d['token']

TOKEN = get_token()

def q(dataset, style, params):
    params = {'slug': SLUG, 'projectId': PID, **params}
    url = f'https://api.vercel.com/v1/query/web-analytics/{dataset}/{style}?' + urllib.parse.urlencode(params, doseq=True)
    req = urllib.request.Request(url, headers={'Authorization': f'Bearer {TOKEN}'})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        return {'_error': e.code, '_msg': e.read().decode()[:200]}

def fmt_aggregate(rows, key, metrics=('visitors', 'pageviews')):
    out = []
    for r in rows[:8]:
        k = r.get(key) or r.get('timestamp', '')[:10]
        vals = ' / '.join(f"{r.get(m, 0)}{m}" for m in metrics)
        out.append(f'{k}: {vals}')
    return out

today = date.today()
d7 = (today - timedelta(days=7)).isoformat()
d1 = (today - timedelta(days=1)).isoformat()

lines = []
lines.append(f'=== ai-tools-compared.com 流量日报 {today.isoformat()} ===')

lifetime = q('visits', 'count', {})
if '_error' in lifetime:
    lines.append(f"[查询失败 code={lifetime['_error']}] {lifetime.get('_msg','')}")
    if lifetime['_error'] == 400:
        lines.append('(提示: Web Analytics 可能尚未在 Dashboard 启用)')
    print('\n'.join(lines)); sys.exit(1)

pv, v = lifetime['data']['pageviews'], lifetime['data']['visitors']
lines.append(f'[累计] pageviews={pv} visitors={v}')

# 近7天每日
daily = q('visits', 'aggregate', {'since': d7, 'until': today.isoformat(), 'by': 'day'})
if daily.get('data'):
    lines.append('[近7天逐日] (日期: visitors/pageviews)')
    lines += ['  ' + l for l in fmt_aggregate(daily['data'], 'timestamp')]

# 昨日 top 页面
top = q('visits', 'aggregate', {'since': d1, 'until': today.isoformat(), 'by': 'requestPath', 'limit': 8})
if top.get('data'):
    lines.append('[昨日Top页面]')
    lines += ['  ' + l for l in fmt_aggregate(top['data'], 'requestPath')]

# 近7天来源
ref = q('visits', 'aggregate', {'since': d7, 'until': today.isoformat(), 'by': 'referrerHostname', 'limit': 6})
if ref.get('data'):
    lines.append('[近7天来源域名]')
    lines += ['  ' + l for l in fmt_aggregate(ref['data'], 'referrerHostname', ('visitors',))]

# 近7天国家
geo = q('visits', 'aggregate', {'since': d7, 'until': today.isoformat(), 'by': 'country', 'limit': 6})
if geo.get('data'):
    lines.append('[近7天国家]')
    lines += ['  ' + l for l in fmt_aggregate(geo['data'], 'country', ('visitors',))]

report = '\n'.join(lines)
print(report)

os.makedirs(f'{SITE}/reports', exist_ok=True)
open(f'{SITE}/reports/traffic_{today.isoformat()}.md', 'w').write(report)
