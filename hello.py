import cv2
from flask import Flask,render_template,Response
app = Flask(__name__)
fps = 60
VideoCapture = cv2.VideoCapture(0)
@app.route('/')
def index():
    return render_template('index.html')
def gen(VideoCapture):
    success,frame = VideoCapture.read()
    while success:
        success,frame = VideoCapture.read()
        #frameToStr = frame.tostring()
        c = cv2.waitKey(1000/60)
        yield(b'--framern'
              b'Content-Type:image/jpegrnrn'+frame+b'rn')
       
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCapture),
            mimetype = 'multipart/x-mixed-replace;boundary=frame')

def hello_world():
   # VideoCapture = cv2.VideoCapture(0)
   # success,frame = VideoCapture.read()
   # while success:
   #     imshow('test',frame)
   #     cv2.waitKey(1000/60)
   #    success,frame = VideoCapture.read()
    return 'Hello World!'
if __name__ == '__main__':
    app.run()

