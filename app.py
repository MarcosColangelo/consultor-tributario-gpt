import os
import openai
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Pegando a chave da variável de ambiente
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/consulta", methods=["POST"])
def consulta():
    data = request.get_json()
    pergunta = data.get("pergunta", "")

    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é um advogado tributarista experiente. Responda com base na EC 132/2023 e PLP 68/2024"},
                {"role": "user", "content": pergunta}
            ]
        )
        return jsonify({"resposta": resposta.choices[0].message.content})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
