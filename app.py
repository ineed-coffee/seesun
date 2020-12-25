from flask import Flask, render_template, Response,request,redirect, url_for
import cv2
import os
import time
from camera import Camera
import shutil
from Detect import seesunObjectDetector,seesunTextDetector
from Speech import seesunSpeech

app = Flask(__name__)
camera = None
ssod = None
ssot = None
speech = None
guide=False

# camera.py
def get_camera():
    global camera
    if not camera:
        camera = Camera()
    return camera

def get_yolo():
    global ssod
    if not ssod:
        ssod = seesunObjectDetector()
    return ssod

def get_text():
    global ssot
    if not ssot:
        ssot = seesunTextDetector()
    return ssot

def get_speech():
    global speech
    if not speech:
        speech = seesunSpeech()
    return speech

# 되돌아갈경우
@app.route('/')
def root():
    speech = get_speech()
    path = speech.MP3_DIR
    for del_file_name in os.listdir(path):
        file_path = path + del_file_name
        temp = os.path.splitext(file_path)[-1]
        if temp == ".mp3":
            os.remove(file_path)
    return redirect(url_for('index'))

# mainpage
@app.route('/index/')
def index():
    global guide
    if not guide:
        guide=True
        speech = get_speech()
        time.sleep(2.5)
        speech.play_audio('guide_voice',guide=True,wait=False)
    return render_template('index.html')

# 이미지 캡처 camera.py에서 frame
def gen(camera):
    while True:
        frame = camera.get_feed()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# 이미지 캡쳐 된 것을 보여줌..?
@app.route('/video_feed/')
def video_feed():
    camera = get_camera()
    return Response(gen(camera),
        mimetype='multipart/x-mixed-replace; boundary=frame')

# 캡처된 이미지 저장
@app.route('/img/')
def img_capture():
    camera = get_camera()
    stamp = camera.capture()
    return redirect(url_for('show_capture', timestamp=stamp))

def stamp_file(timestamp):
    return 'temp/' + timestamp +".jpg"

# 이미지
@app.route('/img/image/<timestamp>', methods=['POST', 'GET'])
def show_capture(timestamp):
    path = stamp_file(timestamp)
    file_name = path.split('/')[1]
    file_path = camera.CAPTURES_DIR + file_name
    detector = get_yolo()
    image = cv2.imread(file_path) 
    speech = get_speech()
    speech.play_audio('wait_for_it',guide=True,wait=True)
    flag,new_image,label=detector.detect(image)
    if flag:
        cv2.imwrite(file_path, new_image)
    speech.tts(label)
    # 저장된이미지를 모델에서 보여줌
    return render_template('image.html', path=path,label=label)

# 캡처된 텍스트 이미지 저장
@app.route('/text/')
def text_capture():
    camera = get_camera()
    stamp = camera.capture()
    return redirect(url_for('show_text', name=stamp))

# 텍스트
@app.route('/text/image/<name>', methods=['POST', 'GET'])
def show_text(name):
    path = stamp_file(name)
    file_name = path.split('/')[1]
    file_path = camera.CAPTURES_DIR + file_name
    detector = get_text()
    image = cv2.imread(file_path)
    speech = get_speech()
    speech.play_audio('wait_for_it',guide=True,wait=True)
    flag,new_image,label=detector.recognize(image)
    if flag:
        cv2.imwrite(file_path, new_image)
    speech.tts(label)
    # 저장된이미지를 모델에서 보여줌
    return render_template('text.html', path=path,label=label)

# speak
@app.route('/speak/')
def start_speak():
    speech = get_speech()
    speech.play_audio('voice_on',guide=True,wait=False)
    return_text = speech.stt()
    if '보여' in return_text: 
        return redirect(url_for('img_capture'))
    elif '읽어' in return_text:
        return redirect(url_for('text_capture'))
    elif '아빠' in return_text:
        return redirect(url_for('dad'))
    elif '엄마' in return_text:
        return redirect(url_for('mom'))
    else:
        return redirect(url_for('error'))

# 예외처리 페이지
@app.route('/error')
def error():
    speech = get_speech()
    speech.play_audio('unknown_command',guide=True,wait=False)
    return render_template('return.html')

# no 캐싱
@app.after_request
def set_response_headers(r):
    r.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    r.headers['Pragma'] = 'no-cache'
    r.headers['Expires'] = '0'
    return r

#팀원들,,,
@app.route('/teams')
def teams():
    return render_template('user.html')

@app.route('/dad')
def dad():
    speech = get_speech()
    speech.tts('절 만드신 아빠는 김진원, 이동재 두분이에요! 하.하.하.')
    return redirect(url_for('index'))

@app.route('/mom')
def mom():
    speech = get_speech()
    speech.tts('절 만드신 엄마는 민채정, 박희원, 이찬주 세분이에요! 호.호.호.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
    # app.run(host='192.168.0.57',port=5001,debug=True)