import base64

def get_base64_img(path):
    with open(path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

try:
    b64_dark = get_base64_img('/mnt/personal file/from w11/github/oldregime_readme/profile_dark.png')
    b64_light = get_base64_img('/mnt/personal file/from w11/github/oldregime_readme/profile_light.png')
except FileNotFoundError:
    print("Error: PNG files not found!")
    exit(1)

right_side = [
    '<tspan class="key">Divyansh Joshi</tspan> <tspan class="value">| AI Engineer • Full Stack Developer • Linux Enthusiast</tspan>',
    '',
    '<tspan class="cc">. </tspan><tspan class="key">OS</tspan>:<tspan class="cc"> .......................... </tspan><tspan class="value">Fedora Linux</tspan>',
    '<tspan class="cc">. </tspan><tspan class="key">Shell</tspan>:<tspan class="cc"> ....................... </tspan><tspan class="value">zsh</tspan>',
    '<tspan class="cc">. </tspan><tspan class="key">Editor</tspan>:<tspan class="cc"> ...................... </tspan><tspan class="value">VS Code</tspan>',
    '<tspan class="cc">. </tspan><tspan class="key">Location</tspan>:<tspan class="cc"> .................... </tspan><tspan class="value">India</tspan>',
    '<tspan class="cc">. </tspan><tspan class="key">Education</tspan>:<tspan class="cc"> ................... </tspan><tspan class="value">B.Tech CS @ VIT</tspan>',
    '<tspan class="cc">. </tspan><tspan class="key">Status</tspan>:<tspan class="cc"> ...................... </tspan><tspan class="value">Building • Learning • Sharing</tspan>',
    '<tspan class="cc">. </tspan>',
    '<tspan class="cc">. </tspan><tspan class="key">Languages</tspan>:<tspan class="cc"> ................... </tspan><tspan class="value">Python, C++, JavaScript, SQL, Bash</tspan>',
    '<tspan class="cc">. </tspan><tspan class="key">Tech</tspan>.<tspan class="key">Frontend</tspan>:<tspan class="cc"> ............... </tspan><tspan class="value">React, HTML, CSS, Tailwind</tspan>',
    '<tspan class="cc">. </tspan><tspan class="key">Tech</tspan>.<tspan class="key">Backend</tspan>:<tspan class="cc"> ................ </tspan><tspan class="value">FastAPI, Node.js</tspan>',
    '<tspan class="cc">. </tspan><tspan class="key">Tech</tspan>.<tspan class="key">AI_ML</tspan>:<tspan class="cc"> .................. </tspan><tspan class="value">LangChain, LangGraph, OpenAI</tspan>',
    '<tspan class="cc">. </tspan><tspan class="key">Tech</tspan>.<tspan class="key">DevOps</tspan>:<tspan class="cc"> ................. </tspan><tspan class="value">Docker, Proxmox, Git, Linux</tspan>',
    '<tspan class="cc">. </tspan><tspan class="key">Tech</tspan>.<tspan class="key">Database</tspan>:<tspan class="cc"> ............... </tspan><tspan class="value">PostgreSQL, MongoDB, SQLite</tspan>',
    '<tspan class="cc">. </tspan>',
    '<tspan class="cc">. </tspan><tspan class="key">Interests</tspan>:<tspan class="cc"> ................... </tspan><tspan class="value">AI Agents, Zero-trust networking, Linux</tspan>',
    '<tspan class="cc">. </tspan><tspan class="key">Exploring</tspan>:<tspan class="cc"> ................... </tspan><tspan class="value">Agentic AI, RAG, Kubernetes</tspan>',
    '<tspan class="cc">. </tspan>',
    '- Let\'s Connect -—————————————————————————————————————————————————',
    '<tspan class="cc">. </tspan><tspan class="key">Email</tspan>:<tspan class="cc"> ....................... </tspan><tspan class="value">divyanshjoshidev@gmail.com</tspan>',
    '<tspan class="cc">. </tspan><tspan class="key">GitHub</tspan>:<tspan class="cc"> ...................... </tspan><tspan class="value">github.com/oldregime</tspan>',
    '<tspan class="cc">. </tspan><tspan class="key">LinkedIn</tspan>:<tspan class="cc"> .................... </tspan><tspan class="value">linkedin.com/in/divyanshjoshidev</tspan>',
]

def get_svg(is_dark):
    bg_color = "#0d1117" if is_dark else "#f6f8fa"
    text_color = "#c9d1d9" if is_dark else "#24292f"
    b64 = b64_dark if is_dark else b64_light
    
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
<svg xmlns="http://www.w3.org/2000/svg" font-family="ConsolasFallback,Consolas,monospace" width="1050px" height="580px" font-size="15px">
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
<rect width="1050px" height="580px" fill="{bg_color}" rx="15"/>
<image href="data:image/png;base64,{b64}" x="15" y="40" width="400" height="500" preserveAspectRatio="xMidYMid slice" />
<text fill="{text_color}" class="ascii">
"""
    
    y = 50
    for right in right_side:
        svg += f'<tspan x="420" y="{y}">{right}</tspan>\n'
        y += 20
        
    svg += """
</text>
</svg>
"""
    return svg

with open('/mnt/personal file/from w11/github/oldregime_readme/dark_mode.svg', 'w', encoding='utf-8') as f:
    f.write(get_svg(True))
with open('/mnt/personal file/from w11/github/oldregime_readme/light_mode.svg', 'w', encoding='utf-8') as f:
    f.write(get_svg(False))

print("Created SVGs with perfectly embedded high-res ASCII PNGs and NO OVERLAPPING!")
