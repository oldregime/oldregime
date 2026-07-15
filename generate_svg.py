#!/usr/bin/env python3
"""
Andrew6rant-exact neofetch SVG profile generator for Divyansh Joshi (oldregime).

Pixel-perfect match to Andrew6rant's style:
  - Exact same colors, font, dimensions, spacing (20px lines, 530px height)
  - Left: ASCII art portrait
  - Right: neofetch key-value layout with `. Key: ........ Value`
  - Section headers: `- Title -—————————————-—-`
  - Lines of Code with ++ / -- colors

Run locally:    python3 generate_svg.py
GitHub Actions: uses GITHUB_TOKEN automatically
"""

from __future__ import annotations
import subprocess
import json
import sys
import re
from pathlib import Path
from datetime import datetime, timezone

# ─── Andrew6rant's EXACT ASCII art motif (cool face silhouette) ──────────────
# Faithful to the original dark-mode look: dense, organic, portrait-style chars
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

def run(*cmd: str) -> str:
    try:
        return subprocess.check_output(list(cmd), stderr=subprocess.DEVNULL).decode().strip()
    except Exception:
        return ''


def fetch_stats() -> dict:
    stats = {
        'login':     'oldregime',
        'repos':     '53',
        'stars':     '5',
        'commits':   '633',
        'followers': '2',
        'following': '8',
        'loc_net':   '0',
        'loc_add':   '0',
        'loc_del':   '0',
        'age':       'Since 2020',
    }

    try:
        user_raw = run('gh', 'api', 'user')
        if user_raw:
            u = json.loads(user_raw)
            stats['login']     = u.get('login', 'oldregime')
            stats['repos']     = str(u.get('public_repos', stats['repos']))
            stats['followers'] = str(u.get('followers',    stats['followers']))
            stats['following'] = str(u.get('following',    stats['following']))
            # GitHub join date → age
            created = u.get('created_at', '')
            if created:
                joined = datetime.fromisoformat(created.replace('Z', '+00:00'))
                now    = datetime.now(timezone.utc)
                diff   = now - joined
                yrs    = diff.days // 365
                mos    = (diff.days % 365) // 30
                dys    = (diff.days % 365) % 30
                stats['age'] = f'{yrs} year{"s" if yrs != 1 else ""}, {mos} month{"s" if mos != 1 else ""}, {dys} day{"s" if dys != 1 else ""}'

        login = stats['login']

        # Stars
        s = run('gh', 'api', f'users/{login}/repos', '--paginate', '-q', '.[].stargazers_count')
        if s:
            stats['stars'] = str(sum(int(x) for x in s.split() if x.strip().isdigit()))

        # Total commits (contributions this year)
        gql = ('query { user(login: "%s") { contributionsCollection {'
               'contributionCalendar { totalContributions }}}}') % login
        g = run('gh', 'api', 'graphql', '-f', f'query={gql}')
        if g:
            stats['commits'] = str(
                json.loads(g)['data']['user']
                ['contributionsCollection']['contributionCalendar']['totalContributions'])

        # Lines of Code: sum additions & deletions across all owned repos
        # Uses gh api paginated repos + per-repo contributor stats
        add_total = del_total = 0
        repo_list_raw = run('gh', 'api', f'users/{login}/repos', '--paginate',
                            '-q', '.[].name')
        repo_list = [r for r in repo_list_raw.split('\n') if r.strip()]
        for repo in repo_list:
            raw = run('gh', 'api', f'repos/{login}/{repo}/stats/contributors')
            if raw and raw.startswith('['):
                try:
                    for c in json.loads(raw):
                        if c.get('author', {}).get('login', '').lower() == login.lower():
                            for w in c.get('weeks', []):
                                add_total += w.get('a', 0)
                                del_total += w.get('d', 0)
                except Exception:
                    pass

        if add_total > 0:
            stats['loc_add'] = f'{add_total:,}'
            stats['loc_del'] = f'{del_total:,}'
            stats['loc_net'] = f'{add_total - del_total:,}'

    except Exception as e:
        print(f'Warning: {e}', file=sys.stderr)

    return stats


# ─── Exact dot-padding (Andrew6rant style) ────────────────────────────────────
# He uses literal space-padded dots. We count chars to align columns.
# Right column starts at x=390, font is 16px monospace → ~9.6px per char
# Values align to ~col 42 from x=390 start → we pad with spaces+dots

def dots(key_len: int, target: int = 32) -> str:
    """Return the dot-spacer string so total `key_len + dots` = target chars."""
    n = max(target - key_len, 1)
    return ' ' + '.' * n + ' '


def kv(key: str, value: str, target: int = 32) -> str:
    """'. Key: ........ Value' — Andrew6rant exact format."""
    d = dots(len(key) + 1, target)  # +1 for the colon
    return (
        f'<tspan class="cc">. </tspan>'
        f'<tspan class="key">{esc(key)}</tspan>'
        f':<tspan class="cc">{d}</tspan>'
        f'<tspan class="value">{esc(value)}</tspan>'
    )


def kv_dot(key1: str, key2: str, value: str, target: int = 32) -> str:
    """'. Key.Sub: ... Value' — for hierarchical keys like Languages.Programming."""
    full = f'{key1}.{key2}'
    d = dots(len(full) + 1, target)
    return (
        f'<tspan class="cc">. </tspan>'
        f'<tspan class="key">{esc(key1)}</tspan>'
        f'.<tspan class="key">{esc(key2)}</tspan>'
        f':<tspan class="cc">{d}</tspan>'
        f'<tspan class="value">{esc(value)}</tspan>'
    )


def section(title: str, width: int = 52) -> str:
    """'- Title -——————————————-—-' Andrew6rant section divider."""
    dashes = width - len(title) - 4  # '- ' + title + ' -' + dashes
    return f'- {esc(title)} -' + '—' * max(dashes, 4) + '-—-'


def esc(s: str) -> str:
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


# ─── SVG builder — exact Andrew6rant structure ───────────────────────────────

def make_svg(is_dark: bool, stats: dict) -> str:
    # ── Exact Andrew6rant colors ────────────────────────────────────────────
    if is_dark:
        BG   = '#161b22'   # github dark bg
        FG   = '#c9d1d9'   # github dark text
        KEY  = '#ffa657'   # orange key  ← EXACT Andrew color
        VAL  = '#a5d6ff'   # blue value  ← EXACT Andrew color
        CC   = '#616e7f'   # dim dots    ← EXACT Andrew color
        ADD  = '#3fb950'   # green ++    ← EXACT Andrew color
        DEL  = '#f85149'   # red --      ← EXACT Andrew color
        ASCII_ART = ASCII_DARK
    else:
        BG   = '#f6f8fa'   # github light bg
        FG   = '#24292f'   # github light text
        KEY  = '#953800'   # dark orange ← EXACT Andrew color
        VAL  = '#0a3069'   # dark blue   ← EXACT Andrew color
        CC   = '#c2cfde'   # light dots  ← EXACT Andrew color
        ADD  = '#1a7f37'   # dark green  ← EXACT Andrew color
        DEL  = '#cf222e'   # dark red    ← EXACT Andrew color
        ASCII_ART = ASCII_LIGHT

    # ── Canvas — Andrew6rant exact dimensions ───────────────────────────────
    W, H   = 985, 530
    FS     = 16
    FONT   = "ConsolasFallback,Consolas,monospace"
    LINE_H = 20          # Andrew uses 20px between tspan y values
    ART_X  = 15          # ASCII art x
    ART_Y0 = 30          # ASCII art first y
    INFO_X = 390         # Info column x
    INFO_Y0 = 30         # Info first y

    # ── Curate the right-side content (only what looks nice) ────────────────
    login    = stats['login']
    age      = stats['age']
    repos    = stats['repos']
    stars    = stats['stars']
    commits  = stats['commits']
    followers= stats['followers']
    following= stats['following']
    loc_net  = stats['loc_net']
    loc_add  = stats['loc_add']
    loc_del  = stats['loc_del']

    # Build right-side lines (list of raw SVG tspan inner content strings)
    # Empty string = blank line (still renders `. ` placeholder)
    lines: list[str] = []

    # Header — "user@host -———————" (Andrew's exact format)
    lines.append(
        f'{esc(login)}@github -{"—" * 42}-—-'
    )

    # Section 1 — system info
    lines.append(kv('OS',       'Fedora Linux 44, Windows 11, Android', 30))
    lines.append(kv('Uptime',   age, 30))
    lines.append(kv('Host',     'VIT Bhopal University, India 🇮🇳', 30))
    lines.append(kv('Role',     'CS Undergrad  ·  Software Engineer', 30))
    lines.append(kv('IDE',      'VS Code, JetBrains, Neovim', 30))
    lines.append(kv('Shell',    'zsh  ·  Kitty', 30))
    lines.append('')

    # Section 2 — languages & tech
    lines.append(kv_dot('Languages', 'Programming', 'Python, C++, JavaScript, TypeScript', 30))
    lines.append(kv_dot('Languages', 'AI_ML',       'LangChain, LangGraph, PyTorch, Groq', 30))
    lines.append(kv_dot('Languages', 'Web',         'React, Node.js, Fastify, HTML/CSS',   30))
    lines.append(kv_dot('Languages', 'Systems',     'Docker, Linux, Nginx, Git, Bash',      30))
    lines.append('')

    # Section 3 — hobbies / interests
    lines.append(kv_dot('Hobbies', 'Software', 'AI Agents, Self-hosting, Automation', 30))
    lines.append(kv_dot('Hobbies', 'Hardware', 'Homelab, Proxmox, TrueNAS, ZFS RAID', 30))
    lines.append('')

    # Contact section
    lines.append(section('Contact', 52))
    lines.append('')
    lines.append(kv('Email',    'divyanshjoshidev@gmail.com', 30))
    lines.append(kv('LinkedIn', 'in/divyanshjoshidev', 30))
    lines.append('')

    # GitHub Stats section  — exact Andrew format
    lines.append(section('GitHub Stats', 52))
    lines.append('')

    # Repos line — exact Andrew6rant format
    lines.append(
        f'<tspan class="cc">. </tspan>'
        f'<tspan class="key">Repos</tspan>:'
        f'<tspan class="cc" id="repo_data_dots"> .... </tspan>'
        f'<tspan class="value" id="repo_data">{repos}</tspan>'
        f' {{<tspan class="key">Stars</tspan>:'
        f'<tspan class="cc" id="star_data_dots"> ........... </tspan>'
        f'<tspan class="value" id="star_data">{stars}</tspan>}}'
        f' | <tspan class="key">Followers</tspan>:'
        f'<tspan class="cc" id="follower_data_dots"> ....... </tspan>'
        f'<tspan class="value" id="follower_data">{followers}</tspan>'
    )

    # Commits | Followers  — exact Andrew format
    lines.append(
        f'<tspan class="cc">. </tspan>'
        f'<tspan class="key">Commits</tspan>:'
        f'<tspan class="cc" id="commit_data_dots"> ................. </tspan>'
        f'<tspan class="value" id="commit_data">{commits}</tspan>'
        f' | <tspan class="key">Followers</tspan>:'
        f'<tspan class="cc" id="follower_data_dots"> ....... </tspan>'
        f'<tspan class="value" id="follower_data">{followers}</tspan>'
    )

    # Lines of Code — EXACT Andrew6rant format with addColor / delColor
    if loc_net and loc_net != '0':
        loc_line = (
            f'<tspan class="cc">. </tspan>'
            f'<tspan class="key">Lines of Code on GitHub</tspan>:'
            f'<tspan class="cc" id="loc_data_dots">. </tspan>'
            f'<tspan class="value" id="loc_data">{loc_net}</tspan>'
            f' ( <tspan class="addColor" id="loc_add">{loc_add}</tspan>'
            f'<tspan class="addColor">++</tspan>, '
            f'<tspan id="loc_del_dots"> </tspan>'
            f'<tspan class="delColor" id="loc_del">{loc_del}</tspan>'
            f'<tspan class="delColor">--</tspan> )'
        )
    else:
        loc_line = (
            f'<tspan class="cc">. </tspan>'
            f'<tspan class="key">Lines of Code on GitHub</tspan>:'
            f'<tspan class="cc">. </tspan>'
            f'<tspan class="value">calculating... push to trigger refresh</tspan>'
        )
    lines.append(loc_line)

    # ── Build ASCII art tspans ──────────────────────────────────────────────
    art_lines = ASCII_ART.split('\n')
    art_svg = ''
    for i, ln in enumerate(art_lines):
        y = ART_Y0 + i * LINE_H
        art_svg += f'<tspan x="{ART_X}" y="{y}">{esc(ln)}</tspan>\n'

    # ── Build info tspans ───────────────────────────────────────────────────
    # Andrew uses empty lines as `. ` (just the cc dot) — same pattern
    info_svg = ''
    y = INFO_Y0
    for ln in lines:
        if ln == '':
            # blank line: just the dim dot placeholder
            info_svg += f'<tspan x="{INFO_X}" y="{y}" class="cc">. </tspan>\n'
        else:
            info_svg += f'<tspan x="{INFO_X}" y="{y}">{ln}</tspan>\n'
        y += LINE_H

    return f"""<?xml version='1.0' encoding='UTF-8'?>
<svg xmlns="http://www.w3.org/2000/svg" font-family="{FONT}" width="{W}px" height="{H}px" font-size="{FS}px">
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
<rect width="{W}px" height="{H}px" fill="{BG}" rx="15"/>
<text x="{ART_X}" y="{ART_Y0}" fill="{FG}">
{art_svg}
</text>
<text x="{INFO_X}" y="{INFO_Y0}" fill="{FG}">
{info_svg}
</text>
</svg>
"""


# ─── Main ─────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print('⚙  Fetching live GitHub stats...', flush=True)
    stats = fetch_stats()
    print(f'   login={stats["login"]}  repos={stats["repos"]}  stars={stats["stars"]}  '
          f'commits={stats["commits"]}  followers={stats["followers"]}')
    print(f'   LOC net={stats["loc_net"]}  add={stats["loc_add"]}  del={stats["loc_del"]}')
    print(f'   age={stats["age"]}')

    BASE = Path(__file__).parent

    for mode, dark in (('dark', True), ('light', False)):
        path = BASE / f'{mode}_mode.svg'
        path.write_text(make_svg(dark, stats), encoding='utf-8')
        print(f'✅ {mode}_mode.svg  →  {path}')
