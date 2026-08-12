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

def get_isometric_graph_b64():
    url = "https://isometric-contributions-spectrewolf8.onrender.com/api/graph?username=oldregime&theme=dark"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req).read()
    return base64.b64encode(response).decode('utf-8')

def generate_svg():
    with open("jason_chat.svg", "r", encoding="utf-8") as f:
        svg = f.read()

    day = datetime.datetime.now().strftime("%A")
    weather_str = get_weather()
    iso_b64 = get_isometric_graph_b64()

    # Msg 1
    svg = re.sub(r'<text x="15" y="27">Hi, I\'m Jason</text>', r'<text x="15" y="27">Hi, I\'m Divyansh</text>', svg)
    
    # Msg 2
    svg = re.sub(r'<text x="15" y="27">I live in Columbus, Ohio where it’s supposed to be</text>', r'<text x="15" y="27">I live in Indore, India where it’s supposed to be</text>', svg)
    svg = re.sub(r'<text x="15" y="50">80° F \(27° C\) and <tspan class="emoji">🌧</tspan> today.</text>', f'<text x="15" y="50">{weather_str}</text>', svg)
    
    # Msg 3
    svg = re.sub(r'<text x="15" y="27">I’m a product designer. I used to work at GitHub,</text>', r'<text x="15" y="27">I’m a CS Engineer. I build high-performance</text>', svg)
    svg = re.sub(r'<text x="15" y="50">but I’ve been at PlanetScale for over 5 years now.</text>', r'<text x="15" y="50">systems, distributed storage, and AI pipelines.</text>', svg)
    
    # Msg 4
    svg = re.sub(r'<text x="15" y="27">My favorite project is isometric-contributions. It’s a </text>', r'<text x="15" y="27">I love Self-Hosting and Linux Distro hopping.</text>', svg)
    svg = re.sub(r'<text x="15" y="50">browser extension that shows your GitHub </text>', r'<text x="15" y="50">Here is my isometric contribution graph:</text>', svg)
    svg = re.sub(r'<text x="15" y="73">contributions like this</text>', r'', svg)
    
    # Replace Jason's image with Divyansh's generated base64 image
    # Note: Jason's image has height="258" width="440". We will keep the same dimensions.
    svg = re.sub(r'(<image[^>]*xlink:href="data:image/png;base64,)[^"]+(")', rf'\g<1>{iso_b64}\g<2>', svg)
    
    # The bubble height for msg-4 was 363. The text is now 2 lines instead of 3. We can shift the image up slightly and reduce bubble height by 23px.
    # New image Y = 70. New bubble height = 340.
    svg = re.sub(r'<image x="15" y="90"', r'<image x="15" y="70"', svg)
    svg = re.sub(r'(<g[^>]*class="msg-4"[^>]*>\s*<rect[^>]*)height="363"', r'\1height="340"', svg)
    
    # Msg 5
    svg = re.sub(r'<text x="15" y="27">You can find me on Bluesky at</text>', r'<text x="15" y="27">You can get in touch with me on email at</text>', svg)
    svg = re.sub(r'<a xlink:href="https://bsky.app/profile/jasonlong.me">https://bsky.app/profile/jasonlong.me</a>', r'<a xlink:href="mailto:divyanshjoshidev@gmail.com">divyanshjoshidev@gmail.com</a>', svg)
    
    # Adjust msg-5 bubble width to fit the email address text (width 390 instead of 350)
    svg = re.sub(r'(<g[^>]*class="msg-5"[^>]*>\s*<rect[^>]*)width="350"', r'\1width="390"', svg)
    
    # Adjust Y coordinates for subsequent animations and bubbles since we shrank msg-4 by 23px
    # 560 - 23 = 537
    # 632 - 23 = 609
    svg = re.sub(r'translate\(10, 560\)', r'translate(10, 537)', svg)
    svg = re.sub(r'translate\(10, 632\)', r'translate(10, 609)', svg)
    svg = re.sub(r'translate\(10px, 565px\)', r'translate(10px, 542px)', svg)
    svg = re.sub(r'translate\(10px, 560px\)', r'translate(10px, 537px)', svg)
    svg = re.sub(r'translate\(10px, 637px\)', r'translate(10px, 614px)', svg)
    svg = re.sub(r'translate\(10px, 632px\)', r'translate(10px, 609px)', svg)
    
    # Change total SVG height (original 684 - 23 = 661)
    svg = re.sub(r'height="684"', r'height="661"', svg)
    svg = re.sub(r'viewBox="0 0 550 684"', r'viewBox="0 0 550 661"', svg)
    
    # Msg 6
    svg = re.sub(r'<text x="15" y="27">Have a great Wednesday! <tspan class="emoji">✌🏻</tspan></text>', f'<text x="15" y="27">Have a great {day}! <tspan class="emoji">✌🏻</tspan></text>', svg)

    with open("chat.svg", "w", encoding="utf-8") as f:
        f.write(svg)
        
    print("Successfully generated chat.svg")

if __name__ == "__main__":
    generate_svg()
