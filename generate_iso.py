import re
import urllib.request
import base64

def lighten(hex_color, amount=0.2):
    hex_color = hex_color.lstrip('#')
    if hex_color == 'ebedf0': hex_color = 'eeeeee' # Adjust light grey
    if len(hex_color) == 3: hex_color = ''.join(c + c for c in hex_color)
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    r = min(255, int(r + (255 - r) * amount))
    g = min(255, int(g + (255 - g) * amount))
    b = min(255, int(b + (255 - b) * amount))
    return f"#{r:02x}{g:02x}{b:02x}"

def darken(hex_color, amount=0.2):
    hex_color = hex_color.lstrip('#')
    if hex_color == 'ebedf0': hex_color = 'eeeeee'
    if len(hex_color) == 3: hex_color = ''.join(c + c for c in hex_color)
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    r = max(0, int(r * (1 - amount)))
    g = max(0, int(g * (1 - amount)))
    b = max(0, int(b * (1 - amount)))
    return f"#{r:02x}{g:02x}{b:02x}"

def build_iso_svg():
    with open('/tmp/ghchart.svg', 'r') as f:
        svg_content = f.read()

    rects = re.findall(r'<rect[^>]*fill:([^;]+);[^>]*data-score="(\d+)"[^>]*x="(\d+)"[^>]*y="(\d+)"', svg_content)
    if not rects:
        # Fallback to other format
        rects = re.findall(r'<rect[^>]*fill="([^"]+)"[^>]*data-score="(\d+)"[^>]*x="(\d+)"[^>]*y="(\d+)"', svg_content)
    if not rects:
        rects = re.findall(r'<rect[^>]*x="(\d+)"[^>]*y="(\d+)"[^>]*fill="([^"]+)"[^>]*data-score="(\d+)"', svg_content)
        rects = [(f, s, x, y) for (x, y, f, s) in rects]
        
    # The x values are 27, 39, 51...
    # The y values are 20, 32, 44...
    cells = []
    min_x = min([int(r[2]) for r in rects]) if rects else 0
    min_y = min([int(r[3]) for r in rects]) if rects else 0
    
    for fill, score, x, y in rects:
        col = (int(x) - min_x) // 12
        row = (int(y) - min_y) // 12
        cells.append({'col': col, 'row': row, 'score': int(score), 'fill': fill})
        
    # Sort for painter's algorithm: back to front, which is col + row
    cells.sort(key=lambda c: c['col'] + c['row'])
    
    dx = 6
    dy = 3
    dz = 8
    
    out_svg = '<svg xmlns="http://www.w3.org/2000/svg" width="440" height="258" viewBox="-50 0 700 258">\n'
    
    start_x = 350
    start_y = 50
    
    for c in cells:
        col = c['col']
        row = c['row']
        score = c['score']
        fill = c['fill']
        
        # Base colors
        top_color = lighten(fill, 0.1)
        left_color = fill
        right_color = darken(fill, 0.15)
        
        cx = start_x + (col - row) * dx
        cy = start_y + (col + row) * dy
        
        h = 2 + (score * dz)
        
        # Top
        pts_top = f"{cx},{cy-h} {cx+dx},{cy-h+dy} {cx},{cy-h+2*dy} {cx-dx},{cy-h+dy}"
        out_svg += f'<polygon points="{pts_top}" fill="{top_color}" />\n'
        
        # Left
        pts_left = f"{cx-dx},{cy-h+dy} {cx},{cy-h+2*dy} {cx},{cy+2*dy} {cx-dx},{cy+dy}"
        out_svg += f'<polygon points="{pts_left}" fill="{left_color}" />\n'
        
        # Right
        pts_right = f"{cx},{cy-h+2*dy} {cx+dx},{cy-h+dy} {cx+dx},{cy+dy} {cx},{cy+2*dy}"
        out_svg += f'<polygon points="{pts_right}" fill="{right_color}" />\n'
        
    out_svg += '</svg>'
    
    with open('/tmp/iso.svg', 'w') as f:
        f.write(out_svg)

if __name__ == '__main__':
    build_iso_svg()
