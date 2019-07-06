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
    ###API Logic
    
    if request.method == 'POST':
        file = request.files['file']
    #Only use the allowed images
        if file and allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

        #function for detecting the model from file detect.py    
            predicted=detect_model(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    
            return predicted

        else:
            return 'Image Upload Error'
      
    else:
        return '404'


@app.route('/uploads/')
def uploaded_file(filename):
    filename = 'http://127.0.0.1:5000/uploads/' + filename
    return render_template('template.html', filename = filename)

if __name__ == '__main__':
    app.run()
