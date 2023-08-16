from listen import Listener
from talk import Speaker
def main():
    listener = Listener()
    speaker = Speaker('Kly104', 'JuanitoBananasSeMurio', 'auronplay')
    try:
        response = listener.listen()
        print(response)
        if 'hola' in response:
            prompt = response.replace('hola, ','')
            print(prompt)
            speaker.talk(f'Este es el promt que se enviara: {prompt}')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()