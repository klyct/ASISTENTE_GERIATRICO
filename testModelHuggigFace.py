import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
import soundfile as sf

# Ruta a la carpeta que contiene los archivos del modelo personalizado
#model_folder = "path/to/my_tts_model" ##pide un .json
model_name = "facebook/tts-wav2vec2-ljspeech"
# Cargar el modelo y el tokenizador
model = Wav2Vec2ForCTC.from_pretrained(model_name)
tokenizer = Wav2Vec2Tokenizer.from_pretrained(model_name)

# Definir el texto para la generación de voz
text = "Hola, esto es una prueba de generación de voz."
input_ids = tokenizer(text, return_tensors="pt").input_ids

# Generar voz a partir del texto
with torch.no_grad():
    generated_voice = model.generate(input_ids)

# Guardar la voz generada en un archivo WAV
output_file = "output.wav"
sf.write(output_file, generated_voice[0].numpy(), model.config.sampling_rate)

print(f"Voz generada guardada en {output_file}")
