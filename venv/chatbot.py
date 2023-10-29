import openai
import os
import spacy
import numpy as np
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

preguntas_anteriores = []
respuestas_anteriores = []
modelo_spacy = spacy.load("es_Core_news_md") #Modelo que procesa el lenguaje natural en español
palabras_prohibidas = ["palabra1","palabra2"]


def similitud_coseno(vec1,vec2): #Los textos se convierten mediante spacy en vectores.
    superposicion = np.dot(vec1,vec2)
    magnitud1 = np.linalg.norm(vec1)
    magnitud2 = np.linalg.norm(vec2)
    
    sim_cos = superposicion / (magnitud1 * magnitud2)
    return sim_cos

def es_relevante(respuesta,entrada,umbral=0.5):
    entrada_vectorizada = modelo_spacy(entrada).vector
    respuesta_vectorizada = modelo_spacy(respuesta).vector
    
    similitud = similitud_coseno(entrada_vectorizada,respuesta_vectorizada)
    return similitud >= umbral

def filtrar_lista_negra(texto,lista_negra):
    token = modelo_spacy(texto)
    resultado = []
    
    for t in token:
        if t.text.lower() not in lista_negra:
            resultado.append(t.text)
        else:
            resultado.append("[xxxx]")
            
    return " ".join(resultado)
            

def preguntar_chat_gpt(prompt,modelo="text-davinci-002"):
    respuesta = openai.Completion.create(
        engine = modelo,
        prompt = prompt,
        n = 1,
        max_tokens = 150,
        temperature = 1.5
    )
    respuestas_sin_filtro = respuesta.choices[0].text.strip()
    respuestas_filtradas = filtrar_lista_negra(respuestas_sin_filtro,palabras_prohibidas)
    return respuestas_filtradas


print("Bienvenido a nuestro chatbot básico. Escribe 'salir' cuando quieras terminar")

while True:
    convesacion_historica = ""
    ingreso_usuario = input("\nTú:")
    if ingreso_usuario.lower() == "salir":
        break
    
    for pregunta, respuesta in zip(preguntas_anteriores,respuestas_anteriores):
        convesacion_historica += f"El usuario pregunta: {pregunta}\n"
        convesacion_historica += f"ChatGPT responde: {respuesta}\n"
    
    prompt = f"El usuario pregunta: {ingreso_usuario}"
    convesacion_historica += prompt
    
    respuesta_gpt = preguntar_chat_gpt(convesacion_historica)
    
    relevante = es_relevante(respuesta,ingreso_usuario)
    
    if relevante:
        print(f"{respuesta_gpt}")
        preguntas_anteriores.append(ingreso_usuario)
        respuestas_anteriores.append(respuesta_gpt)
    else:
        print("La respuesta no es relevante")