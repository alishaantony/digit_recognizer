from PIL import Image, ImageDraw

# Create a 28x28 white image
image = Image.new('L', (28, 28), color=255)
draw = ImageDraw.Draw(image)

# Draw a black number (e.g., "5")
draw.text((10, 10), '5', fill=0) #You can change the number here.

# Save the image
image.save('test.png')