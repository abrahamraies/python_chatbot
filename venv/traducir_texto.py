import openai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key


def traducir_texto(texto,idioma):
    prompt = f"Por favor, traduce el texto '{texto}' al {idioma}."
    respuesta = openai.Completion.create(
        engine = "text-davinci-002",
        prompt = prompt,
        n = 1,
        max_tokens = 1000,
        temperature = 0.5
    )
    return respuesta.choices[0].text.strip()

texto_a_traducir_con_saltos = input("Ingresa el texto que deseas traducir: ")
texto_a_traducir_sin_saltos  = texto_a_traducir_con_saltos.replace("\n", " ")
mi_idioma = input("A qué idioma lo quieres traducir: ")
traduccion = traducir_texto(texto_a_traducir_sin_saltos,mi_idioma)
print(traduccion)