from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 


def addText(index):

    img = Image.open(f'static/images/{slidephoto[index]}.jpg')

    #need to figure out: accept jpg jpeg and png
    
    lumi = [((a[0]*299 + a[1]*587 + a[2]*114 )//1000) for a in img.getdata()]
    average = sum(lumi) / len(lumi)

    width, height = img.size
    captionx = width/6
    captiony = height - (height/6)

    draw = ImageDraw.Draw(img)
    
    if average >= 200:
        draw.text((captionx, captiony), f'{slidetext[index]}' ,(0,0,0))
    else:
        draw.text((captionx, captiony), f'{slidetext[index]}' ,(255,255,255))

    #need to figure out: make text bigger/scalable 
    
    img.save(f'slide{index}.png')

    return f'slide{index}.png'



# def addTheme(theme):
#     return
# def addMusic(song):
#     return
