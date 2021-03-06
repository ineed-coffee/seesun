# <img src="README.assets/innovation.svg" alt="innovation" width="50" height="50"/> Seesun (시선)

멀티캠퍼스 딥러닝 기반 AI 엔지니어링 과정에서 파이널 프로젝트로 진행한 복합 AI 서비스 시선입니다. (우수상 :star: ​) 

Integrative-AI service project from _Deep Learning based AI engineering course_ at Multicampus (won 2nd place :star: ) 

## 결과보고서(전체 내용) : [Result report](https://drive.google.com/file/d/1nLgAIHOelu9FhDNqWRl28a83gzGkhJgS/view?usp=sharing)  <a><img src="https://media.giphy.com/media/mFknMI76h9WHmuukXw/giphy.gif" width="40px"></a> 

​	


### Table of contents 

1. :scroll: [Overview](#idx1)
2. :game_die: [Role](#idx2)
3. :mag_right: [Skills & Process](#idx3)
4. :open_file_folder: [Service Architecture](#idx4)
5. :outbox_tray: [Main Function](#idx5)
6. :round_pushpin: [Details of my role](#idx6)

---

​	

## 1. Overview <a id="idx1"></a>

#### <img src="README.assets/innovation.svg" alt="innovation" width="30"/>개발 배경

기술의 발전이 항상 우리가 살아가는데 이롭게만 작용하지는 않습니다. 4차 산업혁명에 대한 관심과 개발이 해마다 빠르게 진행됨에 따라 이러한 기술로부터 소외된 계층, 단절된 사용자가 발생하기도 합니다. 이러한 이유로 __시선 서비스__ 는 전맹, 약맥 및 시각적으로 불편하신 분들의 새로운 눈이 되어 세상을 밝혀주고자 진행하게 된 __복합 AI 서비스__ 입니다.

<p align="center">
<img src="README.assets/슬라이드4.PNG" alt="innovation" width="415" />
<img src="README.assets/슬라이드5.PNG" alt="innovation" width="415" />
</p>

#### <img src="README.assets/innovation.svg" alt="innovation" width="30"/>초기 구상

초기 구상 단계에서 크게 2가지 기능으로 서비스 개발을 목표로 하였으며 음성을 통해 서비스를 이용할 수 있도록 구상하였습니다.
> __보여줘__ : YOLO v3 활용 객체 탐지 모델 
>
> __읽어줘__ : pytesseract 활용 문자 인식 모델

<p align="center">
<img src="README.assets/슬라이드9.PNG" alt="innovation" width="415" />
<img src="README.assets/슬라이드10.PNG" alt="innovation" width="415" />
</p>

#### <img src="README.assets/innovation.svg" alt="innovation" width="30"/>최종 구현
최종 서비스 구현은 flask 기반 웹 어플리케이션 형태로 구현하였으며, 음성을 통해 `보여줘` , `읽어줘` 와 같은 명령 전달을 할 수 있습니다.

<p align="center">
<img src="README.assets/seesuntext.gif" alt="innovation" width="415"/>
<img src="README.assets/seesunobj.gif" alt="innovation" width="415"/>
</p>



## [시연 영상(simulation video)](https://drive.google.com/file/d/18GEFLZXRDWiA-2HufVHxsTNec0NyiyJc/view?usp=sharing) <a><img src="https://media.giphy.com/media/mFknMI76h9WHmuukXw/giphy.gif" width="70px"></a> 

---

​	

## 2. Role <a id="idx2"></a>

<img src="https://avatars1.githubusercontent.com/u/46684150?s=400&u=8c807418399048f8df2f14fce271f7f0f1fc7226&v=4" alt="mem1" width="70" height="60"/> [jw0831](https://github.com/jw0831) 

- Prior research review (OCR, STR, CRAFT)
- Text detection modeling ( pytesseract)
- Text recognition modeling ( pytesseract)
- Text-image preprocessing (OpenCV , deskew)
- Support modularization
- Translator modeling (Seq2Seq , in progress)

<img src="https://avatars2.githubusercontent.com/u/57827670?s=400&u=d51d9f14c9bde91f7e55b7087cffdc0f93b726e1&v=4" alt="mem1" width="70" height="60"/> [__ineed-coffee(작성자)__](https://github.com/ineed-coffee) 
> #### For details, [details of my role](#idx6)
- __Image data collection (AI HUB , Roboflow.ai , Google open image dataset)__ 
- __Define custom category & Image annotation work__ 
- __Custom object detection modeling (YOLOv3 , darknet)__ 
- __Modularization & Maintenance__ 
- __Speech-to-text module work (Kakao open API)__ 
- __Support web application implementation (Flask)__ 



<img src="https://avatars0.githubusercontent.com/u/59459751?s=400&v=4" alt="mem1" width="70" height="60"/> [heewonp](https://github.com/heewonp) 

- Prior research review (CRAFT, YOLOv5 from PyTorch)
- Image data collection (AI HUB , Roboflow.ai , Google open image dataset)
- Define custom category & Image annotation work 
- Custom object detection modeling (YOLOv3 , darknet)
- Video-stream module work (Flask)
- Web application implementation (Flask)

<img src="https://avatars1.githubusercontent.com/u/70255515?s=400&v=4" alt="mem1" width="70" height="60"/> [cjlee0217](https://github.com/cjlee0217)

- Prior research review (OCR, STR, EAST, CRAFT)
- Text detection modeling ( pytesseract)
- Text recognition modeling ( pytesseract)
- Text-image preprocessing (OpenCV , deskew)
- Translator modeling (Seq2Seq , in progress)

<img src="https://avatars2.githubusercontent.com/u/32133444?s=400&u=d536da64f1f3d48c84b108622edc5d043a1f317a&v=4" alt="mem1" width="70" height="60"/> [chloecmin](https://github.com/chloecmin)

- Text detection modeling ( pytesseract)
- Text recognition modeling ( pytesseract)
- Text-to-speech module work (Clova open API)
- Video-stream module work (Flask)
- Module QA

 	

---

​	

## 3. Skills & Process <a id="idx3"></a>

### Project skills 

__1. Language & Tool__ 

- Python 3.8 
- Visual Studio Code
- PyCharm


__2. Object detection model__ 

- Darknet framework :link: [Link](https://github.com/AlexeyAB/darknet)
- Fine tuning from YoloV3 pretrained weights
- opencv-dnn framework (4.4.0)

__3. Text recognition model__ 

- pytesseract (0.3.6)
- deskew (0.10.3)
- opencv-python (4.4.0)

### Development process 

2020.11.24 ~ 2020.12.23 

[WBS in details](https://drive.google.com/file/d/1L0GKjlu0fwBe_UINzBbXqwEl1mUZBACm/view?usp=sharing) 

​	

---

​	

## 4. Service Architecture <a id="idx4"></a>

<p align="center">
	<img src="README.assets/arch.png" alt="architecture" width="869" height="549"/>
	<img src="README.assets/flow.png" alt="flow" width="650" height="250"/> 
</p>



​	

---

​	

## 5. Main Function <a id="idx5"></a>

### __【Show】 what's in front of you__ 

- by asking with specific keyword "보여줘" , our custom YOLO model will tell you what's in front of you

​	

__Recognizable object table__ 

|    __    |     __     |          __           |         __          |      __      |
| :------: | :--------: | :-------------------: | :-----------------: | :----------: |
| 1000 won | 10000 won  |         desk          |        chair        |   sunglass   |
|  bottle  |  umbrella  |          toy          |      chopstick      |    biker     |
|   car    | motorcycle |          cat          |         dog         |    person    |
|  truck   |    bus     | traffic light (green) | traffic light (red) | traffic sign |

 	

__Example__ 

```python
Out : "There are 1 1000won , 1 cat , and 1 dog in front of you"
```

<img src="README.assets/show_result.PNG" /> 



### __【Read】 what's in front of you__ 

- by asking with specific keyword "읽어줘" , our pytesseract model will read the recognized text in front of you



__Example__ 

```python
Out : "2020년 하반기 4차산업혁명 선도인력 양성 훈련 입과를 환영합니다 multicampus"
```

<img src="README.assets/text_result.PNG"/> 

​	

---

​	

## 6. Details of my role <a id="idx6"></a>

#### <img src="README.assets/innovation.svg" alt="innovation" width="30"/>__Define custom dataset__ 

> 시각적으로 불편함을 겪는 사용자의 입장에서 자주 찾게되는 물체 20개를 선정.
>
> 수집이 불가한 항목은 직접 샘플 촬영을 진행하여 [labelImg](https://github.com/tzutalin/labelImg) 오픈 소스를 통해 annotation 작업 수행.
>
> 수집 가능한 항목은 [AI hub](https://www.aihub.or.kr/aidata/136) , [roboflow.ai](https://public.roboflow.com/object-detection/self-driving-car) , [google open image dataset](https://storage.googleapis.com/openimages/web/download.html) 로부터 분할 수집을 진행.

![s35](README.assets/슬라이드35.PNG) 

> 수집 결과
> 

![s36](README.assets/슬라이드36.PNG) 

#### <img src="README.assets/innovation.svg" alt="innovation" width="30"/>__Choosing proper framework__ 

> fine-tuning 진행에 앞서 yolo v3 모델 활용을 위한 각 YOLO-framework 비교 및 선정.

![s38](README.assets/슬라이드38.PNG) 

> 최종 선정은 [AlexeyAB](https://github.com/AlexeyAB/darknet/commits?author=AlexeyAB)의 [Darknet](https://github.com/AlexeyAB/darknet) framework 를 로컬환경에 빌드하여 커스텀 데이터셋으로부터 전이학습을 진행.

![s39](README.assets/슬라이드39.PNG) 

#### <img src="README.assets/innovation.svg" alt="innovation" width="30"/>__Training result__ 
> __Train environment__ 
>
> `Windows 10` 
>
> `Visual studio 2017` 
>
> `CUDA 10.1` 
>
> `cuDNN 8.0.5` 
>
> `GeForce RTX 2080 SUPER` (two)
>
> - Image size = 416 X 416
>
> - batch=64
> - subdivisions=32
> - iterations = 60200
> - learning rate = 0.0005 (using 2 GPU)

![s40](README.assets/슬라이드40.PNG) 
> - 0.8 수준의 Avg loss 와 45% 의 최종 mAP 성능을 확인할 수 있었음
> - custom weights file [download](https://drive.google.com/file/d/1lQjvhPUiNVBY9XjWENvcCETSkYTYgdiR/view?usp=sharing)  
> 
***
#### <img src="README.assets/innovation.svg" alt="innovation" width="30"/>__Modularization__ 

> 두 인식 모델 및 음성 입/출력 모듈을 별도로 작성하여 PyPi 에 배포 [SeeSun](https://pypi.org/project/SeeSun/) 

#### `Package architecture` 

- __\_\_init.py\_\___ 
- __model_config__ 
  - model.cfg (모델 구조 파일)
  - model.weights (모델 가중치 파일)
- __Detector.py__ 
  - seesunObjectDetector (class , object)
    - detect (method) : return type =`string` 
  - seesunTextDetector (class , object)
    - recognize(method) : return type = `string` 
- __Speech.py__ 
  - seesunSpeech (class , object)
    - tts (method) : return type = `None` (audio played immediately)
    - stt (method) : return type = `string` 



#### `Usage` 

__for object detection__ 

```python
from SeeSun.Detect import seesunObjectDetector
import cv2

detector = seesunObjectDetector()

my_img = cv2.imread('path/to/image/file')
detector.detect(my_img)
```

```shell
OUT : '현재 앞에는 XX는 3개 , OO은 6대 있습니다.'
```

---

​	

__for text detection__ 

```python
from SeeSun.Detect import seesunTextDetector
import cv2

detector = seesunTextDetector()

my_img = cv2.imread('path/to/image/file')
detector.recognize(my_img)
```

```shell
OUT : '코로나 3차 대유행으로 인한 지하철 운행시간 조정 안내 ... '
```

---

​	

__for speech recognition,synthesis__ 

```python
from SeeSun.Speech import seesunSpeech

speech = seesunSpeech()

speech.tts('input_string')
speech.stt('path/to/audio_file')
```

```shell
OUT : None
```


---









