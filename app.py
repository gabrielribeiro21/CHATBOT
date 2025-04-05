from flask import Flask, render_template, request
import openai

# realizei o projeto sem a chave, no intuito de praticar a estrutura do código
openai.api_key = "sua-chave-aqui"

app = Flask(__name__)

historico = []

@app.route("/", methods=["GET", "POST"])
def index():
    resposta = ""
    if request.method == "POST":
        pergunta = request.form["mensagem"]
        historico.append({"role": "user", "content": pergunta})

        resposta_api = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=historico,
            max_tokens=300
        )
        resposta = resposta_api.choices[0].message["content"]
        historico.append({"role": "assistant", "content": resposta})
    
    return render_template("index.html", resposta=resposta)

if __name__ == "__main__":
    app.run(debug=True)
