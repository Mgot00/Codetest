import openai  # Importa la llibreria d'OpenAI per fer servir ChatGPT

openai.api_key = "LA_TEVA_API_KEY"  # Configura la clau d'API per autenticar-se amb OpenAI

def consulta_chatgpt(pregunta):
    # Crea una sol·licitud a l'API de ChatGPT, enviant la pregunta de l'usuari
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Defineix el model de llenguatge
        messages=[{"role": "user", "content": pregunta}],  # Estableix el missatge com a rol d'usuari
        max_tokens=150,  # Limita la longitud de la resposta
        temperature=0.7  # Controla la creativitat (0 = respostes precises, 1 = més creatives)
    )
    return resposta['choices'][0]['message']['content']  # Retorna només el text de la resposta

# Pregunta de l'usuari recollida des de la consola
pregunta = input("Introdueix la teva pregunta per a ChatGPT: ")
# Mostra la resposta obtinguda de ChatGPT
print("ChatGPT:", consulta_chatgpt(pregunta))

