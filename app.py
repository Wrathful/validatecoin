from flask import Flask, request, redirect, url_for, make_response, render_template,send_from_directory
from Rugadget.moneti.ClassModel import ClassModel
from pandas import errors
import pandas as pandas
from keras.preprocessing import image
import numpy as np
import cv2
app = Flask(__name__)


# start page
@app.route("/")
def hello():
    return render_template('start.html')


# # choose file
# @app.route("/getfile", methods=['GET','POST'])
# def get_file():
#     if request.method == 'POST':
#         result = request.files['myfile']
#     else:
#         result = request.args.get['myfile']
#     return redirect(url_for('predict', filename=result.filename))



# load report
@app.route('/',methods=['GET', 'POST'])
def predict():
    model = ClassModel()
    if request.method == "POST":
        request.files['file'].save('1.jpg')
        img = cv2.imread('1.jpg')
        resized_image = cv2.resize(img, (256, 256))
        print(resized_image.shape)
        y_pred=model.predict(resized_image)
        print(y_pred)
        return render_template('start.html', predicted=y_pred)


# @app.route('/predict/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'],
#                                filename)

@app.errorhandler(404)
def not_found(error):
    return "Error: 404 not found"


@app.errorhandler(IOError)
def not_found(error):
    return "Error: file does not exist"


@app.errorhandler(pandas.errors.EmptyDataError)
def not_found(error):
    return "Error: wrong data"


if __name__ == '__main__':
    app.run(debug=True)