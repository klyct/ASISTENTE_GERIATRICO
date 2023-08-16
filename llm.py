from Bard import Chatbot
token = "Zgg2QUWXYI_Wh9GMuBatHZt6bcpw_tF79eqlj1PQOfoAuQ3VXYe863FItPMWcDSb6_qapA."
token2 = "APoG2W-kyZETC8vsKtoGT25yYQpZWtVuA-uhZkliilLUChxO02vKlmChXsXSRnxzijyAzAxTgBM"
chatbot = Chatbot(token, token2)


import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)  ##velocidad del habla



def prompt_B(prompt):
    response = chatbot.ask(prompt)
    return response['content']


def speak(text):
    engine.say(text)
    engine.runAndWait()


def main():
    print("s")