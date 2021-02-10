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
6. :round_pushpin: [Object detection model details (what I've contributed)](#idx6)

---

​	

## 1. Overview <a id="idx1"></a>

#### <img src="README.assets/innovation.svg" alt="innovation" width="30"/>개발 배경과 구상

기술의 발전이 항상 우리가 살아가는데 이롭게만 작용하지는 않습니다. 4차 산업혁명에 대한 관심과 개발이 해마다 빠르게 진행됨에 따라 이러한 기술로부터 소외된 계층, 단절된 사용자가 발생하기도 합니다. 이러한 이유로 __시선 서비스__ 는 전맹, 약맥 및 시각적으로 불편하신 분들의 새로운 눈이 되어 세상을 밝혀주고자 진행하게 된 __복합 AI 서비스__ 입니다.



<p align="center">
<img src="README.assets/슬라이드4.png" alt="innovation" width="450" />
<img src="README.assets/슬라이드5.png" alt="innovation" width="450" />
</p>

초기 구상 단계에서 크게 2가지 기능으로 서비스 개발을 목표로 하였으며 음성을 통해 서비스를 이용할 수 있도록 구상하였습니다.
> __보여줘__ : YOLO v3 활용 객체 탐지 모델 
>
> __읽어줘__ : pytesseract 활용 문자 인식 모델


<p align="center">
<img src="README.assets/슬라이드9.png" alt="innovation" width="450" />
<img src="README.assets/슬라이드10.png" alt="innovation" width="450" />
</p>



현재 음성을 통한 "보여줘" , "읽어줘" 와 같은 기능을 지원하며 웹 어플리케이션 형태로 구현하였습니다.





### d
<p align="center">
<img src="README.assets/seesuntext.gif" alt="innovation" width="400" height="234"/>
<img src="README.assets/seesunobj.gif" alt="innovation" width="400" height="234"/>
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

## 6. Object detection model details (what I've contributed) <a id="idx6"></a>

## 프로젝트 주제 선정 배경 및 구상



​	

---









