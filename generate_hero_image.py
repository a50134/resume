from PIL import Image, ImageDraw, ImageFont
import os

# Create a hero image
width, height = 1200, 600
image = Image.new('RGB', (width, height), color='#f0f4ff')
draw = ImageDraw.Draw(image)

# Add gradient effect
for y in range(height):
    ratio = y / height
    r = int(240 + (65 - 240) * ratio)
    g = int(244 + (149 - 244) * ratio)
    b = int(255 + (237 - 255) * ratio)
    draw.line([(0, y), (width, y)], fill=(r, g, b))

# Add decorative elements
draw.ellipse([100, 50, 300, 250], outline='#6495ED', width=3)
draw.ellipse([900, 350, 1100, 550], outline='#87CEEB', width=3)
draw.polygon([(600, 100), (700, 300), (500, 300)], outline='#6495ED', width=2)

# Save image
image.save('src/images/hero-bg.png')
print("✓ Hero image generated: src/images/hero-bg.png")
