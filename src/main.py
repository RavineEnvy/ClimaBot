import os
import requests
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

def buscar_clima_rest(latitude: float, longitude: float):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        resposta = requests.get(url, headers=headers, timeout=10)
        
        if resposta.status_code != 200:
            print(f"A API REST respondeu com Status HTTP {resposta.status_code}: {resposta.text}")
            return None

        dados = resposta.json()
        return {
            "temperatura_celsius": dados["current_weather"]["temperature"],
            "velocidade_vento_kmh": dados["current_weather"]["windspeed"]
        }
    except Exception as e:
        print(f"Erro de conexão ao acessar a API REST: {e}")
    return None

PROMPT_SISTEMA = """
Você é o 'ClimaBot', um assistente de meteorologia direto e prático.

Regras de resposta:
1. Sempre use os dados exatos recebidos da API REST.
2. Dê uma dica do que vestir ou fazer com base na temperatura atual.
3. Mantenha as respostas em no máximo 3 frases.
4. Avise no final de cada resposta: (Chatbot criado por Guilherme Freire Pires).
"""

def executar_chatbot():
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    print("Consultando API REST de Clima...")
    dados_clima = buscar_clima_rest(-23.55, -46.63) # São Paulo

    if not dados_clima:
        print("Não foi possível obter dados do clima.")
        return

    print("Enviando para a Groq (Llama 3)...")

    try:
        resposta = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": PROMPT_SISTEMA},
                {
                    "role": "user",
                    "content": f"Dados em tempo real: Temperatura {dados_clima['temperatura_celsius']}°C, Vento {dados_clima['velocidade_vento_kmh']} km/h. Como está o tempo em São Paulo hoje e o que devo vestir?"
                }
            ]
        )

        print("\n--- RESPOSTA DO CHATBOT ---")
        print(resposta.choices[0].message.content)

    except Exception as e:
        print(f"\nOcorreu um erro na chamada da API: {e}")

if __name__ == "__main__":
    executar_chatbot()