from flask import Flask, render_template, url_for, request, jsonify, Response
import base64
import codecs as c
import time
from werkzeug.utils import secure_filename
from Evaluate import Predict

app = Flask(__name__)
evaluate = Predict()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/capture')
def capture():
    return render_template('capture.html')


@app.route('/upload')
def upload():
    return render_template('upload.html')


def fin2(base_string, file_name):  # this writes the image to disk
    str_obj = base_string.split('base64')[1][1:].encode()
    fh = open(file_name, "wb")
    fh.write(c.decode(obj=str_obj, encoding='base64'))
    fh.close()


@app.route('/process/<path:img>')
def process(img):
    img_path = 'static/temp/new.jpg'
    fin2(img, img_path)
    result = evaluate.get_result(img_path)

    return render_template('results.html', res=result)


@app.route('/compare', methods=['POST', 'GET'])
def compare():
    if request.method == 'POST':

        sent_file = request.files['file']
        full_name = f"{int(time.time())}" + secure_filename(sent_file.filename)
        f_name = f'static/temp/{full_name}'
        sent_file.save(f_name)
        result = evaluate.get_result(f_name)

        return render_template('results.html', res=result)
    else:
        return home()


if __name__ == '__main__':
    app.run(debug=True)