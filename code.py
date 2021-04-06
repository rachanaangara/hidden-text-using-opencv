#Import necessary libraries
from flask import Flask, render_template, Response,redirect,url_for
import cv2
#Initialize the Flask app
import os
import numpy as np

app = Flask(__name__)
camera = cv2.VideoCapture(0)
@app.route('/')
def index():
    if os.path.exists('D:/hidden text/static/images/picture1.jpg'):
        os.remove('D:/hidden text/static/images/picture1.jpg')
    if os.path.exists('D:/hidden text/static/images/message.jpg'):
        os.remove('D:/hidden text/static/images/message.jpg')
    
    return render_template('homepage.html')
@app.route('/capture')
def capture():
    return render_template('capture.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


def gen_frames():  
    
    while True:
            success, frame = camera.read()  # read the camera frame
            if not success:
                break
            else:
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                
                yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/imagecaptured')
def image():
    ret,frame = camera.read()
    cv2.imwrite("D:/hidden text/static/images/picture1.jpg",frame)
    
    return render_template('preview.html')
@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response
@app.route('/retakeRequest')
def retake():   
    return redirect(url_for('index'))
@app.route('/messageRevealed')
def hiddenmsg():   
    image = cv2.imread('D:/hidden text/static/images/picture1.jpg')
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # define range of yellow color in HSV
    lower_yellow = np.array([20,100,100])
    upper_yellow = np.array([30,255,255])
    
    # Threshold the HSV image to get only blue colors
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(hsv,hsv, mask= yellow_mask)
    cv2.imwrite("D:/hidden text/static/images/message.jpg",res)
    
    return render_template('output.html')
    
if __name__ == "__main__":
    app.run(debug=True)
    
