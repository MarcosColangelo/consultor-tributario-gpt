from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# 🔐 Carregando chave secreta do ambiente do Render
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/consulta", methods=["POST"])
def consulta():
    data = request.get_json()
    pergunta = data.get("pergunta", "")

    resposta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é um advogado tributarista experiente. Responda com base na EC 132/2023 e no PLP 68/2024."},
            {"role": "user", "content": pergunta}
        ]
    )

    return jsonify({
        "resposta": resposta.choices[0].message.content
    })

# 🔽 Rodando na porta 3000 e ouvindo em 0.0.0.0 (como o Render exige)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
