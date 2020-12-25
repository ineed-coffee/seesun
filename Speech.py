class seesunSpeech():

    MP3_DIR = "static/temp/"
    GUIDE_DIR = "static/mp3/"
    
    def __init__(self):
        
        import os
        import urllib
        from playsound import playsound
        from requests import post
        from json import loads as jls
        from json import load as jl
        import speech_recognition as sr
        import time
        
        self.request = urllib.request
        self.parse = urllib.parse.quote
        self.post = post
        self.loads = jls
        self.load = jl
        self.get_local = time.localtime
        self.path = os.path.dirname( os.path.abspath( __file__ ) )
        self.play = playsound
        self.R = sr.Recognizer()
        self.M = sr.Microphone(sample_rate=16000)

        with open(self.path+'/api_config/kakao.json') as json_file:
            json_data = self.load(json_file)
        self._kakao_api_key = json_data['app_key']

        with open(self.path+'/api_config/clova.json') as json_file:
            json_data = self.load(json_file)
        self._clova_client_id = json_data['client_id']
        self._clova_client_secret = json_data['client_secret']

    def play_audio(self,file_name,guide=False,wait=False):
        if not guide:
            self.play(seesunSpeech.MP3_DIR+file_name + ".mp3",block=wait)
        else:
            self.play(seesunSpeech.GUIDE_DIR+file_name + ".mp3",block=wait)
        return
                
    def tts(self,input_string):
        text = self.parse(input_string)

        speaker = 'nara'
        speed = 0
        
        data = "speaker=" + speaker + "&speed=" + str(speed) + "&text=" + text

        url = "https://naveropenapi.apigw.ntruss.com/tts-premium/v1/tts"
        request = self.request.Request(url)

        request.add_header("X-NCP-APIGW-API-KEY-ID", self._clova_client_id)
        request.add_header("X-NCP-APIGW-API-KEY", self._clova_client_secret)

        response = self.request.urlopen(request, data=data.encode('utf-8'))

        if response.getcode() == 200:

            now = self.get_local()
            response_body = response.read()
            file_name = "%04d%02d%02d_%02d%02d%02d" % \
                        (now.tm_year, now.tm_mon, now.tm_mday,
                         now.tm_hour, now.tm_min, now.tm_sec) + "_" + \
                         speaker + "_" + str(speed) + "_"
            with open(seesunSpeech.MP3_DIR+file_name + ".mp3", 'wb') as f:
                f.write(response_body)

            self.play_audio(file_name)
        else:
             print("Error Code")

    def stt(self):
        url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"

        headers_ = {
            "Content-Type": "application/octet-stream",
            "X-DSS-Service": "DICTATION",
            "Authorization": "KakaoAK " + self._kakao_api_key
        }

        with self.M as source:
            self.R.adjust_for_ambient_noise(source,duration=0.75)
            audio = self.R.listen(source)

        res = self.post(url,headers=headers_,data=audio.get_raw_data())

        result_json_string = res.text[res.text.index('{"type":"finalResult"'):res.text.rindex('}')+1]
        result = self.loads(result_json_string)
        
        return result['value']

            
