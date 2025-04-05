import openai

# Aqui você substitui pela sua chave secreta da OpenAI
openai.api_key = "sua-chave-aqui"

def conversar_com_gpt(mensagem_usuario, historico=[]):
    historico.append({"role": "user", "content": mensagem_usuario})
    
    resposta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=historico
    )
    
    resposta_gpt = resposta.choices[0].message['content']
    historico.append({"role": "assistant", "content": resposta_gpt})
    
    return resposta_gpt, historico

# Loop de conversa
if __name__ == "__main__":
    historico_conversa = []
    print("Chatbot GPT-4 🤖 (digite 'sair' para encerrar)")
    
    while True:
        mensagem = input("Você: ")
        if mensagem.lower() in ["sair", "exit", "quit"]:
            print("Bot: Até a próxima! 👋")
            break
        resposta, historico_conversa = conversar_com_gpt(mensagem, historico_conversa)
        print(f"Bot: {resposta}")