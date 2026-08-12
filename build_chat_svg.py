import datetime
import urllib.request
import re
import json
import base64

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

def get_perry_b64():
    with open('/home/dj/Downloads/Profile_-_Perry_the_Platypus.PNG.webp', 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode('utf-8')

def generate_svg():
    with open("jason_chat.svg", "r", encoding="utf-8") as f:
        svg = f.read()

    day = datetime.datetime.now().strftime("%A")
    weather_str = get_weather()
    perry_b64 = get_perry_b64()

    # Msg 1
    svg = svg.replace('<text x="15" y="27">Hi, I\'m Jason</text>', '<text x="15" y="27">Hi, I am Divyansh</text>')
    svg = re.sub(r'(<g[^>]*class="msg-1 bubble"[^>]*>\s*<rect[^>]*)width="133"', r'\1width="180"', svg)
    
    # Msg 2
    svg = svg.replace('<text x="15" y="27">I live in Columbus, Ohio where it’s supposed to be</text>', '<text x="15" y="27">I live in Indore, India where it’s supposed to be</text>')
    svg = re.sub(r'<text x="15" y="50">80° F \(27° C\) and <tspan class="emoji">🌧</tspan> today.</text>', f'<text x="15" y="50">{weather_str}</text>', svg)
    
    # Msg 3
    svg = svg.replace('<text x="15" y="27">I’m a product designer. I used to work at GitHub,</text>', '<text x="15" y="27">I’m a CS Engineer. I build high-performance</text>')
    svg = svg.replace('<text x="15" y="50">but I’ve been at PlanetScale for over 5 years now.</text>', '<text x="15" y="50">systems, distributed storage, and AI pipelines.</text>')
    
    # Msg 4
    svg = svg.replace('<text x="15" y="27">My favorite project is isometric-contributions. It’s a </text>', '<text x="15" y="27">rather than boring you with my leetcode ,</text>')
    svg = svg.replace('<text x="15" y="50">browser extension that shows your GitHub </text>', '<text x="15" y="50">here is a platypus that is also a detective </text>')
    svg = svg.replace('<text x="15" y="73">contributions like this</text>', '')
    
    # Replace Jason's image with Perry
    svg = re.sub(r'<image\s+[^>]*href="data:image[^>]*>', f'<image x="15" y="70" width="360" height="316" href="data:image/webp;base64,{perry_b64}" />', svg)
    
    # Adjust msg-4 bubble height (70 + 316 + 20 = 406) and width (360 + 30 = 390)
    svg = re.sub(r'(<g[^>]*class="msg-4"[^>]*>\s*<rect[^>]*)width="456"', r'\1width="390"', svg)
    svg = re.sub(r'(<g[^>]*class="msg-4"[^>]*>\s*<rect[^>]*)height="92"', r'\1height="406"', svg)
    
    # Msg 5
    svg = svg.replace('<text x="15" y="27">You can find me on Bluesky at</text>', '<text x="15" y="27">You can get in touch with me on email at</text>')
    svg = svg.replace('<a xlink:href="https://bsky.app/profile/jasonlong.me">https://bsky.app/profile/jasonlong.me</a>', '<a xlink:href="mailto:divyanshjoshidev@gmail.com">divyanshjoshidev@gmail.com</a>')
    svg = re.sub(r'(<g[^>]*class="msg-5"[^>]*>\s*<rect[^>]*)width="350"', r'\1width="415"', svg)
    
    # Recalculate Y positions
    # msg-1: Y=0
    # msg-2: Y=57
    # msg-3: Y=138
    # msg-4: Y=219
    # msg-5: Y = 219 + 406 + 15 = 640
    # msg-6: Y = 640 + 66 + 15 = 721
    
    svg = re.sub(r'translate\(10, 48\)', r'translate(10, 57)', svg)
    svg = re.sub(r'transform: translate\(10px, 53px\);', r'transform: translate(10px, 62px);', svg)
    svg = re.sub(r'transform: translate\(10px, 48px\);', r'transform: translate(10px, 57px);', svg)
    
    svg = re.sub(r'translate\(10, 120\)', r'translate(10, 138)', svg)
    svg = re.sub(r'transform: translate\(10px, 125px\);', r'transform: translate(10px, 143px);', svg)
    svg = re.sub(r'transform: translate\(10px, 120px\);', r'transform: translate(10px, 138px);', svg)
    
    svg = re.sub(r'translate\(10, 192\)', r'translate(10, 219)', svg)
    svg = re.sub(r'transform: translate\(10px, 197px\);', r'transform: translate(10px, 224px);', svg)
    svg = re.sub(r'transform: translate\(10px, 192px\);', r'transform: translate(10px, 219px);', svg)
    
    svg = re.sub(r'translate\(10, 560\)', r'translate(10, 640)', svg)
    svg = re.sub(r'transform: translate\(10px, 565px\);', r'transform: translate(10px, 645px);', svg)
    svg = re.sub(r'transform: translate\(10px, 560px\);', r'transform: translate(10px, 640px);', svg)
    
    svg = re.sub(r'translate\(10, 632\)', r'translate(10, 721)', svg)
    svg = re.sub(r'transform: translate\(10px, 637px\);', r'transform: translate(10px, 726px);', svg)
    svg = re.sub(r'transform: translate\(10px, 632px\);', r'transform: translate(10px, 721px);', svg)

    # Scale SVG
    # Original viewBox 550x684. New height needed: 721 + 42 + 20 = 783.
    # So viewBox="0 0 550 783"
    # width="467" height="665" (approx 85% of 550x783)
    svg = re.sub(r'<svg width="[0-9]*" height="[0-9]*" viewBox="0 0 550 [0-9]*"', r'<svg width="467" height="665" viewBox="0 0 550 783"', svg)

    # Msg 6
    svg = re.sub(r'<text x="15" y="27">Have a great Wednesday! <tspan class="emoji">✌🏻</tspan></text>', f'<text x="15" y="27">Have a great {day}! <tspan class="emoji">✌🏻</tspan></text>', svg)

    with open("chat.svg", "w", encoding="utf-8") as f:
        f.write(svg)
        
    print("Successfully generated chat.svg")

if __name__ == "__main__":
    generate_svg()
