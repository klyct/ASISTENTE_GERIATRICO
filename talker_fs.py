import pyttsx3
import time

class Talker:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.set_female_spanish_voice()

    def set_female_spanish_voice(self):
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if 'female' in voice.name.lower() and 'spanish' in voice.languages[0].lower():
                self.engine.setProperty('voice', voice.id)
                break

    def talk(self, text):
        print("HABLANDO")
        self.engine.say(text)
        self.engine.runAndWait()