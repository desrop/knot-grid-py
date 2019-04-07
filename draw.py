from PIL import Image, ImageDraw

im = Image.open("metroid-tiles.png")
# im = im.convert("RGB")

# Samus straight-on
# 40x70
box = (288,347,328,417)
region = im.crop(box)
region.load()
region.show()

region.save("samus-straight-on.png")
#im2 = Image.new(mode='RGB', size=(100, 100), color=None)
#im2.paste(region, (0, 0))

#im2.show()

