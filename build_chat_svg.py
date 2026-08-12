import datetime
import urllib.request
import re
import json

def get_weather():
    try:
        url = "https://wttr.in/Indore?format=j1"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req).read().decode('utf-8')
        data = json.loads(response)
        current = data['current_condition'][0]
        temp_c = current['temp_C']
        temp_f = current['temp_F']
        desc = current['weatherDesc'][0]['value'].lower()
        
        emoji = "☀️"
        if "rain" in desc or "drizzle" in desc: emoji = "🌧"
        elif "cloud" in desc or "overcast" in desc: emoji = "☁️"
        elif "thunder" in desc: emoji = "⛈"
        elif "snow" in desc: emoji = "❄️"
        elif "fog" in desc or "mist" in desc: emoji = "🌫"
        return f"{temp_f}° F ({temp_c}° C) and <tspan class=\"emoji\">{emoji}</tspan> today."
    except Exception as e:
        return "warm and <tspan class=\"emoji\">☀️</tspan> today."

def generate_svg():
    with open("jason_chat.svg", "r", encoding="utf-8") as f:
        svg = f.read()

    # Day of week
    day = datetime.datetime.now().strftime("%A")
    
    # Weather
    weather_str = get_weather()

    # Replacements
    # Msg 1
    svg = re.sub(r'<text x="15" y="27">Hi, I\'m Jason</text>', r'<text x="15" y="27">Hi, I\'m Divyansh</text>', svg)
    
    # Msg 2
    svg = re.sub(r'<text x="15" y="27">I live in Columbus, Ohio where it’s supposed to be</text>', r'<text x="15" y="27">I live in Indore, India where it’s supposed to be</text>', svg)
    svg = re.sub(r'<text x="15" y="50">80° F \(27° C\) and <tspan class="emoji">🌧</tspan> today.</text>', f'<text x="15" y="50">{weather_str}</text>', svg)
    
    # Msg 3
    svg = re.sub(r'<text x="15" y="27">I’m a product designer. I used to work at GitHub,</text>', r'<text x="15" y="27">I’m a CS Engineer. I build high-performance</text>', svg)
    svg = re.sub(r'<text x="15" y="50">but I’ve been at PlanetScale for over 5 years now.</text>', r'<text x="15" y="50">systems, distributed storage, and AI pipelines.</text>', svg)
    
    # Msg 4 (Jason had 3 lines and an image, we'll replace the text and remove the image, and adjust the bubble size)
    svg = re.sub(r'<text x="15" y="27">My favorite project is isometric-contributions. It’s a </text>', r'<text x="15" y="27">My stats: 1700+ Competitive Rating, 1000+ Commits,</text>', svg)
    svg = re.sub(r'<text x="15" y="50">browser extension that shows your GitHub </text>', r'<text x="15" y="50">and full-stack projects with 40+ live users.</text>', svg)
    svg = re.sub(r'<text x="15" y="73">contributions like this</text>', r'', svg)
    # Remove the image from msg-4 (it's embedded as base64 inside <g class="msg-4">)
    svg = re.sub(r'<image[^>]*href="data:image[^>]*/>', '', svg)
    # The bubble height for msg-4 was 363 (we can see the rect tag). Let's change it to 66
    # We need to find the <rect> inside class="msg-4" and change height.
    # It looks like: <rect width="470" height="363" rx="18" class="bubble" />
    svg = re.sub(r'(<g[^>]*class="msg-4"[^>]*>\s*<rect[^>]*)height="363"', r'\1height="66"', svg)
    svg = re.sub(r'(<g[^>]*class="msg-4"[^>]*>\s*<rect[^>]*)width="470"', r'\1width="470"', svg)
    
    # Adjust Y coordinates for subsequent animations and bubbles since we shrank msg-4
    # The original msg-4 height was 363, new is 66. Difference is 297.
    # We need to translate msg-5, typing-5, msg-6, typing-6 up by 297.
    # Original typing-5 Y=560, msg-5 Y=560. New Y = 560 - 297 = 263.
    # Original typing-6 Y=632, msg-6 Y=632. New Y = 632 - 297 = 335.
    
    svg = re.sub(r'translate\(10, 560\)', r'translate(10, 263)', svg)
    svg = re.sub(r'translate\(10, 632\)', r'translate(10, 335)', svg)
    
    # Also adjust the keyframes for msg-5 and msg-6
    svg = re.sub(r'transform: translate\(10px, 565px\);', r'transform: translate(10px, 268px);', svg)
    svg = re.sub(r'transform: translate\(10px, 560px\);', r'transform: translate(10px, 263px);', svg)
    
    svg = re.sub(r'transform: translate\(10px, 637px\);', r'transform: translate(10px, 340px);', svg)
    svg = re.sub(r'transform: translate\(10px, 632px\);', r'transform: translate(10px, 335px);', svg)

    # Change total SVG height
    svg = re.sub(r'height="684"', r'height="387"', svg)
    svg = re.sub(r'viewBox="0 0 550 684"', r'viewBox="0 0 550 387"', svg)

    # Msg 5
    svg = re.sub(r'<text x="15" y="27">You can find me on Bluesky at</text>', r'<text x="15" y="27">You can find me on GitHub at</text>', svg)
    svg = re.sub(r'<a xlink:href="https://bsky.app/profile/jasonlong.me">https://bsky.app/profile/jasonlong.me</a>', r'<a xlink:href="https://github.com/oldregime">https://github.com/oldregime</a>', svg)
    # The bubble for msg-5 was width=350, let's make it 350 to fit the new text. It's fine.
    
    # Msg 6
    svg = re.sub(r'<text x="15" y="27">Have a great Wednesday! <tspan class="emoji">✌🏻</tspan></text>', f'<text x="15" y="27">Have a great {day}! <tspan class="emoji">✌🏻</tspan></text>', svg)

    with open("chat.svg", "w", encoding="utf-8") as f:
        f.write(svg)
        
    print("Successfully generated chat.svg")

if __name__ == "__main__":
    generate_svg()
