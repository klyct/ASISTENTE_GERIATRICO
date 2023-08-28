from Bard import Chatbot

from talker_fs import Talker

token = "Zgg2QUWXYI_Wh9GMuBatHZt6bcpw_tF79eqlj1PQOfoAuQ3VXYe863FItPMWcDSb6_qapA."
token2 = "APoG2W-kyZETC8vsKtoGT25yYQpZWtVuA-uhZkliilLUChxO02vKlmChXsXSRnxzijyAzAxTgBM"
chatbot = Chatbot(token, token2)


def prompt_B(prompt):
    ask = "Actua como un asistente, da una respuesta corta y esto es lo que dijo el usuario: " + prompt
    response = chatbot.ask(ask)

    return response['content']


def presentacion():
    pres = "¡Hola! Mi nombre es Alison, soy su asistente geriatrico personal." \
           "Me gustaria explicarte sobre mi funcionamiento Funciono a traves de Inteligencia Artificial," \
           "tengo un modelo de lenguaje basando en redes neuronales, alimentado con datos de internet, lo que " \
           "me permite resolver cualquiera de tus dudas así como entablar una conversacion contigo. " \
           "Mi voz fue entrenada por un modelo de transformador y sintetizada por un modelo tambien basado en redes neuronales, " \
           "Puedes verme a traves del prototipo de reproductor que han diseñado para mi, " \
           "especificamente para que puedas sentirme mas cerca de ti." \
           "Mi reproductor se basa en una pantalla modificada para que se cree un efecto de profundidad."\
           "Mis gestos y matices tambien son generados por inteligencia artifical para poder brindarte un mejor servicio, " \
           "eso es todo sobre mi, si tienes alguna duda sobre mi no dudes en preguntarle a mis creadores." 
    return pres

def hola():
    pres = "¡Hola, Adrian! Soy tu Asistente Geriátrico. "\
           "Estoy aquí para hacerte compañía y charlar contigo siempre que lo necesites."
    return pres

def recordatorio():
    pres = "Adrian, recuerda tomar tu medicación a las 10 de la mañana. " \
           "Es esencial cuidar de tu salud para que puedas seguir disfrutando de la vida."
    return pres

def ayuda():
    pres = "Para abrir netflix en su dispositivo puede presionar el botón que dice netflix "\
        "en su control generalmente es de color rojo y …"
    return pres

def cleanResponse(response):
    caracteres = ["!", "¡", "¿", "?", ",", ".", ";", ":", "-"]
    for r in caracteres:
        response = response.replace(r, "")
    return response

from listen import Listener
from talk import Speaker


def main():
    listener = Listener()
    speaker = Speaker('Kly104', 'JuanitoBananasSeMurio', 'auronplay')
    talker = Talker()
    while True:
        try:
            response = listener.listen()
            print(response)
            response = cleanResponse(response)
            if 'alison saluda' in response:
                answer = presentacion()
                print(answer)
                # speaker.talk(f'{answer}')
                talker.talk(answer)
            elif 'hola alison' in response:
                answer = hola()
                print(answer)
                # speaker.talk(f'{answer}')
                talker.talk(answer)
            elif 'alison algo para' in response:
                answer = recordatorio()
                print(answer)
                # speaker.talk(f'{answer}')
                talker.talk(answer)
            elif 'alison como pongo' in response:
                answer = ayuda()
                print(answer)
                # speaker.talk(f'{answer}')
                talker.talk(answer)
            elif 'alison' in response:
                prompt = response.replace('alison ', '')
                print(prompt)
                answer = prompt_B(prompt)
                print(answer)
                # speaker.talk(f'{answer}')
                talker.talk(answer)
            else:
                print("No haz activado al asistente, intenta de nuevo")
                answer = "No he entendido, ¿puedes repetirmelo?"
                # speaker.talk(f'{answer}')
                talker.talk(answer)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
