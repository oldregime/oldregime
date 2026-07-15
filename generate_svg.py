#!/usr/bin/env python3
"""
Andrew6rant-exact neofetch SVG profile generator for Divyansh Joshi (oldregime).

Exact colors/font/style from Andrew6rant/Andrew6rant dark_mode.svg + light_mode.svg.
Runs locally and in GitHub Actions.
"""

from __future__ import annotations
import subprocess, json, sys
from pathlib import Path
from datetime import datetime, timezone

# ─── Andrew6rant's original ASCII portrait art (dark / light variants) ───────
ASCII_DARK = """\
           g@M%@%%@N%Nw,,
        ,M*|`||*%gNM=]mM%g||%N,
       p!``  '! |''` '''|||jhlj%w
     ,@L `    ,,        ''!`|j%M]%M
    ]j'` .,wp@pw,    `.     ''''|%Wg
  /{||]@@@@@@@@@pp.             |||||
 '` ']@@@@@@@@@@@@@@p     , ,'''` `
  , :]%%@@@@@%%%%%%k%h '*||mkr     *
  '  j%M`      |jkk'   ~nrn=|i    ;`
   !  jrr*^`             `"!  L'':!
    j  lp;,.  ,/ @@    ,;\\nmy "  ,~
   i r @@@@mmHM @@@@ `^****M*,p ;,
   | ]@@@@HHH]g@M%%%%%H,jmgpmb%  j
    ;;%%%%%k%@[,.n|;.;j%%k|%k%%',[
     H|%%k%%%j%k||,;;j;!!'|%ij}]@
     "djjmkL,"]][,,,,wwxw;|#kjk`
       %;%km%%%%M%M|%%jkkii|||[
        kjj%%kkkl|!||||||j|||"
         |jm%H@@@b%%kkmk%i|!,[
         @p|j%%%%jkk|||j*'`;j[
        ]@@@g|'''`'''  ` ,;j%k
        @@@@@mgmp;,,,,:;jj%%k%
       @@@@@@@@%%kgki!|jjjj%k%@ .
. ^['' %@@@@HH%b%k{illljkjj%%%% ; `,.
=[' ` . %HH%%%%%H@gkilljjj%kk%".   `'i"""

ASCII_LIGHT = """\
            ;;,, ,;,|g;~,,
         ,g@@@@@@l&$$$@|,w$$@gy,
        $@@@@@@@@@@$@@@@@@@@$$MW$k
       $$@@@@@@B@@@@@@@@@@@@@$@$$g,$
     g@llM**'''||%@@@@@$@@$@@@@@@@L$&
   @$&$F         ''T%M$@@@@@@@@@@@$@$@
  @@@@F              ']@@@@@@$$@$@@@@
  @@@$L               |$@@@$$l$@@@@$F
 ]@@@@L ,@@$@@@@L  ,l@$$$$$$$$$@@@@@
  %$@@@$}',,gg@||@@@@l@g@ggg|l$&$@@$
  ]@@@@@'"*TTTTT'F  ]Wl|||''"'$]@@@@
   $$@M$       ,#    ]gg,,,,,.r'$@$
    &$L        ' ,, ,,,'T''`    $$L
     lL         T"||||!   `-    l"'
     ' |        '||l||||"|L|  L `
      ''   '|L++=*****""*"||` L|
        |           ,,      |||F
        '         |||||||| ||l$
          !                |l&L
           '!,       |||,||@M|L
            ||l&$@$$@$$$@$MT|||
         |    |||lll$$llll|||||L
    ,;y@        ||||||l||@|||||l
,g$@$$$@         |||||||||||||||| $g,
$$$$$$$$@    |    |||||||||||||| |$$@g"""

# ─── GitHub helpers ──────────────────────────────────────────────────────────
def run(*cmd):
    try:
        return subprocess.check_output(list(cmd), stderr=subprocess.DEVNULL).decode().strip()
    except Exception:
        return ''

def fetch_stats():
    stats = {
        'login': 'oldregime', 'repos': '53', 'stars': '5',
        'commits': '636',     'followers': '2',
        'loc_net': '0',       'loc_add': '0', 'loc_del': '0',
        'age': '6 years, 3 months, 25 days',
    }
    try:
        u = json.loads(run('gh', 'api', 'user') or '{}')
        if u:
            login = stats['login'] = u.get('login', 'oldregime')
            stats['repos']     = str(u.get('public_repos', stats['repos']))
            stats['followers'] = str(u.get('followers',    stats['followers']))
            created = u.get('created_at', '')
            if created:
                joined = datetime.fromisoformat(created.replace('Z', '+00:00'))
                now    = datetime.now(timezone.utc)
                d      = now - joined
                y, m, dy = d.days // 365, (d.days % 365) // 30, (d.days % 365) % 30
                stats['age'] = f'{y} year{"s"*(y!=1)}, {m} month{"s"*(m!=1)}, {dy} day{"s"*(dy!=1)}'

        login = stats['login']
        s = run('gh', 'api', f'users/{login}/repos', '--paginate', '-q', '.[].stargazers_count')
        if s: stats['stars'] = str(sum(int(x) for x in s.split() if x.strip().isdigit()))

        gql = f'query{{user(login:"{login}"){{contributionsCollection{{contributionCalendar{{totalContributions}}}}}}}}'
        g   = run('gh', 'api', 'graphql', '-f', f'query={gql}')
        if g:
            stats['commits'] = str(
                json.loads(g)['data']['user']['contributionsCollection']['contributionCalendar']['totalContributions'])

        # LOC via contributor stats API (per-repo)
        add_t = del_t = 0
        repos = [r for r in run('gh','api',f'users/{login}/repos','--paginate','-q','.[].name').split('\n') if r.strip()]
        for repo in repos:
            raw = run('gh', 'api', f'repos/{login}/{repo}/stats/contributors')
            if raw and raw.startswith('['):
                try:
                    for c in json.loads(raw):
                        if c.get('author',{}).get('login','').lower() == login.lower():
                            for w in c.get('weeks', []):
                                add_t += w.get('a', 0); del_t += w.get('d', 0)
                except Exception:
                    pass
        if add_t:
            stats['loc_net'] = f'{add_t-del_t:,}'
            stats['loc_add'] = f'{add_t:,}'
            stats['loc_del'] = f'{del_t:,}'

    except Exception as e:
        print(f'Warning: {e}', file=sys.stderr)
    return stats

# ─── SVG helpers ─────────────────────────────────────────────────────────────
def esc(s): return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

def kv(key, value, pad=32):
    d = ' ' + '.' * max(pad - len(key) - 1, 1) + ' '
    return (f'<tspan class="cc">. </tspan>'
            f'<tspan class="key">{esc(key)}</tspan>'
            f':<tspan class="cc">{d}</tspan>'
            f'<tspan class="value">{esc(value)}</tspan>')

def kvd(k1, k2, value, pad=32):
    key = f'{k1}.{k2}'
    d   = ' ' + '.' * max(pad - len(key) - 1, 1) + ' '
    return (f'<tspan class="cc">. </tspan>'
            f'<tspan class="key">{esc(k1)}</tspan>'
            f'.<tspan class="key">{esc(k2)}</tspan>'
            f':<tspan class="cc">{d}</tspan>'
            f'<tspan class="value">{esc(value)}</tspan>')

def sec(title, width=60):
    dashes = '—' * max(width - len(title) - 4, 4)
    return f'- {esc(title)} -{dashes}-—-'

# ─── SVG maker ───────────────────────────────────────────────────────────────
def make_svg(is_dark, stats):
    if is_dark:
        BG, FG = '#161b22', '#c9d1d9'
        KEY, VAL, CC = '#ffa657', '#a5d6ff', '#616e7f'
        ADD, DEL = '#3fb950', '#f85149'
        ART = ASCII_DARK
    else:
        BG, FG = '#f6f8fa', '#24292f'
        KEY, VAL, CC = '#953800', '#0a3069', '#c2cfde'
        ADD, DEL = '#1a7f37', '#cf222e'
        ART = ASCII_LIGHT

    # Andrew6rant exact spec
    FONT  = 'ConsolasFallback,Consolas,monospace'
    FS    = 16          # font-size px
    LH    = 20          # line-height px (Andrew uses 20px gaps)
    AX    = 15          # ascii art x start
    AY0   = 30          # ascii art first baseline y
    IX    = 390         # info column x
    IY0   = 30          # info first baseline y
    PAD_B = 30          # bottom breathing room (px below last baseline — descenders need ~8px extra)

    # ── Info lines (curated, clean) ──────────────────────────────────────────
    ln = stats
    rows = [
        # Header — Andrew exact format (extended dashes for 1060px width)
        f'{esc(ln["login"])}@github -{"—" * 49}-—-',
        '',
        kv('OS',    'Fedora Linux 44, Windows 11, Android', 32),
        kv('Uptime', ln['age'], 32),
        kv('Host',  'VIT Bhopal University, India 🇮🇳', 32),
        kv('Role',  'CS Undergrad  ·  Software Engineer', 32),
        kv('IDE',   'VS Code, JetBrains, Neovim', 32),
        kv('Shell', 'zsh  ·  Kitty', 32),
        '',
        kvd('Languages', 'Programming', 'Python, C++, JavaScript, TypeScript', 32),
        kvd('Languages', 'AI_ML',       'LangChain, LangGraph, PyTorch, Groq',  32),
        kvd('Languages', 'Web',         'React, Node.js, Fastify, HTML/CSS',    32),
        kvd('Languages', 'Systems',     'Docker, Linux, Nginx, Git, Bash',       32),
        '',
        kvd('Hobbies', 'Software', 'AI Agents, Self-hosting, Automation',  32),
        kvd('Hobbies', 'Hardware', 'Homelab, Proxmox, TrueNAS, ZFS RAID', 32),
        '',
        sec('Contact', 60),
        '',
        kv('Email',   'divyanshjoshidev@gmail.com', 32),
        kv('Discord', 'theoldregime', 32),
        kv('LinkedIn','in/divyanshjoshidev', 32),
        '',
        sec('GitHub Stats', 60),
        '',
        # Repos + Stars + Followers — Andrew exact inline format
        (f'<tspan class="cc">. </tspan>'
         f'<tspan class="key">Repos</tspan>:'
         f'<tspan class="cc" id="repo_data_dots"> .... </tspan>'
         f'<tspan class="value" id="repo_data">{ln["repos"]}</tspan>'
         f' {{<tspan class="key">Stars</tspan>:'
         f'<tspan class="cc" id="star_data_dots"> ........... </tspan>'
         f'<tspan class="value" id="star_data">{ln["stars"]}</tspan>}}'
         f' | <tspan class="key">Followers</tspan>:'
         f'<tspan class="cc" id="follower_data_dots"> ....... </tspan>'
         f'<tspan class="value" id="follower_data">{ln["followers"]}</tspan>'),
        # Commits line
        (f'<tspan class="cc">. </tspan>'
         f'<tspan class="key">Commits</tspan>:'
         f'<tspan class="cc" id="commit_data_dots"> ................. </tspan>'
         f'<tspan class="value" id="commit_data">{ln["commits"]}</tspan>'),
        # Lines of Code — Andrew exact format with addColor / delColor
        (f'<tspan class="cc">. </tspan>'
         f'<tspan class="key">Lines of Code on GitHub</tspan>:'
         f'<tspan class="cc" id="loc_data_dots">. </tspan>'
         f'<tspan class="value" id="loc_data">{ln["loc_net"]}</tspan>'
         f' ( <tspan class="addColor" id="loc_add">{ln["loc_add"]}</tspan>'
         f'<tspan class="addColor">++</tspan>, '
         f'<tspan id="loc_del_dots"> </tspan>'
         f'<tspan class="delColor" id="loc_del">{ln["loc_del"]}</tspan>'
         f'<tspan class="delColor">--</tspan> )'),
    ]

    # ── Auto-size canvas height ───────────────────────────────────────────────
    art_lines  = ART.split('\n')
    art_height = AY0 + len(art_lines) * LH          # bottom of last art line
    inf_height = IY0 + (len(rows) - 1) * LH          # bottom of last info line (y baseline)
    H  = max(art_height, inf_height) + PAD_B          # canvas height

    # ── Build art tspans ─────────────────────────────────────────────────────
    art_svg = ''
    for i, line in enumerate(art_lines):
        art_svg += f'<tspan x="{AX}" y="{AY0 + i*LH}">{esc(line)}</tspan>\n'

    # ── Build info tspans ────────────────────────────────────────────────────
    info_svg = ''
    for i, row in enumerate(rows):
        y = IY0 + i * LH
        if row == '':
            info_svg += f'<tspan x="{IX}" y="{y}" class="cc">. </tspan>\n'
        else:
            info_svg += f'<tspan x="{IX}" y="{y}">{row}</tspan>\n'

    return f"""<?xml version='1.0' encoding='UTF-8'?>
<svg xmlns="http://www.w3.org/2000/svg" font-family="{FONT}" width="1060px" height="{H}px" font-size="{FS}px">
<style>
@font-face {{
src: local('Consolas'), local('Consolas Bold');
font-family: 'ConsolasFallback';
font-display: swap;
-webkit-size-adjust: 109%;
size-adjust: 109%;
}}
.key      {{fill: {KEY};}}
.value    {{fill: {VAL};}}
.addColor {{fill: {ADD};}}
.delColor {{fill: {DEL};}}
.cc       {{fill: {CC};}}
text, tspan {{white-space: pre;}}
</style>
<rect width="1060px" height="{H}px" fill="{BG}" rx="15"/>
<text x="{AX}" y="{AY0}" fill="{FG}">
{art_svg}
</text>
<text x="{IX}" y="{IY0}" fill="{FG}">
{info_svg}
</text>
</svg>
"""

# ─── Entry point ─────────────────────────────────────────────────────────────
if __name__ == '__main__':
    print('⚙  Fetching live GitHub stats...', flush=True)
    s = fetch_stats()
    print(f'   repos={s["repos"]}  stars={s["stars"]}  commits={s["commits"]}  '
          f'followers={s["followers"]}  LOC={s["loc_net"]}')
    BASE = Path(__file__).parent
    for mode, dark in (('dark', True), ('light', False)):
        p = BASE / f'{mode}_mode.svg'
        p.write_text(make_svg(dark, s), encoding='utf-8')
        print(f'✅ {mode}_mode.svg  ({p})')
