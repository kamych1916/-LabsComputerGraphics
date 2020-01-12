import os
import json
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import argparse
import os
import time

from AbbyyOnlineSdk import *


from flask import render_template
UPLOAD_FOLDER = '/static/images'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ip_imagename = {}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():

    if request.method == 'POST':

        file = request.files['file']
        print(type(file))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join("static/images/", filename))
            os.system(f"python process.py static/images/{filename} static/texts/{filename.split('.')[0]}.txt")
            f = open(f"static/texts/{filename.split('.')[0]}.txt", 'r')
            text = f.read()[3:]
            print(text)
            return render_template("FirstPage.html", filename=filename, text=text)
    return render_template("SecondPage.html")


@app.route('/test', methods=['GET', 'POST'])
def upload_fil111e():
    os.system("python process.py static/images/test.jpg test1.txt")
    print("daadad")
    return request.remote_addr


if __name__ == '__main__':
    app.run()