from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from slides import slidetext
from slides import slidephoto

def addText(index):

    img = Image.open(f'static/images/{slidephoto[index]}')

    lumi = [((a[0]*299 + a[1]*587 + a[2]*114 )//1000) for a in img.getdata()]
    average = sum(lumi) / len(lumi)

    width, height = img.size
    captionx = width/10
    captiony = height - (height/6)

    fontsize = width*2 / len(slidetext[index])
    
    if fontsize > 150:
        fontsize = 150
    else:
        fontsize = fontsize

    fontname = 'Arial Rounded Bold'  #replaceable for themes 
    photofont = ImageFont.truetype(f'fonts/{fontname}.ttf', fontsize)

    draw = ImageDraw.Draw(img)

    if average >= 200:
        draw.text((captionx, captiony), f'{slidetext[index]}',
        font=photofont, fill=(0,0,0))
    else:
        draw.text((captionx, captiony), f'{slidetext[index]}', 
        font=photofont, fill=(255,255,255))
    
    img.save(f'static/slides/slide{index}.png')

    return f'slide{index}.png'


# def addBorder():
    

# def addTheme(theme):
#     return
# def addMusic(song):
#     return