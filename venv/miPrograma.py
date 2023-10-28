import os
import openai
import spacy
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

modelo = "text-davinci-002"
prompt = "Inventa poemas sobre C# incluyendo paises"

respuesta = openai.Completion.create(
    engine = modelo,
    prompt = prompt,
    n = 1, #cantidad de respuestas
    temperature=0.1, #alucinaciones
    max_tokens = 30 #cantidad de palabras
)

# for idx, opcion in enumerate(respuesta.choices): #Recorre las respuestas generadas
#     texto_generado = opcion.text.strip()
#     print(f"Respuesta {idx + 1}: {texto_generado}\n")

answer_text = respuesta.choices[0].text.strip()
print(answer_text)

print("***")


modelo_spacy = spacy.load("es_core_news_md")
analisis = modelo_spacy(answer_text)

# for token in analisis:
#     print(token.text)

# for ent in analisis.ents:
#     print(ent.text, ent.label_)

ubicacion = None

for ent in analisis.ents:
    if ent.label_ == "LOC":
        ubicacion = ent
        break
    
if ubicacion:
    prompt2 = f"Dime más sobre {ubicacion}"
    repuesta2 = openai.Completion.create (
        engine = modelo,
        prompt = prompt2,
        n = 1,
        max_tokens = 100
    )