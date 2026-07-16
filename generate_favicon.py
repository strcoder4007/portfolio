from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

size = 64
padding = 3
border_width = 3
radius = 14

img = Image.new("RGBA", (size, size))
draw = ImageDraw.Draw(img)

# Rounded background with subtle gradient
def draw_gradient_rounded_rect(draw, xy, radius, color_top, color_bottom):
    # Create a temporary image for the shape mask
    mask = Image.new("L", (size, size), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle(xy, radius=radius, fill=255)

    # Create gradient fill
    gradient = Image.new("RGBA", (size, size))
    for y in range(size):
        ratio = y / (size - 1)
        r = int(color_top[0] * (1 - ratio) + color_bottom[0] * ratio)
        g = int(color_top[1] * (1 - ratio) + color_bottom[1] * ratio)
        b = int(color_top[2] * (1 - ratio) + color_bottom[2] * ratio)
        a = int(color_top[3] * (1 - ratio) + color_bottom[3] * ratio)
        ImageDraw.Draw(gradient).line([(0, y), (size, y)], fill=(r, g, b, a))

    img.paste(gradient, (0, 0), mask)

draw_gradient_rounded_rect(
    draw,
    (padding, padding, size - padding - 1, size - padding - 1),
    radius,
    (18, 18, 18, 255),   # #121212
    (30, 30, 30, 255),   # #1e1e1e
)

# Green border
draw.rounded_rectangle(
    (padding, padding, size - padding - 1, size - padding - 1),
    radius=radius,
    outline="#1DB954",
    width=border_width,
)

# Try to use a nice bold system font
font_paths = [
    "/System/Library/Fonts/Helvetica.ttc",
    "/System/Library/Fonts/SFNSDisplay.ttf",
    "/System/Library/Fonts/SFNSText.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/System/Library/Fonts/Monaco.ttf",
]

font = None
for fp in font_paths:
    if os.path.exists(fp):
        try:
            font = ImageFont.truetype(fp, 28)
            break
        except Exception:
            continue

if font is None:
    font = ImageFont.load_default()

# Draw "SS" monogram in center, slightly offset up for visual balance
text = "SS"
bbox = draw.textbbox((0, 0), text, font=font)
tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
x = (size - tw) / 2 - bbox[0]
y = (size - th) / 2 - bbox[1] - 1

# Subtle shadow behind text for depth
shadow_offset = 1
draw.text((x + shadow_offset, y + shadow_offset), text, fill=(0, 0, 0, 120), font=font)
# Main text
draw.text((x, y), text, fill="#1DB954", font=font)

img.save("public/favicon.png", "PNG")
print("Created favicon.png")

# Generate ICO with multiple sizes
icons = []
for s in [16, 32, 48]:
    resized = img.resize((s, s), Image.LANCZOS)
    icons.append(resized)
icons[0].save("public/favicon.ico", format="ICO", sizes=[(s, s) for s in [16, 32, 48]], append_images=icons[1:])
print("Created favicon.ico")

# Generate SVG favicon with the same design
svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#121212;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#1e1e1e;stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect x="{padding}" y="{padding}" width="{size - padding * 2}" height="{size - padding * 2}" rx="{radius}" fill="url(#bg)" stroke="#1DB954" stroke-width="{border_width}"/>
  <text x="32" y="44" text-anchor="middle" font-family="Bricolage, Arial, Helvetica, sans-serif" font-size="28" font-weight="700" fill="#1DB954">SS</text>
</svg>"""

with open("public/favicon.svg", "w") as f:
    f.write(svg_content)
print("Created favicon.svg")
