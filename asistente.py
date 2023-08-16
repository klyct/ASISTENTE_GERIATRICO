from Bard import Chatbot
token = "Zgg2QUWXYI_Wh9GMuBatHZt6bcpw_tF79eqlj1PQOfoAuQ3VXYe863FItPMWcDSb6_qapA."
token2 = "APoG2W-kyZETC8vsKtoGT25yYQpZWtVuA-uhZkliilLUChxO02vKlmChXsXSRnxzijyAzAxTgBM"
chatbot = Chatbot(token, token2)

def prompt_B(prompt):
    response = chatbot.ask(prompt)
    return response['content']

def presentacion():
    pres = "¡Hola! Mi nombre es Kim, soy su asistente geriatrico personal" \
           "¿Qué me presente...? Funciono a traves de Inteligencia Artificial," \
           "tengo un modelo de lenguaje que me permite resolver cualquiera de tus dudas" \
           "así como entablar una conversacion contigo. " \
           "Mi voz fue entrenada por un modelo se síntetis tambien basado en redes neuronales," \
           "Puedes verme a traves del prototipo de reproductor que han diseñado para mi" \
           "mis gestos y matices tambien son generados por inteligencia " \
           "artificial para poder brindarte un mejor servicio, eso es todo sobre mi, si tienes alguna duda" \
           "sobre mi no dudes en preguntarle a mis creadores."##Inserte saludo de presentacion
    return pres

from listen import Listener
from talk import Speaker
def main():
    listener = Listener()
    speaker = Speaker('Kly104', 'JuanitoBananasSeMurio', 'auronplay')
    while True:
        try:
            response = listener.listen()
            print(response)
            if 'kim, presentate' in response:
                answer = presentacion()
                print(answer)
                #speaker.talk(f'{answer}')
            elif 'kim' in response:
                prompt = response.replace('kim, ','')
                print(prompt)
                answer = prompt_B(prompt)
                print(answer)
                #speaker.talk(f'{answer}')
            else:
                print("No haz activado al asistente, intenta de nuevo")
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()