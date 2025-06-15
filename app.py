import openai
from flask import Flask, request, jsonify
from flask_cors import CORS

# Inicializa o app Flask
app = Flask(__name__)
CORS(app)

# Substitua abaixo com sua chave da OpenAI (com "Bearer" incluso)
OPENAI_API_KEY = "Bearer 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"

@app.route("/consulta", methods=["POST"])
def consulta():
    data = request.json
    pergunta = data.get("pergunta", "")

    if not pergunta:
        return jsonify({"erro": "Pergunta vazia"}), 400

    try:
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "Atue como um advogado tributarista experiente, com conhecimento atualizado sobre a Reforma Tributária (EC 132/2023, PLP 68/2024). Sempre cite, quando cabível, a base legal. Explique os conceitos de forma didática, se possível com exemplos, como se estivesse orientando empresários e contadores não especialistas."
                },
                {"role": "user", "content": pergunta}
            ],
            api_key=OPENAI_API_KEY
        )
        resposta = response.choices[0].message.content
        return jsonify({"resposta": resposta})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# Inicia o servidor Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
