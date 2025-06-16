from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

# Substitua pela sua chave correta
openai.api_key = "SUA_CHAVE_AQUI"

@app.route("/consulta", methods=["POST"])
def consulta():
    data = request.get_json()

    if not data or "pergunta" not in data:
        return jsonify({"erro": "Formato inválido. Esperado JSON com chave 'pergunta'."}), 400

    pergunta = data["pergunta"]

    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é um advogado tributarista experiente. Responda com linguagem técnica, objetiva e sem dizer que é uma IA."},
                {"role": "user", "content": pergunta}
            ]
        )
        conteudo = resposta["choices"][0]["message"]["content"]
        return jsonify({"resposta": conteudo})
    
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
