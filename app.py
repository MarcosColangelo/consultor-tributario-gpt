import openai
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

openai.api_key = "SUA_CHAVE_AQUI"  # Substitua por sua chave da OpenAI

@app.route("/consulta", methods=["POST"])
def consulta():
    data = request.json
    pergunta = data.get("pergunta", "")
    if not pergunta:
        return jsonify({"erro": "Pergunta vazia"}), 400
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Responda como um advogado tributarista."},
                {"role": "user", "content": pergunta}
            ]
        )
        resposta = response.choices[0].message.content
        return jsonify({"resposta": resposta})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
