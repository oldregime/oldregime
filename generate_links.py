#!/usr/bin/env python3
"""
Generate sleek individual icon-link pill SVGs (dark + light) for social links.
"""

from pathlib import Path

LINKS = [
    (
        'GitHub',
        'https://github.com/oldregime',
        'M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12',
        '#c9d1d9',
    ),
    (
        'LinkedIn',
        'https://linkedin.com/in/divyanshjoshidev',
        'M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z',
        '#a5d6ff',
    ),
    (
        'Discord',
        'https://discord.com/users/theoldregime',
        'M20.317 4.492c-1.53-.69-3.17-1.2-4.885-1.49a.075.075 0 0 0-.079.036c-.21.369-.444.85-.608 1.23a18.566 18.566 0 0 0-5.487 0 12.36 12.36 0 0 0-.617-1.23A.077.077 0 0 0 8.562 3c-1.714.29-3.354.8-4.885 1.491a.07.07 0 0 0-.032.027C.533 9.093-.32 13.555.099 17.961a.08.08 0 0 0 .031.055 20.03 20.03 0 0 0 5.993 2.98.078.078 0 0 0 .084-.026c.462-.62.874-1.275 1.226-1.963.021-.04.001-.088-.041-.104a13.201 13.201 0 0 1-1.872-.878.075.075 0 0 1-.008-.125c.126-.093.252-.19.372-.287a.075.075 0 0 1 .078-.01c3.927 1.764 8.18 1.764 12.061 0a.075.075 0 0 1 .079.009c.12.098.245.195.372.288a.075.075 0 0 1-.006.125c-.598.344-1.22.635-1.873.877a.075.075 0 0 0-.041.105c.36.687.772 1.341 1.225 1.962a.077.077 0 0 0 .084.028 19.963 19.963 0 0 0 6.002-2.981.076.076 0 0 0 .032-.054c.5-5.094-.838-9.52-3.549-13.442a.06.06 0 0 0-.031-.028zM8.02 15.278c-1.182 0-2.157-1.069-2.157-2.38 0-1.312.956-2.38 2.157-2.38 1.21 0 2.176 1.077 2.157 2.38 0 1.312-.956 2.38-2.157 2.38zm7.975 0c-1.183 0-2.157-1.069-2.157-2.38 0-1.312.955-2.38 2.157-2.38 1.21 0 2.176 1.077 2.157 2.38 0 1.312-.946 2.38-2.157 2.38z',
        '#ffa657',
    ),
    (
        'Website',
        'https://oldregime.github.io',
        'M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z',
        '#3fb950',
    ),
    (
        'Resume',
        'https://oldregime.github.io/resume',
        'M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z',
        '#f85149',
    ),
    (
        'Email',
        'mailto:divyanshjoshidev@gmail.com',
        'M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z',
        '#616e7f',
    ),
]

LABEL_DARK  = '#8b949e'
LABEL_LIGHT = '#57606a'

def make_pill(is_dark, lbl, icon_d, color):
    bg     = '#161b22' if is_dark else '#f6f8fa'
    border = '#30363d' if is_dark else '#d0d7de'
    label  = LABEL_DARK if is_dark else LABEL_LIGHT

    PW = 120
    PH = 44
    R  = 8

    # icon centered horizontally, label below
    icon_x = (PW - 24) // 2
    icon_y = 8
    cx = PW // 2

    return f"""<?xml version='1.0' encoding='UTF-8'?>
<svg xmlns="http://www.w3.org/2000/svg" width="{PW}px" height="{PH}px">
<style>
@font-face {{
src: local('Consolas'), local('Consolas Bold');
font-family: 'ConsolasFallback';
font-display: swap;
}}
</style>
<rect width="{PW}" height="{PH}" rx="{R}" fill="{bg}" stroke="{border}" stroke-width="1"/>
<svg x="{icon_x}" y="{icon_y}" width="24" height="24" viewBox="0 0 24 24">
  <path d="{icon_d}" fill="{color}"/>
</svg>
<text x="{cx}" y="{PH - 6}" font-family="ConsolasFallback,Consolas,monospace" font-size="10" fill="{label}" text-anchor="middle">{lbl}</text>
</svg>
"""

if __name__ == '__main__':
    BASE = Path(__file__).parent
    assets_dir = BASE / 'assets'
    assets_dir.mkdir(exist_ok=True)

    readme_links = []
    
    for lbl, url, icon_d, color in LINKS:
        name = lbl.lower()
        for mode, dark in (('dark', True), ('light', False)):
            p = assets_dir / f'link_{name}_{mode}.svg'
            p.write_text(make_pill(dark, lbl, icon_d, color), encoding='utf-8')
            import sys; print(f'✅ {p.name}', file=sys.stderr)
            
        readme_links.append(f'''  <a href="{url}">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/link_{name}_dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="assets/link_{name}_light.svg">
      <img alt="{lbl}" src="assets/link_{name}_dark.svg">
    </picture>
  </a>''')
          
    # Print the markdown snippet to easily embed
    print("\n--- README Snippet ---")
    print('<p align="center">')
    print("\n".join(readme_links))
    print("</p>")
