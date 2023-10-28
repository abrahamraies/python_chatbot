import openai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

def preguntar_chat_gpt(prompt,modelo="text-davinci-002"):
    respuesta = openai.Completion.create(
        engine = modelo,
        prompt = prompt,
        n = 1,
        max_tokens = 150,
        temperature = 1.5
    )
    return respuesta.choices[0].text.strip()


print("Bienvenido a nuestro chatbot básico. Escribe 'salir' cuando quieras terminar")

while True:
    ingreso_usuario = input("\nTú:")
    if ingreso_usuario.lower() == "salir":
        break
    
    prompt = f"El usuario pregunta: {ingreso_usuario}\ChatGPT responde:"
    respuesta_gpt = preguntar_chat_gpt(prompt)
    print(f"Chatbot: {respuesta_gpt}")
    