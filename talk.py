import os.path
import tempfile
from pygame import mixer
import time
import fakeyou

fake_you = fakeyou.FakeYou()
class Speaker :
    def __init__(self, username, password, model_name):
        self.username = username
        self.password = password
        self.model_name = model_name

    def __login_fakeyou(self):
        fake_you.login(self.username, self.password)

    def __get_token(self, model_name):
        result = fake_you.search(model_name)
        return result.voices.modelToken[0]

    def __generate_audio(self,text):
        temp_file = tempfile.mkdtemp()
        save_path=os.path.join(temp_file, 'temp.wav')
        tts_model =self.model_name
        fake_you.say(text=text, ttsModelToken=tts_model, filename=save_path)
        return save_path

    def talk(self, text):
        mixer.init()
        filename = self.__generate_audio(text)
        mixer.music.load(filename)
        audio_duration = mixer.Sound(filename).get_length()
        mixer.music.play()
        time.sleep(audio_duration)
