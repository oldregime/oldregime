import html

# Andrew6rant exact SVG specs:
# width=985px, height=530px, font-size=16px, font-family="ConsolasFallback,Consolas,monospace"
# rx=15
# y steps = 20px (30, 50, 70, 90, 110, 130, 150, 170, 190, 210, 230, 250, 270, 290, 310, 330, 350, 370, 390, 410, 430, 450, 470, 490, 510)

ascii_dark = [
"           g@M%@%%@N%Nw,,                   ",
"        ,M*|`||*%gNM=]mM%g||%N,             ",
"       p!``  '! |''` '''|||jhlj%w           ",
"     ,@L `    ,,        ''!`|j%M]%M         ",
"    ]j'` .,wp@pw,    `.     ''''|%Wg       ",
"  /{||]@@@@@@@@@pp.             |||||      ",
" '` ']@@@@@@@@@@@@@@p     , ,'''` `        ",
"  , :]%%@@@@@%%%%%%k%h '*||mkr     *       ",
"  '  j%M`      |jkk'   ~nrn=|i    ;`       ",
"   !  jrr*^`             `\"!  L'':!   ",
"    j  lp;,.  ,/ @@    ,;\\nmy \"  ,~   ",
"   i r @@@@mmHM @@@@ `^****M*,p ;,         ",
"   | ]@@@@HHH]g@M%%%%%H,jmgpmb%  j         ",
"    ;;%%%%%k%@[,.n|;.;j%%k|%k%%',[         ",
"     H|%%k%%%j%k||,;;j;!!'|%ij}]@          ",
"     \"djjmkL,\"]][,,,,wwxw;|#kjk` ",
"       %;%km%%%%M%M|%%jkkii|||[            ",
"        kjj%%kkkl|!||||||j|||\"        ",
"         |jm%H@@@b%%kkmk%i|!,[             ",
"         @p|j%%%%jkk|||j*'`;j[             ",
"        ]@@@g|'''`'''  ` ,;j%k             ",
"        @@@@@mgmp;,,,,:;jj%%k%             ",
"       @@@@@@@@%%kgki!|jjjj%k%@ .          ",
". ^['' %@@@@HH%b%k{illljkjj%%%% ; `,.",
"=[' ` . %HH%%%%%H@gkilljjj%kk%\".   `'i"
]

ascii_light = [
"            ;;,, ,;,|g;~,,                      ",
"         ,g@@@@@@l&$$$@|,w$$@gy,            ",
"        $@@@@@@@@@@$@@@@@@@@$$MW$k              ",
"       $$@@@@@@B@@@@@@@@@@@@@$@$$g,$            ",
"     g@llM**'''||%@@@@@$@@$@@@@@@@L$&           ",
"   @&$F         ''T%M$@@@@@@@@@@@$@$@     ",
"  @@@@F              ']@@@@@@$$@$@@@@          ",
"  @@@$L               |$@@@$$l$@@@@$F          ",
" ]@@@@L ,@@$@@@@L  ,l@$$$$$$$$$@@@@@           ",
"  %$@@@}',,gg@||@@@@l@g@ggg|l&$@$$       ",
"  ]@@@@@'\"*TTTTT'F  ]Wl|||'\"'$]@@@@ ",
"   $$@M$       ,#    ]gg,,,,,.r'$@$            ",
"    &$L        ' ,, ,,,'T'`    $$L        ",
"     lL         T\"||||!   `-    l\"'  ",
"     ' |        '||l||||\"|L|  L `         ",
"      ''   '|L++=*****\"\"*\"||` L|",
"        |           ,,      |||F               ",
"        '         |||||||| ||l$                ",
"          !                |l&L            ",
"           '!,       |||,||@M|L                ",
"            ||l&$@$$@$$$@$MT|||            ",
"         |    |||lll$$llll|||||L               ",
"    ,;y@        ||||||l||@|||||l               ",
",g$@$$$@         |||||||||||||||| $g,          ",
"$$$$$$$$@    |    |||||||||||||| |$$@g         "
]

def make_dark_svg():
    return f"""<?xml version='1.0' encoding='UTF-8'?>
<svg xmlns="http://www.w3.org/2000/svg" font-family="ConsolasFallback,Consolas,monospace" width="985px" height="530px" font-size="16px">
<style>
@font-face {{
src: local('Consolas'), local('Consolas Bold');
font-family: 'ConsolasFallback';
font-display: swap;
-webkit-size-adjust: 109%;
size-adjust: 109%;
}}
.key {{fill: #ffa657;}}
.value {{fill: #a5d6ff;}}
.addColor {{fill: #3fb950;}}
.delColor {{fill: #f85149;}}
.cc {{fill: #616e7f;}}
text, tspan {{white-space: pre;}}
</style>
<rect width="985px" height="530px" fill="#161b22" rx="15"/>
<text x="15" y="30" fill="#c9d1d9" class="ascii">
<tspan x="15" y="30">{html.escape(ascii_dark[0])}</tspan>
<tspan x="15" y="50">{html.escape(ascii_dark[1])}</tspan>
<tspan x="15" y="70">{html.escape(ascii_dark[2])}</tspan>
<tspan x="15" y="90">{html.escape(ascii_dark[3])}</tspan>
<tspan x="15" y="110">{html.escape(ascii_dark[4])}</tspan>
<tspan x="15" y="130">{html.escape(ascii_dark[5])}</tspan>
<tspan x="15" y="150">{html.escape(ascii_dark[6])}</tspan>
<tspan x="15" y="170">{html.escape(ascii_dark[7])}</tspan>
<tspan x="15" y="190">{html.escape(ascii_dark[8])}</tspan>
<tspan x="15" y="210">{html.escape(ascii_dark[9])}</tspan>
<tspan x="15" y="230">{html.escape(ascii_dark[10])}</tspan>
<tspan x="15" y="250">{html.escape(ascii_dark[11])}</tspan>
<tspan x="15" y="270">{html.escape(ascii_dark[12])}</tspan>
<tspan x="15" y="290">{html.escape(ascii_dark[13])}</tspan>
<tspan x="15" y="310">{html.escape(ascii_dark[14])}</tspan>
<tspan x="15" y="330">{html.escape(ascii_dark[15])}</tspan>
<tspan x="15" y="350">{html.escape(ascii_dark[16])}</tspan>
<tspan x="15" y="370">{html.escape(ascii_dark[17])}</tspan>
<tspan x="15" y="390">{html.escape(ascii_dark[18])}</tspan>
<tspan x="15" y="410">{html.escape(ascii_dark[19])}</tspan>
<tspan x="15" y="430">{html.escape(ascii_dark[20])}</tspan>
<tspan x="15" y="450">{html.escape(ascii_dark[21])}</tspan>
<tspan x="15" y="470">{html.escape(ascii_dark[22])}</tspan>
<tspan x="15" y="490">{html.escape(ascii_dark[23])}</tspan>
<tspan x="15" y="510">{html.escape(ascii_dark[24])}</tspan>
</text>
<text x="390" y="30" fill="#c9d1d9">
<tspan x="390" y="30">divyansh@joshi</tspan> -———————————————————————————————————————————-—-
<tspan x="390" y="50" class="cc">. </tspan><tspan class="key">OS</tspan>:<tspan class="cc"> ........................ </tspan><tspan class="value">Fedora Linux 44, Windows 11, Wayland</tspan>
<tspan x="390" y="70" class="cc">. </tspan><tspan class="key">Host</tspan>:<tspan class="cc"> ....................... </tspan><tspan class="value">Systems &amp; AI Engineer</tspan>
<tspan x="390" y="90" class="cc">. </tspan><tspan class="key">Hardware</tspan>:<tspan class="cc"> ................... </tspan><tspan class="value">AMD Ryzen 7 7840HS, NVIDIA RTX 4050</tspan>
<tspan x="390" y="110" class="cc">. </tspan><tspan class="key">Kernel</tspan>:<tspan class="cc"> ..................... </tspan><tspan class="value">AI Pipelines &amp; P2P Storage Systems</tspan>
<tspan x="390" y="130" class="cc">. </tspan><tspan class="key">IDE</tspan>:<tspan class="cc"> ........................ </tspan><tspan class="value">VSCode, Neovim, Rust-Analyzer</tspan>
<tspan x="390" y="150" class="cc">. </tspan>
<tspan x="390" y="170" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Programming</tspan>:<tspan class="cc"> ..... </tspan><tspan class="value">Rust, C++, Python, TypeScript, WASM</tspan>
<tspan x="390" y="190" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">AI_ML</tspan>:<tspan class="cc"> ........... </tspan><tspan class="value">PyTorch, LangGraph, Llama 3, HiFi-GAN</tspan>
<tspan x="390" y="210" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Systems</tspan>:<tspan class="cc"> ......... </tspan><tspan class="value">Tokio, Raft Consensus, Linux, Docker</tspan>
<tspan x="390" y="230" class="cc">. </tspan>
<tspan x="390" y="250" class="cc">. </tspan><tspan class="key">Hobbies</tspan>.<tspan class="key">Software</tspan>:<tspan class="cc"> .... </tspan><tspan class="value">AI Agents, Self-hosting, WASM</tspan>
<tspan x="390" y="270" class="cc">. </tspan><tspan class="key">Hobbies</tspan>.<tspan class="key">Hardware</tspan>:<tspan class="cc"> ............. </tspan><tspan class="value">Fedora Wayland, Systems Tuning</tspan>
<tspan x="390" y="310">- Contact</tspan> -——————————————————————————————————————————————-—-
<tspan x="390" y="330" class="cc">. </tspan><tspan class="key">Email</tspan>:<tspan class="cc"> ....................... </tspan><tspan class="value">divyanshjoshidev@gmail.com</tspan>
<tspan x="390" y="350" class="cc">. </tspan><tspan class="key">Portfolio</tspan>:<tspan class="cc"> .................... </tspan><tspan class="value">https://oldregime.github.io/</tspan>
<tspan x="390" y="370" class="cc">. </tspan><tspan class="key">LinkedIn</tspan>:<tspan class="cc"> ..................... </tspan><tspan class="value">in/divyanshjoshidev</tspan>
<tspan x="390" y="390" class="cc">. </tspan><tspan class="key">Discord</tspan>:<tspan class="cc"> ...................... </tspan><tspan class="value">theoldregime</tspan>
<tspan x="390" y="410" class="cc">. </tspan><tspan class="key">Medium</tspan>:<tspan class="cc"> ....................... </tspan><tspan class="value">theoldregime.medium.com</tspan>
<tspan x="390" y="450">- GitHub Stats</tspan> -—————————————————————————————————————————-—-
<tspan x="390" y="470" class="cc">. </tspan><tspan class="key">Repos</tspan>:<tspan class="cc" id="repo_data_dots"> .... </tspan><tspan class="value" id="repo_data">53</tspan> {{<tspan class="key">Contributed</tspan>: <tspan class="value" id="contrib_data">18</tspan>}} | <tspan class="key">Stars</tspan>:<tspan class="cc" id="star_data_dots"> ........... </tspan><tspan class="value" id="star_data">12</tspan>
<tspan x="390" y="490" class="cc">. </tspan><tspan class="key">Commits</tspan>:<tspan class="cc" id="commit_data_dots"> ................. </tspan><tspan class="value" id="commit_data">1,000+</tspan> | <tspan class="key">CP Rating</tspan>:<tspan class="cc" id="follower_data_dots"> ....... </tspan><tspan class="value" id="follower_data">1700+</tspan>
<tspan x="390" y="510" class="cc">. </tspan><tspan class="key">Lines of Code on GitHub</tspan>:<tspan class="cc" id="loc_data_dots">. </tspan><tspan class="value" id="loc_data">1,604,865</tspan> ( <tspan class="addColor" id="loc_add">1,724,227</tspan><tspan class="addColor">++</tspan>, <tspan id="loc_del_dots"> </tspan><tspan class="delColor" id="loc_del">119,362</tspan><tspan class="delColor">--</tspan> )
</text>
</svg>"""

def make_light_svg():
    return f"""<?xml version='1.0' encoding='UTF-8'?>
<svg xmlns="http://www.w3.org/2000/svg" font-family="ConsolasFallback,Consolas,monospace" width="985px" height="530px" font-size="16px">
<style>
@font-face {{
src: local('Consolas'), local('Consolas Bold');
font-family: 'ConsolasFallback';
font-display: swap;
-webkit-size-adjust: 109%;
size-adjust: 109%;
}}
.key {{fill: #953800;}}
.value {{fill: #0a3069;}}
.addColor {{fill: #1a7f37;}}
.delColor {{fill: #cf222e;}}
.cc {{fill: #c2cfde;}}
text, tspan {{white-space: pre;}}
</style>
<rect width="985px" height="530px" fill="#f6f8fa" rx="15"/>
<text x="15" y="30" fill="#24292f" class="ascii">
<tspan x="15" y="30">{html.escape(ascii_light[0])}</tspan>
<tspan x="15" y="50">{html.escape(ascii_light[1])}</tspan>
<tspan x="15" y="70">{html.escape(ascii_light[2])}</tspan>
<tspan x="15" y="90">{html.escape(ascii_light[3])}</tspan>
<tspan x="15" y="110">{html.escape(ascii_light[4])}</tspan>
<tspan x="15" y="130">{html.escape(ascii_light[5])}</tspan>
<tspan x="15" y="150">{html.escape(ascii_light[6])}</tspan>
<tspan x="15" y="170">{html.escape(ascii_light[7])}</tspan>
<tspan x="15" y="190">{html.escape(ascii_light[8])}</tspan>
<tspan x="15" y="210">{html.escape(ascii_light[9])}</tspan>
<tspan x="15" y="230">{html.escape(ascii_light[10])}</tspan>
<tspan x="15" y="250">{html.escape(ascii_light[11])}</tspan>
<tspan x="15" y="270">{html.escape(ascii_light[12])}</tspan>
<tspan x="15" y="290">{html.escape(ascii_light[13])}</tspan>
<tspan x="15" y="310">{html.escape(ascii_light[14])}</tspan>
<tspan x="15" y="330">{html.escape(ascii_light[15])}</tspan>
<tspan x="15" y="350">{html.escape(ascii_light[16])}</tspan>
<tspan x="15" y="370">{html.escape(ascii_light[17])}</tspan>
<tspan x="15" y="390">{html.escape(ascii_light[18])}</tspan>
<tspan x="15" y="410">{html.escape(ascii_light[19])}</tspan>
<tspan x="15" y="430">{html.escape(ascii_light[20])}</tspan>
<tspan x="15" y="450">{html.escape(ascii_light[21])}</tspan>
<tspan x="15" y="470">{html.escape(ascii_light[22])}</tspan>
<tspan x="15" y="490">{html.escape(ascii_light[23])}</tspan>
<tspan x="15" y="510">{html.escape(ascii_light[24])}</tspan>
</text>
<text x="390" y="30" fill="#24292f">
<tspan x="390" y="30">divyansh@joshi</tspan> -———————————————————————————————————————————-—-
<tspan x="390" y="50" class="cc">. </tspan><tspan class="key">OS</tspan>:<tspan class="cc"> ........................ </tspan><tspan class="value">Fedora Linux 44, Windows 11, Wayland</tspan>
<tspan x="390" y="70" class="cc">. </tspan><tspan class="key">Host</tspan>:<tspan class="cc"> ....................... </tspan><tspan class="value">Systems &amp; AI Engineer</tspan>
<tspan x="390" y="90" class="cc">. </tspan><tspan class="key">Hardware</tspan>:<tspan class="cc"> ................... </tspan><tspan class="value">AMD Ryzen 7 7840HS, NVIDIA RTX 4050</tspan>
<tspan x="390" y="110" class="cc">. </tspan><tspan class="key">Kernel</tspan>:<tspan class="cc"> ..................... </tspan><tspan class="value">AI Pipelines &amp; P2P Storage Systems</tspan>
<tspan x="390" y="130" class="cc">. </tspan><tspan class="key">IDE</tspan>:<tspan class="cc"> ........................ </tspan><tspan class="value">VSCode, Neovim, Rust-Analyzer</tspan>
<tspan x="390" y="150" class="cc">. </tspan>
<tspan x="390" y="170" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Programming</tspan>:<tspan class="cc"> ..... </tspan><tspan class="value">Rust, C++, Python, TypeScript, WASM</tspan>
<tspan x="390" y="190" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">AI_ML</tspan>:<tspan class="cc"> ........... </tspan><tspan class="value">PyTorch, LangGraph, Llama 3, HiFi-GAN</tspan>
<tspan x="390" y="210" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Systems</tspan>:<tspan class="cc"> ......... </tspan><tspan class="value">Tokio, Raft Consensus, Linux, Docker</tspan>
<tspan x="390" y="230" class="cc">. </tspan>
<tspan x="390" y="250" class="cc">. </tspan><tspan class="key">Hobbies</tspan>.<tspan class="key">Software</tspan>:<tspan class="cc"> .... </tspan><tspan class="value">AI Agents, Self-hosting, WASM</tspan>
<tspan x="390" y="270" class="cc">. </tspan><tspan class="key">Hobbies</tspan>.<tspan class="key">Hardware</tspan>:<tspan class="cc"> ............. </tspan><tspan class="value">Fedora Wayland, Systems Tuning</tspan>
<tspan x="390" y="310">- Contact</tspan> -——————————————————————————————————————————————-—-
<tspan x="390" y="330" class="cc">. </tspan><tspan class="key">Email</tspan>:<tspan class="cc"> ....................... </tspan><tspan class="value">divyanshjoshidev@gmail.com</tspan>
<tspan x="390" y="350" class="cc">. </tspan><tspan class="key">Portfolio</tspan>:<tspan class="cc"> .................... </tspan><tspan class="value">https://oldregime.github.io/</tspan>
<tspan x="390" y="370" class="cc">. </tspan><tspan class="key">LinkedIn</tspan>:<tspan class="cc"> ..................... </tspan><tspan class="value">in/divyanshjoshidev</tspan>
<tspan x="390" y="390" class="cc">. </tspan><tspan class="key">Discord</tspan>:<tspan class="cc"> ...................... </tspan><tspan class="value">theoldregime</tspan>
<tspan x="390" y="410" class="cc">. </tspan><tspan class="key">Medium</tspan>:<tspan class="cc"> ....................... </tspan><tspan class="value">theoldregime.medium.com</tspan>
<tspan x="390" y="450">- GitHub Stats</tspan> -—————————————————————————————————————————-—-
<tspan x="390" y="470" class="cc">. </tspan><tspan class="key">Repos</tspan>:<tspan class="cc" id="repo_data_dots"> .... </tspan><tspan class="value" id="repo_data">53</tspan> {{<tspan class="key">Contributed</tspan>: <tspan class="value" id="contrib_data">18</tspan>}} | <tspan class="key">Stars</tspan>:<tspan class="cc" id="star_data_dots"> ........... </tspan><tspan class="value" id="star_data">12</tspan>
<tspan x="390" y="490" class="cc">. </tspan><tspan class="key">Commits</tspan>:<tspan class="cc" id="commit_data_dots"> ................. </tspan><tspan class="value" id="commit_data">1,000+</tspan> | <tspan class="key">CP Rating</tspan>:<tspan class="cc" id="follower_data_dots"> ....... </tspan><tspan class="value" id="follower_data">1700+</tspan>
<tspan x="390" y="510" class="cc">. </tspan><tspan class="key">Lines of Code on GitHub</tspan>:<tspan class="cc" id="loc_data_dots">. </tspan><tspan class="value" id="loc_data">1,604,865</tspan> ( <tspan class="addColor" id="loc_add">1,724,227</tspan><tspan class="addColor">++</tspan>, <tspan id="loc_del_dots"> </tspan><tspan class="delColor" id="loc_del">119,362</tspan><tspan class="delColor">--</tspan> )
</text>
</svg>"""

with open("/mnt/personal file/from w11/github/oldregime_readme/dark_mode.svg", "w") as f:
    f.write(make_dark_svg())

with open("/mnt/personal file/from w11/github/oldregime_readme/light_mode.svg", "w") as f:
    f.write(make_light_svg())

print("Built build_svgs.py successfully!")
