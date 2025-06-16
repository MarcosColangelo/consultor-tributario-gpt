from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/consulta", methods=["POST"])
def consulta():
    data = request.get_json()
    pergunta = data.get("pergunta", "")
    resposta = f"Sua pergunta foi: {pergunta}"
    return jsonify({"resposta": resposta})

@app.route("/saudacao", methods=["GET"])
def saudacao():
    return "Olá, tudo certo! API está funcionando com sucesso ✅"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
