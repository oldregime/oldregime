import urllib.request
import json
import datetime
import base64

def lighten(hex_color, amount=0.1):
    hex_color = hex_color.lstrip('#')
    if hex_color == 'ebedf0': hex_color = 'eeeeee'
    if len(hex_color) == 3: hex_color = ''.join(c + c for c in hex_color)
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    r = min(255, int(r + (255 - r) * amount))
    g = min(255, int(g + (255 - g) * amount))
    b = min(255, int(b + (255 - b) * amount))
    return f"#{r:02x}{g:02x}{b:02x}"

def darken(hex_color, amount=0.15):
    hex_color = hex_color.lstrip('#')
    if hex_color == 'ebedf0': hex_color = 'eeeeee'
    if len(hex_color) == 3: hex_color = ''.join(c + c for c in hex_color)
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    r = max(0, int(r * (1 - amount)))
    g = max(0, int(g * (1 - amount)))
    b = max(0, int(b * (1 - amount)))
    return f"#{r:02x}{g:02x}{b:02x}"

def generate_stats_svg():
    url = "https://github-contributions.vercel.app/api/v1/oldregime"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        response = urllib.request.urlopen(req).read().decode('utf-8')
        data = json.loads(response)
    except:
        print("Failed to fetch data")
        return
        
    conts = data.get('contributions', [])
    # Sort by date
    conts.sort(key=lambda x: x['date'])
    
    # We only want the last 365 days
    if len(conts) > 365:
        conts = conts[-365:]
        
    total_count = sum(c['count'] for c in conts)
    best_day = max(c['count'] for c in conts) if conts else 0
    
    # Calculate streaks
    longest_streak = 0
    current_streak = 0
    temp_streak = 0
    for c in conts:
        if c['count'] > 0:
            temp_streak += 1
            if temp_streak > longest_streak:
                longest_streak = temp_streak
        else:
            temp_streak = 0
            
    # Calculate current streak by looking backward from today
    # But today might be 0, so we check if today or yesterday had commits
    rev_conts = reversed(conts)
    c_streak = 0
    started = False
    for i, c in enumerate(rev_conts):
        if c['count'] > 0:
            c_streak += 1
            started = True
        elif started or i > 1:
            break
    current_streak = c_streak
    
    # Drawing SVG
    svg_w = 740
    svg_h = 420
    
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{svg_w}" height="{svg_h}" viewBox="0 0 {svg_w} {svg_h}">\n'
    # Base background
    svg += f'<rect width="{svg_w}" height="{svg_h}" rx="8" fill="#ffffff" stroke="#e1e4e8" stroke-width="2"/>\n'
    
    # Style for text
    svg += '''
    <style>
      .title { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 14px; font-weight: 600; fill: #24292e; }
      .stat-num { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 26px; font-weight: 600; fill: #28a745; }
      .stat-label { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 12px; font-weight: 600; fill: #586069; }
      .stat-sub { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 10px; font-weight: 400; fill: #586069; }
    </style>
    '''
    
    # Draw right stats panel
    svg += '<g transform="translate(480, 40)">\n'
    svg += '<text x="0" y="0" class="title">Contributions</text>\n'
    svg += f'<text x="0" y="35" class="stat-num">{total_count:,}</text>\n'
    svg += '<text x="0" y="55" class="stat-label">Total</text>\n'
    
    svg += f'<text x="90" y="35" class="stat-num">{best_day:,}</text>\n'
    svg += '<text x="90" y="55" class="stat-label">Best day</text>\n'
    svg += '</g>\n'
    
    # Draw left stats panel
    svg += '<g transform="translate(40, 310)">\n'
    svg += '<text x="0" y="0" class="title">Streaks</text>\n'
    
    svg += f'<text x="0" y="35" class="stat-num">{longest_streak} <tspan class="stat-label">days</tspan></text>\n'
    svg += '<text x="0" y="55" class="stat-label">Longest</text>\n'
    
    svg += f'<text x="90" y="35" class="stat-num">{current_streak} <tspan class="stat-label">days</tspan></text>\n'
    svg += '<text x="90" y="55" class="stat-label">Current</text>\n'
    svg += '</g>\n'
    
    # Draw the Isometric Graph
    start_x = 320
    start_y = 60
    
    dx = 7
    dy = 4
    dz = 7 # height per commit
    
    # Group cells by week (col) and day of week (row)
    # The vercel api date is YYYY-MM-DD. We can map to col/row
    cells = []
    # First day of the 365 days
    first_date = datetime.datetime.strptime(conts[0]['date'], "%Y-%m-%d")
    # Shift so first_date is the correct row (0 = Sunday, 6 = Saturday)
    # Python weekday(): 0=Mon, 6=Sun. We want 0=Sun.
    start_row = (first_date.weekday() + 1) % 7
    
    for i, c in enumerate(conts):
        day_idx = i + start_row
        col = day_idx // 7
        row = day_idx % 7
        cells.append({'col': col, 'row': row, 'score': c['count'], 'fill': c['color']})
        
    cells.sort(key=lambda c: c['col'] + c['row'])
    
    for c in cells:
        col = c['col']
        row = c['row']
        score = min(c['score'], 20) # Cap height
        fill = c['fill']
        
        # Base colors
        top_color = lighten(fill, 0.1)
        left_color = fill
        right_color = darken(fill, 0.15)
        
        cx = start_x + (col - row) * dx
        cy = start_y + (col + row) * dy
        
        # Make the height dynamic based on the count. 
        # Base height is 3. Max height could be 50.
        h = 3 + (score * dz)
        if score == 0:
            h = 3
            top_color = "#ebedf0"
            left_color = "#e2e4e7"
            right_color = "#d9dcdf"
        
        # Top
        pts_top = f"{cx},{cy-h} {cx+dx},{cy-h+dy} {cx},{cy-h+2*dy} {cx-dx},{cy-h+dy}"
        svg += f'<polygon points="{pts_top}" fill="{top_color}" />\n'
        
        # Left
        pts_left = f"{cx-dx},{cy-h+dy} {cx},{cy-h+2*dy} {cx},{cy+2*dy} {cx-dx},{cy+dy}"
        svg += f'<polygon points="{pts_left}" fill="{left_color}" />\n'
        
        # Right
        pts_right = f"{cx},{cy-h+2*dy} {cx+dx},{cy-h+dy} {cx+dx},{cy+dy} {cx},{cy+2*dy}"
        svg += f'<polygon points="{pts_right}" fill="{right_color}" />\n'
    
    svg += '</svg>'
    
    with open('/tmp/iso.svg', 'w') as f:
        f.write(svg)
    print("Successfully generated /tmp/iso.svg")

if __name__ == '__main__':
    generate_stats_svg()
