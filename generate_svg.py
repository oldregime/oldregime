#!/usr/bin/env python3
"""
Andrew6rant-exact neofetch SVG profile generator for Divyansh Joshi (oldregime).
"""

from __future__ import annotations
import subprocess, json, sys
from pathlib import Path
from datetime import datetime, timezone

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

def esc(s): return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

def sec(title, width=41):
    dashes = '—' * max(width - len(title) - 4, 4)
    return f'- {esc(title)} -{dashes}-—-'

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

    FONT  = 'ConsolasFallback,Consolas,monospace'
    FS    = 16          
    LH    = 20          
    AX    = 15          
    AY0   = 30          
    IX    = 385         
    IY0   = 30          
    PAD_B = 30          

    ln = stats
    rows = []

    def add_raw(s): rows.append(s)
    def add_blank(): rows.append(f'<tspan class="cc">. </tspan>')

    def add_kv(key, val, pad=21, max_val=38):
        d = ' ' + '.' * max(pad - len(key) - 1, 1) + ' '
        if len(val) <= max_val:
            rows.append(f'<tspan class="cc">. </tspan><tspan class="key">{esc(key)}</tspan>:<tspan class="cc">{d}</tspan><tspan class="value">{esc(val)}</tspan>')
        else:
            words = val.split(', ')
            l1, l2 = [], []
            for w in words:
                if len(', '.join(l1 + [w])) <= max_val:
                    l1.append(w)
                else:
                    l2.append(w)
            v1 = ', '.join(l1) + ','
            v2 = ', '.join(l2)
            rows.append(f'<tspan class="cc">. </tspan><tspan class="key">{esc(key)}</tspan>:<tspan class="cc">{d}</tspan><tspan class="value">{esc(v1)}</tspan>')
            
            indent = ' ' * (len(key) + 1 + len(d) - 1)
            rows.append(f'<tspan class="cc">. </tspan><tspan class="cc">{indent}</tspan><tspan class="value">{esc(v2)}</tspan>')

    def add_kvd(k1, k2, val, pad=21, max_val=38):
        add_kv(f'{k1}.{k2}', val, pad, max_val)

    add_raw(f'{esc(ln["login"])}@github -{"—" * 41}-—-')
    add_blank()
    add_kv('OS', 'Fedora Linux 44, Windows 11, Android')
    add_kv('Uptime', ln['age'])
    add_kv('Host', 'VIT Bhopal University, India 🇮🇳')
    add_kv('Role', 'CS Undergrad  ·  Software Engineer')
    add_kv('IDE', 'VS Code, JetBrains, Neovim')
    add_kv('Shell', 'zsh  ·  Kitty')
    add_blank()
    add_kvd('Languages', 'Programming', 'Python, C++, JavaScript, TypeScript')
    add_kvd('Languages', 'AI_ML', 'LangChain, LangGraph, PyTorch, Groq')
    add_kvd('Languages', 'Web', 'React, Node.js, Fastify, HTML/CSS')
    add_kvd('Languages', 'Systems', 'Docker, Linux, Nginx, Git, Bash')
    add_blank()
    add_kvd('Hobbies', 'Software', 'AI Agents, Self-hosting, Automation')
    add_kvd('Hobbies', 'Hardware', 'Homelab, Proxmox, TrueNAS, ZFS RAID')
    add_blank()
    add_raw(sec('Contact', 42))
    add_blank()
    add_kv('Email', 'divyanshjoshidev@gmail.com')
    add_kv('Discord', 'theoldregime')
    add_kv('LinkedIn', 'in/divyanshjoshidev')
    add_blank()
    add_raw(sec('GitHub Stats', 42))
    add_blank()

    rows.append(f'<tspan class="cc">. </tspan>'
         f'<tspan class="key">Repos</tspan>:<tspan class="cc"> ..... </tspan>'
         f'<tspan class="value">{ln["repos"]}</tspan>'
         f' {{<tspan class="key">Stars</tspan>:<tspan class="cc"> ... </tspan>'
         f'<tspan class="value">{ln["stars"]}</tspan>}}'
         f' | <tspan class="key">Followers</tspan>:<tspan class="cc"> .. </tspan>'
         f'<tspan class="value">{ln["followers"]}</tspan>')
    
    rows.append(f'<tspan class="cc">. </tspan>'
         f'<tspan class="key">Commits</tspan>:<tspan class="cc"> ...................... </tspan>'
         f'<tspan class="value">{ln["commits"]}</tspan>')
         
    rows.append(f'<tspan class="cc">. </tspan>'
         f'<tspan class="key">LOC</tspan>:<tspan class="cc"> . </tspan>'
         f'<tspan class="value">{ln["loc_net"]}</tspan>'
         f' (<tspan class="addColor">{ln["loc_add"]}++</tspan>, '
         f'<tspan class="delColor">{ln["loc_del"]}--</tspan>)')

    art_lines  = ART.split('\n')
    art_height = AY0 + len(art_lines) * LH          
    inf_height = IY0 + (len(rows) - 1) * LH          
    H  = max(art_height, inf_height) + PAD_B          

    art_svg = ''
    for i, line in enumerate(art_lines):
        art_svg += f'<tspan x="{AX}" y="{AY0 + i*LH}">{esc(line)}</tspan>\n'

    info_svg = ''
    for i, row in enumerate(rows):
        y = IY0 + i * LH
        info_svg += f'<tspan x="{IX}" y="{y}">{row}</tspan>\n'

    return f"""<?xml version='1.0' encoding='UTF-8'?>
<svg xmlns="http://www.w3.org/2000/svg" font-family="{FONT}" width="985px" height="{H}px" font-size="{FS}px">
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
<rect width="985px" height="{H}px" fill="{BG}" rx="15"/>
<text x="{AX}" y="{AY0}" fill="{FG}">
{art_svg}
</text>
<text x="{IX}" y="{IY0}" fill="{FG}">
{info_svg}
</text>
</svg>
"""

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
