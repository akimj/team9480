from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 


def addText(index):

    img = Image.open(slidephoto[index])
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("sans-serif.ttf", 16)

    # if color is => 100:
    draw.text((0, 0), slidetext[index] ,(255,255,255),font=font)
    img.save(f"slide{index}.jpg")

    return none

# def addTheme(theme):
#     return
# def addMusic(song):
#     return
