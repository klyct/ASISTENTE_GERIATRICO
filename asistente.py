from Bard import Chatbot
token = "Zgg2QUWXYI_Wh9GMuBatHZt6bcpw_tF79eqlj1PQOfoAuQ3VXYe863FItPMWcDSb6_qapA."
token2 = "APoG2W-kyZETC8vsKtoGT25yYQpZWtVuA-uhZkliilLUChxO02vKlmChXsXSRnxzijyAzAxTgBM"
chatbot = Chatbot(token, token2)

def prompt_B(prompt):
    response = chatbot.ask(prompt)
    return response['content']


from listen import Listener
from talk import Speaker
def main():
    listener = Listener()
    speaker = Speaker('Kly104', 'JuanitoBananasSeMurio', 'auronplay')
    while True:
        try:
            response = listener.listen()
            print(response)
            if 'hola' in response:
                prompt = response.replace('hola, ','')
                print(prompt)
                answer = prompt_B(prompt)
                print(answer)
                speaker.talk(f'{answer}')

        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()