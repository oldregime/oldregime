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
    # Fixing the backslash issue and widening the bubble to 180px
    svg = re.sub(r'<text x="15" y="27">Hi, I\'m Jason</text>', r'<text x="15" y="27">Hi, I\'m Divyansh</text>', svg)
    svg = re.sub(r'(<g[^>]*class="msg-1"[^>]*>\s*<rect[^>]*)width="138"', r'\1width="180"', svg)
    
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
    svg = re.sub(r'(<image[^>]*xlink:href="data:image/png;base64,)[^"]+(")', rf'\g<1>{iso_b64}\g<2>', svg)
    
    # Adjust msg-4 bubble height precisely to enclose the image
    svg = re.sub(r'<image x="15" y="90"', r'<image x="15" y="70"', svg)
    svg = re.sub(r'(<g[^>]*class="msg-4"[^>]*>\s*<rect[^>]*)height="363"', r'\1height="350"', svg)
    
    # Msg 5
    svg = re.sub(r'<text x="15" y="27">You can find me on Bluesky at</text>', r'<text x="15" y="27">You can get in touch with me on email at</text>', svg)
    svg = re.sub(r'<a xlink:href="https://bsky.app/profile/jasonlong.me">https://bsky.app/profile/jasonlong.me</a>', r'<a xlink:href="mailto:divyanshjoshidev@gmail.com">divyanshjoshidev@gmail.com</a>', svg)
    svg = re.sub(r'(<g[^>]*class="msg-5"[^>]*>\s*<rect[^>]*)width="350"', r'\1width="415"', svg)
    
    # Recalculate all Y positions with 15px gap (original gap was 6px)
    # y_msg1 = 0
    # y_msg2 = 57
    # y_msg3 = 138
    # y_msg4 = 219
    # y_msg5 = 219 + 350 + 15 = 584
    # y_msg6 = 584 + 66 + 15 = 665
    
    # Update translate for g tags
    # Original values in jason_chat.svg: 
    # msg-1: (10, 0)
    # msg-2: (10, 48)
    # msg-3: (10, 120)
    # msg-4: (10, 192)
    # msg-5: (10, 560)
    # msg-6: (10, 632)
    
    # Update msg-2
    svg = re.sub(r'translate\(10, 48\)', r'translate(10, 57)', svg)
    svg = re.sub(r'transform: translate\(10px, 53px\);', r'transform: translate(10px, 62px);', svg)
    svg = re.sub(r'transform: translate\(10px, 48px\);', r'transform: translate(10px, 57px);', svg)
    
    # Update msg-3
    svg = re.sub(r'translate\(10, 120\)', r'translate(10, 138)', svg)
    svg = re.sub(r'transform: translate\(10px, 125px\);', r'transform: translate(10px, 143px);', svg)
    svg = re.sub(r'transform: translate\(10px, 120px\);', r'transform: translate(10px, 138px);', svg)
    
    # Update msg-4
    svg = re.sub(r'translate\(10, 192\)', r'translate(10, 219)', svg)
    svg = re.sub(r'transform: translate\(10px, 197px\);', r'transform: translate(10px, 224px);', svg)
    svg = re.sub(r'transform: translate\(10px, 192px\);', r'transform: translate(10px, 219px);', svg)
    
    # Update msg-5
    svg = re.sub(r'translate\(10, 560\)', r'translate(10, 584)', svg)
    svg = re.sub(r'transform: translate\(10px, 565px\);', r'transform: translate(10px, 589px);', svg)
    svg = re.sub(r'transform: translate\(10px, 560px\);', r'transform: translate(10px, 584px);', svg)
    
    # Update msg-6
    svg = re.sub(r'translate\(10, 632\)', r'translate(10, 665)', svg)
    svg = re.sub(r'transform: translate\(10px, 637px\);', r'transform: translate(10px, 670px);', svg)
    svg = re.sub(r'transform: translate\(10px, 632px\);', r'transform: translate(10px, 665px);', svg)

    # Change total SVG height and width to scale it down slightly (85% scale)
    # Original viewBox="0 0 550 684", new height needed is 665 + 42 + 20 = 727
    # So viewBox="0 0 550 727"
    # width="467" height="617" (approx 85% of 550x727)
    svg = re.sub(r'<svg width="550" height="684" viewBox="0 0 550 684"', r'<svg width="467" height="617" viewBox="0 0 550 727"', svg)

    with open("chat.svg", "w", encoding="utf-8") as f:
        f.write(svg)
        
    print("Successfully generated chat.svg")

if __name__ == "__main__":
    generate_svg()
