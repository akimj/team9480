from flask import Flask, render_template, url_for
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


