import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from detect import detect_model
import json

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg',])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
                   
@app.route('/', methods=['GET', 'POST'])

def upload_file():
    if request.method == 'POST':
        image_file = request.files['file']
        if image_file and allowed_file(image_file.filename):
            image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename))
            queue.put()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8181)
