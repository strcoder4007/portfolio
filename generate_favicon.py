from PIL import Image, ImageDraw, ImageFont
import os

size = 64
img = Image.new("RGBA", (size, size))
draw = ImageDraw.Draw(img)

# Green rounded rect background
draw.rounded_rectangle((0, 0, size - 1, size - 1), radius=14, fill="#1DB954")

# Try to use a system font
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
            font = ImageFont.truetype(fp, 30)
            break
        except Exception:
            continue

if font is None:
    font = ImageFont.load_default()

bbox = draw.textbbox((0, 0), "SS", font=font)
tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
x = (size - tw) / 2 - bbox[0]
y = (size - th) / 2 - bbox[1] + 2
draw.text((x, y), "SS", fill="#111111", font=font)

img.save("public/favicon.png", "PNG")
print("Created favicon.png")

icons = []
for s in [16, 32, 48]:
    resized = img.resize((s, s), Image.LANCZOS)
    icons.append(resized)
icons[0].save("public/favicon.ico", format="ICO", sizes=[(s, s) for s in [16, 32, 48]], append_images=icons[1:])
print("Created favicon.ico")