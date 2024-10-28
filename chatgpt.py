import openai  # Importa la llibreria d'OpenAI

openai.api_key = "LA_TEVA_API_KEY"  # Configura la clau d'API que podem trobar al nostre perfil de ChatGPT

def consulta_chatgpt(pregunta):
    # Crea una sol·licitud a l'API de ChatGPT
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Defineix el model 
        messages=[{"role": "user", "content": pregunta}],  # Estableix el missatge com a rol d'usuari
        max_tokens=200,  # Longitud de la resposta
        temperature=0.8  # Creativitat (0 = respostes precises, 1 = més creatives)
    )
    return resposta['choices'][0]['message']['content']  # Retorna només el text de la resposta

# Pregunta i resposta
pregunta = input("Introdueix la teva pregunta per a ChatGPT: ")
print("ChatGPT:", consulta_chatgpt(pregunta))
