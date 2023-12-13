import os
from flask import Flask, render_template, request, redirect,url_for
from flask_bootstrap import Bootstrap5
from functions import addText
#
# CST 205
# SlideMaker
# This program makes a slideshow.
# Aiden Kim, Jake Martin, Kylie Cota, Matthijs De Vries
# 12/13/2023
#



slidephoto = []
slidetext = []
slidenames = []
textcolor = []

app = Flask(__name__)
UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'csumb-otter'
app.config['U'] = 'static/slides'

bootstrap = Bootstrap5(app)

@app.route('/')
def index():

    global slide_num
    slide_num = 0
    clear_images2()
    print("Vanilla Images:")  # Console test
    print(slidephoto) 
    print(slidetext)  # Console test
    return render_template('index.html', slidephoto=slidephoto, slidetext = slidetext)
slide_num = 0
@app.route('/noslides')
def noslides(): 
    return render_template('noslides.html') 
@app.route('/slideshow')
def slideshow():
    clear_images2()
    print("Vanilla Images:")  # Console test
    for i in range(len(slidephoto)):
        addText(i)
    print(slidephoto) 
    print(slidetext)   # Console test
    print(slidenames)
    print(textcolor)
    if not slidephoto:
        return redirect('/noslides')
    else:
        return render_template('slideshow.html', slidenames=slidenames, slide_num = slide_num)
@app.route('/increment_slide')
def increment_slide():
    global slide_num
    
    if(slide_num != len(slidenames) - 1):
        slide_num += 1
    return redirect('/slideshow')

@app.route('/decrement_slide')
def decrement_slide():
    global slide_num
    if(slide_num != 0):
        slide_num -= 1
    return redirect('/slideshow')
   
@app.route('/upload', methods=['POST'])
def upload_file():
    global slide_num
    slide_num = 0
    clear_images2()
    if request.method == 'POST':
        uploaded_file = request.files['fileToUpload']
        if uploaded_file:
            filename = uploaded_file.filename
            uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            slidephoto.append(filename)  
            text = request.form.get('lname')
            slidetext.append(text) 
            color = request.form.get('text-color')
            textcolor.append(color)
            print(slidephoto) 
            print(slidetext)
            print(textcolor)
            return redirect(url_for('index'))  
    return redirect(url_for('index'))
@app.route('/clear_images', methods=['POST'])
def clear_images():
    slidephoto.clear()
    slidetext.clear()
    slidenames.clear()
    textcolor.clear()
    folder = app.config['UPLOAD_FOLDER']
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")
    folder = app.config['U']
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")
    return render_template('index.html', slidephoto=slidephoto)

def clear_images2():
    slidenames.clear()
    folder = app.config['U']
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")
    return