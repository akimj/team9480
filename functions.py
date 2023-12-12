from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
def addText(index):
    from slides import slidephoto, slidetext, slidenames, textcolor
    img = Image.open(f'static/images/{slidephoto[index]}')

    # lumi = [((a[0]*299 + a[1]*587 + a[2]*114 )//1000) for a in img.getdata()]
    # average = sum(lumi) / len(lumi)
    # No longer needed since user selects color for each image

    width, height = img.size
    captionx = width/10
    captiony = height - (height/6)
    fontsize = 1
    if(len(slidetext[index])!=0):
        fontsize = width*1.5 / len(slidetext[index])
    if fontsize > 150:
        fontsize = 150
    else:
        fontsize = fontsize

    fontname = 'Arial Rounded Bold'  #replaceable for themes 
    photofont = ImageFont.truetype(f'fonts/{fontname}.ttf', fontsize)

    draw = ImageDraw.Draw(img)

    if textcolor[index] == 'black':
        draw.text((captionx, captiony), f'{slidetext[index]}',
        font=photofont, fill=(0,0,0))
    elif textcolor[index] == 'white':
        draw.text((captionx, captiony), f'{slidetext[index]}', 
        font=photofont, fill=(255,255,255))
    elif textcolor[index] == 'blue':
        draw.text((captionx, captiony), f'{slidetext[index]}', 
        font=photofont, fill=(0,0,255))
    elif textcolor[index] == 'red':
        draw.text((captionx, captiony), f'{slidetext[index]}', 
        font=photofont, fill=(255,0,0))
    elif textcolor[index] == 'green':
        draw.text((captionx, captiony), f'{slidetext[index]}', 
        font=photofont, fill=(0,255,0))
    elif textcolor[index] == 'purple':
        draw.text((captionx, captiony), f'{slidetext[index]}', 
        font=photofont, fill=(128,0,128))
    elif textcolor[index] == 'yellow':
        draw.text((captionx, captiony), f'{slidetext[index]}', 
        font=photofont, fill=(255,255,0))  

    img.save(f'static/slides/slide{index}.png')
    slidenames.append(f'slide{index}.png')

    return f'slide{index}.png'


# def addBorder():
    

# def addTheme(theme):
#     return
# def addMusic(song):
#     return