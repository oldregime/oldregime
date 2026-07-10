import re

ascii_art = """                ⣀⠤⠒⠑⠢⢄
            ⢀⠠⠐⠉      ⠈⠐⠠⢀
          ⢰⠈              ⣈⢶
          ⢸           ⡀  ⠉ ⢸
          ⣿⢸⠑⠲⠉⢲   ⡠⠔⠈     ⢸
          ⢸⢠⣜⡀ ⠈⠒⠤⡀⠁       ⢸
          ⢸⢬⡙⠻⣄⣠⣄⣀⠁⣄       ⠸
         ⡠⢺⡀⠈⠑⠉⢸⠛⠿⡏⡞   ⣤⡆  ⢠
      ⢀⡔⠊  ⢈⡱ ⠱ ⠉⠒ ⠇   ⣩⠵⢔⠊⠁
      ⢸⠈⠑⢤⡖⠁ ⢀⣼⠉⠒⣤⣀⣀⡠⠔⣭⣤⠖⡍⡇
      ⠘⢄⡠⠠ ⡠⠒⠁⣼⠒⠩ ⢀⡡⠔⠊⠹⣿ ⢀⡇
      ⣀⠤⠊⠉⠙⠢⢄⡀⢧⠑⠲⠚⠕   ⣠⣿⠊⠁
     ⡟⠢      ⢈⡙⢄⡈⠇⣀⠤⢲⣿⣿⣿
     ⣹⣷⡀⢄⠁⠂⡔⠊⠁ ⢸⡿⠋⠈⠑⢾⣿⡿⢇⠁⠂⢄
  ⡤⣒⡫⠄⠉⠃⠄⣸⣶⡇   ⠚ ⠛⠛⣰⣿⠟⠉⠁ ⢘⣻
  ⡧⣀⠁⠂⠄⣤⠢⣌⢽⡇⠁⢀⡄⠚⡶⣶⣾⡿⠋ ⡠⠔⠊⠇⢸
  ⠳⢄⡉⠒⠤⣀⣏⡠⢼⡇ ⢸⣿⣿⣿⣟⣉⢤⠂⠁    ⢸
    ⠈⣷⣦⣄⣯⣤⠚⡇ ⠸⠿⢿⣿⡟⡧⠚      ⢸
     ⠙⢿⢿⣿⠿ ⣇⠤⠒⠁ ⢸ ⠇       ⢸
      ⠈⠁                  ⠈⠁
       ⠈⠂⢄⡀      ⠑⠂ ⣀⡤⠒⠁
          ⠈⠑⠢⢄⡀ ⣀⡠⠔⢻⡄⡇
              ⠈⡋⢸  ⢸⠇⡇
         ⢠⠔⠊⡉⠑⠊⢩⡾  ⢸⡇⡇
          ⠉⠒⠤⣐⠒⠄⡉⠒⠖⠊⡲⠇
              ⠈⠚⢤⣀⠂⣤⠍⠂"""

sys_info = """dj@loqfedora
host    82XT (LOQ 15APH8)
os      Fedora Linux 44 (KDE Plasma Desktop Edition) x86_64
de      KWin (Wayland)
disp    1920x1080 @ 1.25x in 16", 120 Hz [Built-in]
pkgs    2981
shell   zsh 5.9
cpu     AMD Ryzen 7 7840HS (16) @ 3.80 GHz - 39.9°C
gpu     NVIDIA GeForce RTX 4050 Laptop GPU - 40.0°C
gpu     AMD Radeon 780M Graphics - 40.0°C
kernel  Linux 7.0.12-201.fc44.x86_64
uptime  2h 55m
os age  22 days
memory  10.71 GiB / 14.80 GiB (72%)
● ● ● ● ● ● ● ●"""

def generate_svg():
    width = 1100
    height = 540
    
    # Catppuccin Macchiato Palette
    bg = "#1e1e2e"
    box_bg = "#181825"
    text_color = "#cad3f5"
    accent1 = "#8aadf4" # Blue
    accent2 = "#a6da95" # Green
    accent3 = "#f5a97f" # Peach
    accent4 = "#c6a0f6" # Mauve
    border = "#363a4f"

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
    <style>
        .title {{ font: bold 32px 'Segoe UI', Ubuntu, sans-serif; fill: {accent1}; }}
        .subtitle {{ font: 600 16px 'Segoe UI', Ubuntu, sans-serif; fill: {accent2}; }}
        .terminal {{ font: 13px 'Fira Code', Consolas, monospace; fill: {text_color}; }}
        .label {{ font: bold 14px 'Segoe UI', Ubuntu, sans-serif; fill: {accent4}; }}
        .value {{ font: 14px 'Segoe UI', Ubuntu, sans-serif; fill: {text_color}; }}
        .braille {{ font: 12px Consolas, monospace; fill: {accent1}; }}
        .key {{ fill: {accent3}; font-weight: bold; }}
    </style>
    
    <!-- Background -->
    <rect width="{width}" height="{height}" fill="{bg}" rx="15" stroke="{border}" stroke-width="2"/>
    
    <!-- Terminal Window -->
    <rect x="25" y="25" width="550" height="490" fill="{box_bg}" rx="10" stroke="{border}" stroke-width="1"/>
    <!-- Mac Buttons -->
    <circle cx="45" cy="45" r="6" fill="#ed8796"/>
    <circle cx="65" cy="45" r="6" fill="#eed49f"/>
    <circle cx="85" cy="45" r="6" fill="#a6da95"/>
    <text x="300" y="50" class="terminal" fill="#8087a2" text-anchor="middle">dj@loqfedora:~</text>
    <line x1="25" y1="65" x2="575" y2="65" stroke="{border}" stroke-width="1"/>
    """

    # Add ASCII Art
    y = 90
    for line in ascii_art.split('\n'):
        # Escape HTML chars
        safe_line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        svg += f'<text x="35" y="{y}" class="braille" xml:space="preserve">{safe_line}</text>\n'
        y += 14

    # Add Sys Info
    y = 90
    for line in sys_info.split('\n'):
        if line.startswith('dj@loqfedora'):
            svg += f'<text x="210" y="{y}" class="terminal" font-weight="bold" fill="{accent1}">dj</text>'
            svg += f'<text x="225" y="{y}" class="terminal" font-weight="bold" fill="{text_color}">@</text>'
            svg += f'<text x="235" y="{y}" class="terminal" font-weight="bold" fill="{accent4}">loqfedora</text>\n'
            y += 16
            svg += f'<text x="210" y="{y}" class="terminal" fill="#8087a2">------------</text>\n'
            y += 16
            continue
            
        if line.startswith('●'):
            colors = ["#ed8796", "#a6da95", "#eed49f", "#8aadf4", "#f5bde6", "#8bd5ca", "#f4dbd6", "#a5adcb"]
            svg += f'<text x="210" y="{y}" class="terminal">'
            for i, c in enumerate(colors):
                svg += f'<tspan fill="{c}">● </tspan>'
            svg += '</text>\n'
            y += 16
            continue

        parts = line.split(' ', 1)
        if len(parts) == 2:
            key = parts[0].strip()
            val = parts[1].strip()
            # If the key is empty because of spacing, handle it
            if not key and val:
                key = val.split()[0]
                val = ' '.join(val.split()[1:])
            
            svg += f'<text x="210" y="{y}" class="terminal" xml:space="preserve"><tspan class="key">{key.ljust(6)}</tspan> <tspan>{val}</tspan></text>\n'
        y += 16

    # Right Side Content
    svg += f"""
    <text x="605" y="65" class="title">Divyansh Joshi</text>
    <text x="605" y="95" class="subtitle">Computer Science Student • AI Developer • Linux Enthusiast</text>
    
    <!-- Tech Stack Box -->
    <rect x="605" y="125" width="465" height="180" fill="{box_bg}" rx="8" stroke="{border}" stroke-width="1"/>
    <text x="625" y="155" class="subtitle" fill="{accent1}">💻 Tech Stack</text>
    
    <text x="625" y="185" class="value"><tspan class="label">Languages  :</tspan> C++, Python, JavaScript</text>
    <text x="625" y="210" class="value"><tspan class="label">AI / ML    :</tspan> LangGraph, Large Language Models</text>
    <text x="625" y="235" class="value"><tspan class="label">Sys &amp; Infra:</tspan> Proxmox, TrueNAS, ZFS RAID, Linux</text>
    <text x="625" y="260" class="value"><tspan class="label">Hardware   :</tspan> ESP32 Embedded Systems</text>
    <text x="625" y="285" class="value"><tspan class="label">Networking :</tspan> Zero-trust architectures</text>
    
    <!-- Connect Box -->
    <rect x="605" y="325" width="465" height="190" fill="{box_bg}" rx="8" stroke="{border}" stroke-width="1"/>
    <text x="625" y="355" class="subtitle" fill="{accent1}">🔗 Connect &amp; Info</text>
    
    <text x="625" y="390" class="value"><tspan class="label">Education  :</tspan> B.Tech CS @ Vellore Institute of Technology</text>
    <text x="625" y="420" class="value"><tspan class="label">Email      :</tspan> divyanshjoshidev@gmail.com</text>
    <text x="625" y="450" class="value"><tspan class="label">GitHub     :</tspan> github.com/oldregime</text>
    <text x="625" y="480" class="value"><tspan class="label">LinkedIn   :</tspan> linkedin.com/in/divyanshjoshidev</text>
    """
    
    svg += "</svg>"
    
    with open('/mnt/personal file/from w11/github/oldregime_readme/profile.svg', 'w', encoding='utf-8') as f:
        f.write(svg)

generate_svg()
