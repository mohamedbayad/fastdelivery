from PIL import Image, ImageDraw, ImageFont


# create image object
image = Image.new("RGB", (200, 100), (255, 255, 255))

# create draw object
draw = ImageDraw.Draw(image)

# select a font
font = ImageFont.truetype('Code39.ttf', 24)

# draw code bar text
text = "1234567890"
draw.text((10, 10), text, font=font, fill=(0, 0, 0))

# save image to a file
image.save("codebar.png")