import io
from pydub import AudioSegment
import speech_recognition as sr
import whisper
import tempfile
import os

temp_file = tempfile.mkdtemp()
save_path = os.path.join(temp_file,'temp.wav')
listener = sr.Recognizer()
class Listener:
    def __listen_from_mic(self):
        try:
            with sr.Microphone() as source:
                print('Di algo')
                listener.adjust_for_ambient_noise(source, duration=0.2,)
                audio = listener.listen(source)
                data = io.BytesIO(audio.get_wav_data())
                audio_clip = AudioSegment.from_file(data)
                audio_clip.export(save_path, format='wav')
        except Exception as e:
            print(e)
        return save_path


    def __recognize_audio(self, save_path):
        audio_model = whisper.load_model('base')
        transcription = audio_model.transcribe(save_path, language='spanish', fp16=False)
        return transcription['text']

    def listen(self):
        return self.__recognize_audio(self.__listen_from_mic()).lower()