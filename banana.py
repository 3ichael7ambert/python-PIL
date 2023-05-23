from PIL import Image, ImageDraw

# create a new image
image = Image.new('RGBA', (100, 200), (255, 255, 255, 0))

# get a drawing context
draw = ImageDraw.Draw(image)

# draw a banana shape
draw.ellipse((20, 10, 80, 190), fill='#F5D76E', outline='#E8C348', width=2)
draw.polygon([(50, 5), (70, 30), (75, 80), (65, 130), (50, 165), (25, 165), (10, 135), (10, 75)], fill='#FFC300', outline='#E8C348', width=2)
draw.polygon([(40, 15), (60, 35), (65, 70), (55, 110), (40, 130), (20, 130), (10, 100), (10, 55)], fill='#FF5733', outline='#E8C348', width=2)

# save the image as PNG
image.save('banana.png')
