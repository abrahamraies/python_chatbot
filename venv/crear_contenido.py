import openai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

def crear_contenido(tema,tokens,temperatura,modelo="text-davinci-002"):
    prompt = f"Por favor escribe un artículo corto sobre el tema: {tema}\n\n"
    respuesta = openai.Completion.create(
        engine = modelo,
        prompt = prompt,
        n = 1,
        max_tokens = tokens,
        temperature = temperatura
    )
    return respuesta.choices[0].text.strip()

def resumir_texto(texto,tokens,temperatura,modelo="text-davinci-002"):
    prompt = f"Por favor resume el siguiente texto en español: {texto}\n\n"
    respuesta = openai.Completion.create(
        engine = modelo,
        prompt = prompt,
        n = 1,
        max_tokens = tokens,
        temperature = temperatura
    )
    return respuesta.choices[0].text.strip()

tema = input("Elije un tema para tu artículo: ")
tokens = int(input("Cuántas palabras maximas tendrá tu artículo: "))
temperatura = int(input("Del 1 al 10 que tan creativo quieres que sea tu artíuclo"))/10

articulo_creado = crear_contenido(tema,tokens,temperatura)
print(articulo_creado)

original_con_saltos = input("Pega aquí el artículo que quieres resumir: ")
original  = original_con_saltos.replace("\n", " ")
tokens = int(input("Cuántas palabras maximas tendrá tu resumen: "))
temperatura = int(input("Del 1 al 10 que tan creativo quieres que sea tu resumen"))/10

resumen_creado = resumir_texto(original,tokens,temperatura)
print(resumen_creado)