from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap5
import random
from PIL import Image

app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'

bootstrap = Bootstrap5(app)
@app.route('/')
def index(): 
    return render_template('index.html')
@app.route('/slideshow')
def slideshow():
   
    return render_template('slideshow.html')
@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        uploaded_file = request.files['fileToUpload']
        if uploaded_file:
            uploaded_file.save(uploaded_file.filename)  # Save the uploaded file in the current directory
            return 'File uploaded successfully!'
    return 'No file uploaded'
