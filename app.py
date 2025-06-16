import os
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Obtém a chave da OpenAI do ambiente
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/consulta", methods=["POST"])
def consulta():
    try:
        data = request.get_json()
        pergunta = data.get("pergunta", "")

        resposta = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é um advogado tributarista experiente. Responda com base na EC 132/2023 e PLP 68/2024."},
                {"role": "user", "content": pergunta}
            ]
        )

        conteudo = resposta.choices[0].message.content
        return jsonify({"resposta": conteudo})

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# Executa localmente na porta 3000 (ignorada na Render)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
