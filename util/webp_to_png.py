# Convert webp file to png
from PIL import Image

# Open the WebP image
img = Image.open("/home/larry/mk/devcraft/util/blutterfly.webp")

# Save it as PNG
img.save("bluttterfly.png", "PNG")

print("Conversion complete: bluttterfly.png")
