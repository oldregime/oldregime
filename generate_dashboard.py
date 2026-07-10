import sys

ascii_art = """⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣤⣤⣤⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⣾⣿⣿⣿⣿⣿⡿⠿⠿⠛⠛⠛⠛⠋⠉⠀⣠⣾⢿⢳⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣿⣿⣿⣿⣿⠟⠁⠀⠀⢀⣠⣴⡶⠶⠶⠶⠿⠋⠁⣾⠟⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⣿⣿⣿⣿⣿⣷⣦⡀⠰⡽⡟⠉⠉⠻⠿⣆⠀⠀⠀⡧⠤⣼⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⢀⠴⠒⠒⢌⠳⡀⠀⢣⡀⣼⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠹⣿⡿⠟⠛⠛⠿⣿⣿⣿⡁⠀⠀⡎⠀⠀⠀⢀⡇⠁⠀⠀⠉⠳⢬⣷⣄⠀⠀⠀⠀⠀⠀⠀⣰⣾⣦⣀⣀⣀⠀⣀⡀⠀⠀⠀
⢰⡇⢰⡾⠛⠛⠒⠦⣌⠻⢿⠦⠀⠘⣄⠀⠀⡻⡵⠒⠂⠀⠀⠀⠀⠀⠙⣷⠀⠀⠀⠀⠀⠀⠻⡟⠀⠀⠈⠉⠛⣿⣿⠀⠀⠀
⠘⣧⠸⣄⠀⠀⠀⠀⠀⣤⠀⠀⠀⠀⠀⠈⠁⠀⠙⠤⠤⢤⣄⣀⡀⠀⣠⡿⠀⠀⠀⠀⠀⠀⠀⡇⠠⣠⠀⠀⣰⠏⠉⠀⠀⠀
⠀⠘⠳⣤⣙⠒⠤⠤⠤⢛⣁⠀⠀⠀⠀⠀⠀⠸⠓⠒⢒⠭⠟⠀⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⡷⠿⠖⠀⣰⠏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠙⠛⠛⠛⠉⠙⠷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠟⠁⠀⠀⠀⠀⢠⣤⢤⣤⣞⠑⣄⣀⠞⣻⣀⣀⣠⡴⢦⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠦⣄⡀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠈⠛⠓⣿⣿⡟⠓⡿⢺⣭⣭⣉⢠⣶⠛⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⢶⣄⡀⠀⠙⢦⡀⠀⠀⣇⡀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡟⢰⠁⠀⠑⢮⡞⠳⣽⡷⣌⣳⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⢁⠞⣩⢧⡀⠀⢀⣿⢶⣟⠻⢿⣷⡦⢤⣤⣀⣀⡴⠟⡾⣀⡎⠀⠀⠀⠀⢱⣄⡜⣷⠈⠛⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⠀⠘⠁⣼⡃⠀⣾⢭⣆⠱⡹⣌⢻⣷⡀⠀⠀⠀⣠⣤⡷⠻⡇⠀⠀⠀⠀⣼⠉⠉⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠳⢤⣄⣀⣻⣄⡇⠀⡟⢹⠿⣿⠢⡹⣿⡛⠛⠛⠛⠉⠀⠀⣿⠒⣦⡔⠐⣯⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡯⢿⡇⠀⢻⠈⠣⣹⣆⠑⡜⣷⡀⠀⠀⠀⠀⢀⡇⠀⣸⣇⠀⢹⡀⠀⠀⠀⠀⠀"""


def get_svg(is_dark):
    bg_color = "#09090b" if is_dark else "#f4f4f5"
    border_color = "#27272a" if is_dark else "#e4e4e7"
    text_main = "#f4f4f5" if is_dark else "#09090b"
    text_muted = "#a1a1aa" if is_dark else "#71717a"
    box_bg = "#18181b" if is_dark else "#ffffff"
    title_color = "#60a5fa" if is_dark else "#2563eb"
    subtitle_color = "#2dd4bf" if is_dark else "#0d9488"
    
    ascii_svg = ""
    y = 120
    for line in ascii_art.split('\n'):
        # preserve spacing
        safe_line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace(' ', '&#160;')
        ascii_svg += f'<text x="15" y="{y}" class="ascii-text">{safe_line}</text>\n'
        y += 20

    svg = f"""<?xml version='1.0' encoding='UTF-8'?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 680" width="1200" height="680" font-family="Consolas, 'Courier New', monospace">
    <style>
        .title {{ font: bold 32px 'Segoe UI', Ubuntu, sans-serif; fill: {title_color}; }}
        .subtitle {{ font: 16px 'Segoe UI', Ubuntu, sans-serif; fill: {subtitle_color}; }}
        .section-title {{ font: bold 16px 'Segoe UI', Ubuntu, sans-serif; }}
        .label {{ fill: {text_muted}; font-size: 14px; }}
        .value {{ fill: {text_main}; font-size: 14px; }}
        .box-title {{ fill: {text_muted}; font-size: 13px; }}
        .box-val {{ fill: {title_color}; font: bold 24px 'Segoe UI', Ubuntu, sans-serif; }}
        .box-sub {{ fill: {text_muted}; font-size: 11px; }}
        .ascii-text {{ fill: {text_main}; font: 14px Consolas, monospace; letter-spacing: 0px; }}
        line {{ stroke: {border_color}; stroke-dasharray: 4 4; }}
    </style>

    <!-- Background -->
    <rect width="1190" height="670" x="5" y="5" fill="{bg_color}" rx="12" stroke="{border_color}" stroke-width="2"/>
    
    <!-- Left Profile ASCII Art -->
    {ascii_svg}

    <!-- Top Right: Header -->
    <text x="520" y="50" class="title">Divyansh Joshi</text>
    <text x="520" y="80" class="subtitle">AI Engineer • Full Stack Developer • Linux Enthusiast</text>
    <line x1="520" y1="100" x2="1170" y2="100"/>

    <!-- Section 1: Basic Info & Languages -->
    <!-- Basic Info -->
    <text x="520" y="130" class="label">🐧 OS</text><text x="630" y="130" class="value">: Fedora Linux</text>
    <text x="520" y="155" class="label">🐚 Shell</text><text x="630" y="155" class="value">: zsh</text>
    <text x="520" y="180" class="label">💻 Editor</text><text x="630" y="180" class="value">: VS Code, Neovim</text>
    <text x="520" y="205" class="label">📍 Location</text><text x="630" y="205" class="value">: India 🇮🇳</text>
    <text x="520" y="230" class="label">🎓 Education</text><text x="630" y="230" class="value">: B.Tech CS @ VIT</text>
    <text x="520" y="255" class="label">🚀 Status</text><text x="630" y="255" class="value">: Building • Learning • Sharing</text>
    
    <!-- Languages -->
    <text x="880" y="130" class="section-title" fill="#f97316">&lt;/&gt; Languages</text>
    <text x="880" y="155" class="value">• Python</text>
    <text x="880" y="180" class="value">• C++</text>
    <text x="880" y="205" class="value">• JavaScript</text>
    <text x="880" y="230" class="value">• SQL</text>
    <text x="880" y="255" class="value">• Bash</text>

    <line x1="520" y1="275" x2="1170" y2="275"/>

    <!-- Section 2: Tech Stack & Interests -->
    <!-- Tech Stack -->
    <text x="520" y="300" class="section-title" fill="#3b82f6">🚀 Tech Stack</text>
    <text x="520" y="325" class="label">Frontend</text><text x="620" y="325" class="value">: React, HTML, CSS, Tailwind</text>
    <text x="520" y="350" class="label">Backend</text><text x="620" y="350" class="value">: FastAPI, Node.js</text>
    <text x="520" y="375" class="label">AI / ML</text><text x="620" y="375" class="value">: LangChain, LangGraph, OpenAI</text>
    <text x="520" y="400" class="label">Database</text><text x="620" y="400" class="value">: PostgreSQL, MongoDB, SQLite</text>
    <text x="520" y="425" class="label">Hardware</text><text x="620" y="425" class="value">: ESP32 Embedded Systems</text>
    <text x="520" y="450" class="label">DevOps</text><text x="620" y="450" class="value">: Docker, Linux, Proxmox, ZFS</text>

    <!-- Interests -->
    <text x="880" y="300" class="section-title" fill="#eab308">⭐ Interests</text>
    <text x="880" y="325" class="value">• AI Agents &amp; LLMs</text>
    <text x="880" y="350" class="value">• Zero-trust Networking</text>
    <text x="880" y="375" class="value">• DevOps &amp; Automation</text>
    <text x="880" y="400" class="value">• Open Source</text>
    <text x="880" y="425" class="value">• Linux &amp; System Tuning</text>
    <text x="880" y="450" class="value">• Highly Available Systems</text>

    <line x1="520" y1="475" x2="1170" y2="475"/>

    <!-- Section 3: Exploring & Hobbies -->
    <text x="520" y="500" class="section-title" fill="#ec4899">💡 Currently Exploring</text>
    <text x="520" y="525" class="value">Agentic AI • RAG • Kubernetes</text>
    <text x="520" y="550" class="value">System Architecture • Performance Tuning</text>

    <text x="880" y="500" class="section-title" fill="#a855f7">🎵 Hobbies</text>
    <text x="880" y="525" class="value">🎮 Gaming      🎧 Music</text>
    <text x="880" y="550" class="value">✈️ Travel      📚 Books</text>

    <line x1="20" y1="575" x2="1170" y2="575" stroke-dasharray="0"/>

    <!-- Bottom Section: Stats & Connect -->
    <!-- GitHub Stats -->
    <text x="30" y="605" class="section-title" fill="#22c55e">💚 GitHub Stats</text>
    
    <!-- Repos -->
    <rect x="30" y="615" width="125" height="50" fill="{box_bg}" rx="6" stroke="{border_color}" stroke-width="1"/>
    <text x="40" y="632" class="box-title">📦 Repositories</text>
    <text x="40" y="655" class="box-val" fill="#22c55e">95</text>
    <text x="95" y="655" class="box-sub">Contributed: 133</text>
    
    <!-- Commits -->
    <rect x="170" y="615" width="125" height="50" fill="{box_bg}" rx="6" stroke="{border_color}" stroke-width="1"/>
    <text x="180" y="632" class="box-title">🔄 Commits</text>
    <text x="180" y="655" class="box-val" fill="#3b82f6">1,138</text>
    <text x="240" y="655" class="box-sub">Total Commits</text>
    
    <!-- Stars -->
    <rect x="310" y="615" width="125" height="50" fill="{box_bg}" rx="6" stroke="{border_color}" stroke-width="1"/>
    <text x="320" y="632" class="box-title">⭐ Stars</text>
    <text x="320" y="655" class="box-val" fill="#eab308">342</text>
    <text x="375" y="655" class="box-sub">Total Stars</text>
    
    <!-- Followers -->
    <rect x="450" y="615" width="125" height="50" fill="{box_bg}" rx="6" stroke="{border_color}" stroke-width="1"/>
    <text x="460" y="632" class="box-title">👥 Followers</text>
    <text x="460" y="655" class="box-val" fill="#ec4899">196</text>
    <text x="505" y="655" class="box-sub">Across Repos</text>
    
    <!-- LoC -->
    <rect x="590" y="615" width="170" height="50" fill="{box_bg}" rx="6" stroke="{border_color}" stroke-width="1"/>
    <text x="600" y="632" class="box-title">&lt;/&gt; Lines of Code</text>
    <text x="600" y="655" class="box-val" fill="#f97316">523,178+</text>
    
    <!-- Connect -->
    <text x="790" y="605" class="section-title" fill="#2dd4bf">🤝 Let's Connect</text>
    <text x="790" y="630" class="label">✉️ Email</text><text x="875" y="630" class="value">: divyanshjoshidev@gmail.com</text>
    <text x="790" y="650" class="label">🔗 GitHub</text><text x="875" y="650" class="value">: github.com/oldregime</text>
</svg>
"""
    return svg

with open('/mnt/personal file/from w11/github/oldregime_readme/dark_mode.svg', 'w', encoding='utf-8') as f:
    f.write(get_svg(True))
with open('/mnt/personal file/from w11/github/oldregime_readme/light_mode.svg', 'w', encoding='utf-8') as f:
    f.write(get_svg(False))

print("Created SVGs with new ASCII art and updated exact stats!")
