# ----------------------------------------------------------------------------- #
from PIL import Image, ImageFont, ImageDraw   # Helps to add font to image.
import urllib.request                         # Fetch image from the web.

# To remove security issue.
IMAGE_PATH = "https://wallpapercave.com/wp/wp3292188.jpg"
USER_AGENT = "Type your user agent"

opener = urllib.request.URLopener()
opener.addheader('User-Agent', USER_AGENT)
IMAGE = opener.retrieve(IMAGE_PATH, "image.jpg")[0]   # Saving the image as IMAGE.


image = Image.open(IMAGE)                             # Import image and create an image object.
width, height = image.size                            # Finding the resolution of image.
if width >= 1000 and height >= 1000:
    FONT_SIZE = 50
if width >= 2000 and height >= 2000:
    FONT_SIZE = 100
if width >= 3000 and height >= 3000:
    FONT_SIZE = 150
if width >= 4000 and height >= 4000:
    FONT_SIZE = 200

draw = ImageDraw.Draw(image)                          # Setting the image as canvas to draw watermark.
text = "Github @arjunan-k"                            # Creating a watermark text for the image.


font = ImageFont.truetype("pacifico.ttf", FONT_SIZE)  # Choosing a font image and dimensions for text. Use google fonts for getting custom fonts.
text_width, text_height = draw.textsize(text, font)   # Finding the resolution of text.


PADDING = 70                                          # Choosing the positioning of the text.
x_cor = width - text_width - PADDING                  # Find coordinates of bottom right corner.
y_cor = height - text_height - PADDING


draw.text((x_cor, y_cor), text, font=font)            # Moving to bottom right corner with padding.
image.show()

image.save("watermark.jpg")                           # Save watermark.
# ----------------------------------------------------------------------------- #