import base64
from PIL import Image
import numpy as np

img = Image.open('/mnt/personal file/from w11/github/profile_cropped.jpg').convert('L')
img = img.resize((55, 36))
data = np.array(img)

chars = ['@', '%', '#', '*', '+', '=', '-', ':', '.', ' ']
ascii_lines = []
for row in data:
    line = ''.join([chars[min(9, int((p) / 256 * 10))] for p in row])
    ascii_lines.append(line)

right_side = [
    '',
    '<tspan class="key">Hi</tspan>, <tspan class="value">I\'m Divyansh Joshi</tspan>',
    '',
    '<tspan class="cc">. </tspan><tspan class="key">GitHub</tspan>:<tspan class="cc"> ............................ </tspan><tspan class="value">oldregime</tspan>',
    '<tspan class="cc">. </tspan><tspan class="key">Education</tspan>:<tspan class="cc"> ......................... </tspan><tspan class="value">B.Tech CS @ VIT</tspan>',
    '<tspan class="cc">. </tspan><tspan class="key">Focus</tspan>:<tspan class="cc"> ............................. </tspan><tspan class="value">AI-driven platforms, Secure networks</tspan>',
    '<tspan class="cc">. </tspan>',
    '<tspan class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Programming</tspan>:<tspan class="cc"> ..... </tspan><tspan class="value">C++, Python, JavaScript</tspan>',
    '<tspan class="cc">. </tspan><tspan class="key">Technologies</tspan>:<tspan class="cc"> ................... </tspan><tspan class="value">LangGraph, Proxmox, ZFS, ESP32</tspan>',
    '<tspan class="cc">. </tspan>',
    '<tspan class="cc">. </tspan><tspan class="key">Interests</tspan>.<tspan class="key">Tech</tspan>:<tspan class="cc"> ................ </tspan><tspan class="value">Zero-trust networking, highly available systems</tspan>',
    '<tspan class="cc">. </tspan><tspan class="key">Philosophy</tspan>:<tspan class="cc"> ...................... </tspan><tspan class="value">"Simplicity is the ultimate sophistication."</tspan>',
    '<tspan class="cc">. </tspan>',
    '- Contact -——————————————————————————————————————————————-—-',
    '<tspan class="cc">. </tspan><tspan class="key">LinkedIn</tspan>:<tspan class="cc"> .................................... </tspan><tspan class="value">divyanshjoshidev</tspan>',
]

while len(right_side) < len(ascii_lines):
    right_side.append('')

def get_svg(is_dark):
    bg_color = "#0d1117" if is_dark else "#f6f8fa"
    text_color = "#c9d1d9" if is_dark else "#24292f"
    
    if is_dark:
        css = """
        .key {fill: #e3b341;}
        .value {fill: #a5d6ff;}
        .cc {fill: #8b949e;}
        """
    else:
        css = """
        .key {fill: #953800;}
        .value {fill: #0a3069;}
        .cc {fill: #c2cfde;}
        """
        
    svg = f"""<?xml version='1.0' encoding='UTF-8'?>
<svg xmlns="http://www.w3.org/2000/svg" font-family="ConsolasFallback,Consolas,monospace" width="985px" height="530px" font-size="14px">
<style>
@font-face {{
src: local('Consolas'), local('Consolas Bold');
font-family: 'ConsolasFallback';
font-display: swap;
-webkit-size-adjust: 109%;
size-adjust: 109%;
}}
{css}
text, tspan {{white-space: pre;}}
</style>
<rect width="985px" height="530px" fill="{bg_color}" rx="15"/>
<text fill="{text_color}" class="ascii">
"""
    
    y = 30
    for i in range(len(ascii_lines)):
        asc = ascii_lines[i].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        right = right_side[i] if i < len(right_side) else ""
        
        svg += f'<tspan x="15" y="{y}">{asc}</tspan>\n'
        if right:
            svg += f'<tspan x="450" y="{y}">{right}</tspan>\n'
        y += 14
        
    svg += """
</text>
</svg>
"""
    return svg

with open('/mnt/personal file/from w11/github/oldregime_readme/dark_mode.svg', 'w', encoding='utf-8') as f:
    f.write(get_svg(True))
with open('/mnt/personal file/from w11/github/oldregime_readme/light_mode.svg', 'w', encoding='utf-8') as f:
    f.write(get_svg(False))
