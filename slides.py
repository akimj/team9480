import os
from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap5
import random
from PIL import Image
from functions import addText

slidephoto = []
slidetext = []

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['SECRET_KEY'] = 'csumb-otter'

bootstrap = Bootstrap5(app)
@app.route('/')
def index(): 
    clear_uploaded_files()

    return render_template('index.html')
@app.route('/slideshow')
def slideshow():
   
    return render_template('slideshow.html')
@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        uploaded_file = request.files['fileToUpload']
        if uploaded_file:
            uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename))  # Save the uploaded file in the current directory
            return 'File uploaded successfully!'
    return 'No file uploaded'
def clear_uploaded_files():
    folder = app.config['UPLOAD_FOLDER']
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")
