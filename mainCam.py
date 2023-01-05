import os.path
import numpy as np
import cv2
import json
from flask import Flask,request,Response
import uuid


#image to text code

def ImageToText(image):
    #path to save imaage after processed
    path_file = ('static/%s.jpg'%uuid.uuid4().hex)
    image = cv2.resize(image,(1300,800))
    original = image

    gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    
    cv2.imwrite(path_file,gray_img)
    return json.dumps(path_file)


#making th flask app

app = Flask(__name__)

@app.route("/api/upload", methods = ['POST'])

# @app.route("/")

def upload():
    # return "testing"
    img = cv2.imdecode(np.fromstring(request.files['image'].read(),np.uint8),cv2.IMREAD_UNCHANGED)
    img_processed = ImageToText(img)
    return Response(response=img_processed, status=200, mimetype="application/json")



# app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    app.run(debug = True)



