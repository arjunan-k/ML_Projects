# ----------------------------Importing the modules---------------------------- #

import extcolors
import PIL
from PIL import Image, ImageDraw
import urllib.request

# ----------------------------Fetching the image from web---------------------- #

# Using image URL to fetch filename. OR we can directly assign local image name to IMAGE.
IMAGE_PATH = "https://cq351v1dh3-flywheel.netdna-ssl.com/wp-content/uploads/2015/02/place-final-1050x438.jpg"
IMAGE = urllib.request.urlretrieve(IMAGE_PATH, "image.jpg")[0]

# In case link address and image address of photo shows error save it locally and assign filename to IMAGE
# IMAGE = "bladerunner.jpg"

# ----------------------------Extracting colors-------------------------------- #

colors, total_pixel = extcolors.extract_from_path(IMAGE)
colors = colors[0:9]
print(colors)
print(total_pixel)

# ----------------------------Making RGB & HEX code list----------------------- #

rgb_list = []
for each in colors:
    rgb, pixel = each
    rgb_list.append(rgb)
rgb_list = rgb_list[0:9]
print(rgb_list)

DECIMAL_LIST = {
    "0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7",
    "8": "8", "9": "9", "10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"
}

def rgb_to_hex(RGB):
    code = "#"
    for each in RGB:
        code += str(DECIMAL_LIST[f"{int(each / 16)}"])
        code += str(DECIMAL_LIST[f"{int(each % 16)}"])
    return code

hex_list = []
for each in rgb_list:
    hex_list.append(rgb_to_hex(each))
print(hex_list)

# ----------------------------Creating color palette--------------------------- #

def render_color_palette(color_tuple):
    size = 100
    columns = len(color_tuple)
    width = columns * 100
    height = 100
    result = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    canvas = ImageDraw.Draw(result)
    for index, color in enumerate(color_tuple):
        x = int(index * size)
        y = 0
        canvas.rectangle([(x, y), (x + size, y + size)], fill=color[0])
    return result

# ----------------------------Saving the color palette with image-------------- #

image = PIL.Image.open(IMAGE)
width, height = image.size
x_position = int((int(width) - int(len(colors)*100)) / 2)
y_position = height - 130

render_color_palette(colors).save("color_palette.png")

img1 = Image.open(IMAGE)
img2 = Image.open("color_palette.png")
img1.paste(img2, (x_position, y_position), mask=img2)
img1.save("final.jpg")

# ----------------------------------------------------------------------------- #