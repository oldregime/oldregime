import re

ascii_art = """        ██████╗ ██╗██╗   ██╗██╗   ██╗ █████╗ ███╗   ██╗███████╗██╗  ██╗
        ██╔══██╗██║██║   ██║╚██╗ ██╔╝██╔══██╗████╗  ██║██╔════╝██║  ██║
        ██║  ██║██║██║   ██║ ╚████╔╝ ███████║██╔██╗ ██║███████╗███████║
        ██║  ██║██║╚██╗ ██╔╝  ╚██╔╝  ██╔══██║██║╚██╗██║╚════██║██╔══██║
        ██████╔╝██║ ╚████╔╝    ██║   ██║  ██║██║ ╚████║███████║██║  ██║
        ╚═════╝ ╚═╝  ╚═══╝     ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝"""

text_lines = """oldregime@github --------------------------------------------------------------

.OS..................................... Arch Linux • Windows 11 • Android 16
.Host................................... VIT Bhopal University
.Role................................... Software Engineer | AI Engineer
.Editor................................. VS Code • JetBrains • Neovim
.Terminal............................... Kitty • Bash • PowerShell

.Languages.Programming................. Python • C++ • JavaScript • TypeScript
.Languages.Web......................... React • Node.js • HTML • CSS
.Languages.Database.................... PostgreSQL • MongoDB • SQLite
.Languages.DevOps...................... Docker • Git • Linux • Nginx
.Languages.AI.......................... PyTorch • TensorFlow • LangChain

.Interests.Software.................... AI • Self Hosting • Linux • Automation
.Interests.Hardware.................... Homelab • Networking • Custom ROMs

----------------------------------------- Contact

.Email.................................. divyanshjoshidev@gmail.com
.GitHub................................. github.com/oldregime
.LinkedIn............................... linkedin.com/in/divyansh-joshi

----------------------------------------- Current Focus

.Building............................... PeerStore
.Working On............................. AI Agents • RAG • LLMs
.Learning............................... Kubernetes • AWS • MLOps
.Looking For............................ Open Source & SWE Opportunities

----------------------------------------- GitHub

.Repos................................. Public Projects
.Commits............................... Daily
.Contributions......................... Always Green 🌱""".split('\n')


def get_svg(is_dark):
    bg_color = "#0d1117" if is_dark else "#f6f8fa"
    if is_dark:
        css = """
        .key { fill: #e3b341; }
        .value { fill: #a5d6ff; }
        .cc { fill: #8b949e; }
        .ascii { fill: #a5d6ff; font-weight: bold; }
        """
    else:
        css = """
        .key { fill: #953800; }
        .value { fill: #0a3069; }
        .cc { fill: #8c959f; }
        .ascii { fill: #0a3069; font-weight: bold; }
        """
        
    svg = f"""<?xml version='1.0' encoding='UTF-8'?>
<svg xmlns="http://www.w3.org/2000/svg" font-family="ConsolasFallback,Consolas,monospace" width="850px" height="920px" font-size="15px">
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
<rect width="850px" height="920px" fill="{bg_color}" rx="15"/>
<text>
"""
    
    y = 50
    for line in ascii_art.split('\n'):
        safe_line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        svg += f'<tspan x="40" y="{y}" class="ascii">{safe_line}</tspan>\n'
        y += 20
        
    y += 20
    
    for line in text_lines:
        if not line.strip():
            y += 20
            continue
            
        safe_line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        
        # Parse patterns
        if safe_line.startswith('.'):
            m = re.match(r'^(\.)(.*?)((\.\.)+\.*)\s*(.*)$', safe_line)
            if m:
                svg += f'<tspan x="40" y="{y}"><tspan class="cc">.</tspan><tspan class="key">{m.group(2)}</tspan><tspan class="cc">{m.group(3)} </tspan><tspan class="value">{m.group(5)}</tspan></tspan>\n'
            else:
                svg += f'<tspan x="40" y="{y}"><tspan class="value">{safe_line}</tspan></tspan>\n'
        elif safe_line.startswith('oldregime@github'):
            svg += f'<tspan x="40" y="{y}"><tspan class="key">oldregime@github </tspan><tspan class="cc">--------------------------------------------------------------</tspan></tspan>\n'
        elif safe_line.startswith('---'):
            m = re.match(r'^(-+)\s*(.*)$', safe_line)
            if m:
                svg += f'<tspan x="40" y="{y}"><tspan class="cc">{m.group(1)} </tspan><tspan class="key">{m.group(2)}</tspan></tspan>\n'
        else:
            svg += f'<tspan x="40" y="{y}"><tspan class="value">{safe_line}</tspan></tspan>\n'
            
        y += 20

    svg += """
</text>
</svg>
"""
    return svg

with open('/mnt/personal file/from w11/github/oldregime_readme/terminal_dark.svg', 'w', encoding='utf-8') as f:
    f.write(get_svg(True))
with open('/mnt/personal file/from w11/github/oldregime_readme/terminal_light.svg', 'w', encoding='utf-8') as f:
    f.write(get_svg(False))
