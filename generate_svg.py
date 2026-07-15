#!/usr/bin/env python3
"""
Generate Andrew6rant-exact style neofetch SVG profile cards.
Dark + Light mode SVGs. Fetches live GitHub stats via `gh` CLI.
"""

import subprocess
import json
import sys

# ─── ASCII Art (left panel) ───────────────────────────────────────────────────
# Stylised terminal / code motif — fits ~26 lines at 20px spacing = 520px
ASCII_ART = """\
 ┌─────────────────────────┐
 │  #!/usr/bin/env dj      │
 │  ░░░░░░░░░░░░░░░░░░░░░  │
 │                         │
 │  fn main() {            │
 │    build();             │
 │    ship();              │
 │    learn();             │
 │    repeat();            │
 │  }                      │
 │                         │
 ├─────────────────────────┤
 │  Languages              │
 │  ▓▓▓▓▓▓▓▓▓ Python      │
 │  ▓▓▓▓▓▓▓░░ JavaScript  │
 │  ▓▓▓▓▓▓░░░ C++         │
 │  ▓▓▓▓▓░░░░ TypeScript   │
 │  ▓▓▓▓░░░░░ Bash/Shell   │
 ├─────────────────────────┤
 │  Stack                  │
 │  🐧 Fedora  ⚙ KDE      │
 │  🧠 AI/ML  🏗 DevOps   │
 │  🔒 ZFS    ☁ Proxmox   │
 │  📡 ESP32  🔧 Docker    │
 └─────────────────────────┘"""

# ─── Live GitHub Stats ────────────────────────────────────────────────────────

def run(cmd):
    try:
        return subprocess.check_output(cmd, stderr=subprocess.DEVNULL).decode().strip()
    except Exception:
        return ''

def fetch_stats():
    stats = {
        'repos': '53', 'followers': '2', 'following': '8',
        'stars': '5',  'commits': '0',  'prs': '0',
        'login': 'oldregime',
    }
    try:
        user_raw = run(['gh', 'api', 'user'])
        if user_raw:
            user = json.loads(user_raw)
            stats['repos']     = str(user.get('public_repos', stats['repos']))
            stats['followers'] = str(user.get('followers',    stats['followers']))
            stats['following'] = str(user.get('following',    stats['following']))
            stats['login']     = user.get('login', 'oldregime')
        login = stats['login']

        # Stars
        s = run(['gh', 'api', f'users/{login}/repos', '--paginate', '-q', '.[].stargazers_count'])
        if s:
            stats['stars'] = str(sum(int(x) for x in s.split() if x.strip().isdigit()))

        # Contributions (commits proxy)
        q = ('query { user(login: "%s") { contributionsCollection {'
             'contributionCalendar { totalContributions }}}}') % login
        g = run(['gh', 'api', 'graphql', '-f', f'query={q}'])
        if g:
            stats['commits'] = str(
                json.loads(g)['data']['user']
                ['contributionsCollection']['contributionCalendar']['totalContributions'])

        # PRs
        pr = run(['gh', 'api', 'search/issues', '-q', '.total_count',
                  '-f', f'q=author:{login} type:pr'])
        if pr.strip().isdigit():
            stats['prs'] = pr.strip()

    except Exception as e:
        print(f'Warning: {e}', file=sys.stderr)
    return stats

# ─── SVG Helpers ─────────────────────────────────────────────────────────────

def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def kv(key: str, value: str, pad: int = 29) -> str:
    """Andrew-style  ". Key:....... Value" line."""
    dots = max(pad - len(key), 1) * '.'
    return (f'<tspan class="cc">. </tspan>'
            f'<tspan class="key">{esc(key)}</tspan>'
            f':<tspan class="cc">{dots} </tspan>'
            f'<tspan class="value">{esc(value)}</tspan>')

def section(title: str, dashes: int = 32) -> str:
    d = '—' * max(dashes - len(title) - 2, 1)
    return (f'<tspan class="text">- </tspan>'
            f'<tspan class="key">{esc(title)}</tspan>'
            f'<tspan class="cc"> {d}</tspan>')

# ─── SVG Generator ───────────────────────────────────────────────────────────

def make_svg(is_dark: bool, stats: dict) -> str:
    if is_dark:
        bg    = '#0d1117'; fg = '#c9d1d9'
        KEY   = '#e3b341'; VAL = '#a5d6ff'; CC = '#8b949e'
        ASCII = '#a5d6ff'
    else:
        bg    = '#ffffff'; fg = '#24292f'
        KEY   = '#953800'; VAL = '#0a3069'; CC = '#8c959f'
        ASCII = '#0a3069'

    W, H = 985, 530
    FONT = "ConsolasFallback,Consolas,'Courier New',monospace"

    # Right-side lines
    r, s = stats['repos'], stats['stars']
    fol,  fing = stats['followers'], stats['following']
    c, p = stats['commits'], stats['prs']

    right = [
        # Header
        (f'<tspan class="key">oldregime</tspan><tspan class="text">@</tspan>'
         f'<tspan class="value">github</tspan>'
         f'<tspan class="cc"> —————————————————————————————————————————</tspan>'),
        '',
        # System
        kv('OS',     'Fedora Linux 44, Windows 11, Android'),
        kv('Uptime', 'Since Mar 2020  |  India 🇮🇳'),
        kv('Host',   'VIT Bhopal University'),
        kv('Role',   'SWE & AI Engineer'),
        kv('IDE',    'VS Code · JetBrains · Neovim'),
        kv('Shell',  'zsh + Kitty terminal'),
        kv('CPU',    'Ryzen 7 7840HS · RTX 4050 Laptop GPU'),
        '',
        # Languages
        kv('Languages.Programming', 'Python, C++, JS, TypeScript'),
        kv('Languages.Web',         'React, Node.js, HTML/CSS'),
        kv('Languages.AI',          'LangChain, LangGraph, PyTorch'),
        kv('Languages.DevOps',      'Docker, Linux, Git, Nginx'),
        kv('Languages.Database',    'PostgreSQL, MongoDB, SQLite'),
        '',
        # Interests
        kv('Interests.Software', 'AI Agents · Self-hosting · Automation'),
        kv('Interests.Hardware', 'Homelab · Proxmox · TrueNAS · ZFS'),
        kv('Interests.Network',  'Zero-trust · ESP32 · WireGuard'),
        kv('Exploring',          'Agentic AI · RAG · Kubernetes · MLOps'),
        '',
        # Contact
        section('Contact'),
        '',
        kv('Email.Personal', 'divyanshjoshidev@gmail.com'),
        kv('GitHub',         'github.com/oldregime'),
        kv('LinkedIn',       'linkedin.com/in/divyanshjoshidev'),
        kv('Website',        'oldregime.github.io'),
        '',
        # GitHub Stats
        section('GitHub Stats'),
        '',
        (f'<tspan class="cc">. </tspan><tspan class="key">Repos</tspan>:'
         f'<tspan class="cc"> .............. </tspan><tspan class="value">{r}</tspan>'
         f' {{<tspan class="key">Stars</tspan>: <tspan class="value">{s}</tspan>}} | '
         f'<tspan class="key">Following</tspan>:<tspan class="cc"> . </tspan>'
         f'<tspan class="value">{fing}</tspan>'),
        (f'<tspan class="cc">. </tspan><tspan class="key">Commits</tspan>:'
         f'<tspan class="cc"> .............. </tspan><tspan class="value">{c}</tspan>'
         f' | <tspan class="key">Followers</tspan>:<tspan class="cc"> ...... </tspan>'
         f'<tspan class="value">{fol}</tspan>'),
        (f'<tspan class="cc">. </tspan><tspan class="key">Pull Requests</tspan>:'
         f'<tspan class="cc"> ........ </tspan><tspan class="value">{p}</tspan>'),
    ]

    # Build art tspans
    art_lines = ASCII_ART.split('\n')
    art_svg = ''
    for i, ln in enumerate(art_lines):
        y = 22 + i * 20
        art_svg += f'<tspan x="15" y="{y}" class="ascii">{esc(ln)}</tspan>\n'

    # Build right tspans  (start at y=22, step 18px — tight neofetch spacing)
    right_svg = ''
    y = 22
    for ln in right:
        right_svg += f'<tspan x="360" y="{y}">{ln}</tspan>\n'
        y += 18

    # Auto-size height to fit all content
    needed_h = max(len(art_lines) * 20 + 30, y + 10)
    H = needed_h

    return f"""<?xml version='1.0' encoding='UTF-8'?>
<svg xmlns="http://www.w3.org/2000/svg" font-family="{FONT}" width="{W}px" height="{H}px" font-size="15px">
<style>
@font-face {{
src: local('Consolas'), local('Consolas Bold');
font-family: 'ConsolasFallback';
font-display: swap;
-webkit-size-adjust: 109%;
size-adjust: 109%;
}}
.key   {{fill: {KEY};}}
.value {{fill: {VAL};}}
.cc    {{fill: {CC};}}
.text  {{fill: {fg};}}
.ascii {{fill: {ASCII}; font-size: 14px;}}
text, tspan {{white-space: pre;}}
</style>
<rect width="{W}px" height="{H}px" fill="{bg}" rx="15"/>
<text fill="{fg}">
{art_svg}
{right_svg}
</text>
</svg>
"""

# ─── Main ─────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    from pathlib import Path

    print('⚙  Fetching live GitHub stats...', flush=True)
    stats = fetch_stats()
    print(f'   repos={stats["repos"]}  stars={stats["stars"]}  '
          f'commits={stats["commits"]}  followers={stats["followers"]}  prs={stats["prs"]}')

    # Output next to this script (works locally and in CI)
    BASE = Path(__file__).parent

    for mode, dark in (('dark', True), ('light', False)):
        path = BASE / f'{mode}_mode.svg'
        path.write_text(make_svg(dark, stats), encoding='utf-8')
        print(f'✅ {mode}_mode.svg written')
