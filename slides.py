import os
from flask import Flask, render_template, request, redirect,url_for
from flask_bootstrap import Bootstrap5

slidephoto = []
slidetext = []

app = Flask(__name__)
UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap5(app)

@app.route('/')
def index(): 
    print("Vanilla Images:")  # Console test
    print(slidephoto)  # Console test
    return render_template('index.html', slidephoto=slidephoto)

@app.route('/slideshow')
def slideshow():
    print("Vanilla Images:")  # Console test
    print(slidephoto)  # Console test
    return render_template('slideshow.html')

    
@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        uploaded_file = request.files['fileToUpload']
        if uploaded_file:
            uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename))
            slidephoto.append(uploaded_file.filename)
            print("Vanilla Images:")  # Console test
            print(slidephoto)  # Console test
            return redirect(url_for('index'))  # Redirect to the main page after uploading
    return redirect(url_for('index'))
    
    
    
    print("Vanilla Images:")  # Console test
    print(slidephoto)  # Console test
    if request.method == 'POST':
        uploaded_file = request.files['fileToUpload']
        if uploaded_file:
            uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename))
            slidephoto.append(uploaded_file.filename)
            print("Vanilla Images:")  # Console test
            print(slidephoto)  # Console test
            return render_template('index.html')
    return render_template('index.html', slidephoto=slidephoto)
@app.route('/clear_images', methods=['POST'])
def clear_images():
    slidephoto.clear()
    folder = app.config['UPLOAD_FOLDER']
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")
    return render_template('index.html', slidephoto=slidephoto)
