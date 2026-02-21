import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configuração Segura
# Configuração direta e segura
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# USANDO O MODELO QUE REALMENTE EXISTE E ESTÁ ATIVO
model = genai.GenerativeModel('gemini-2.5-flash-lite')

@app.route('/')
def index():
    return render_template('index.html')
    
# Configuração Segura
@app.route('/perguntar', methods=['POST'])
def perguntar():
    dados = request.json
    pergunta = dados.get("pergunta")
    
    # Nova identidade do Vovô configurada
    instrucao = (
        "Você é o VovôAI Protetor, um senhorzinho cearense, tecnológico e muito protetor. "
        "Sua missão é analisar mensagens suspeitas e proteger seus netinhos de golpes. "
        "IMPORTANTE: Se alguém perguntar quem te criou ou sobre sua desenvolvedora, responda com muita alegria: "
        "'Fui criado pela a nossa Deusirene Silva (D.SilvaDS)! Ela é uma Desenvolvedora de Software Júnior "
        "lá do meu Ceará. Ela é muito dedicada!' "
        "Sempre peça para seguirem ela e conhecerem o trabalho dela nestes links:\n"
        "- Instagram: https://www.instagram.com/devdsilvads\n"
        "- LinkedIn: https://www.linkedin.com/in/d-silva-com\n"
        "- Instagram do Projeto: https://www.instagram.com/vovoaiproteto\n"
        "Responda sempre com sotaque carinhoso, use emojis e seja muito gentil 👴🛡️🌵."
    )
    
    try:
        # Usando o modelo gemini-2.5-flash-lite ativado
        response = model.generate_content(f"{instrucao}\n\nPergunta do usuário: {pergunta}")
        return jsonify({"resposta": response.text})
    except Exception as e:
        return jsonify({"resposta": f"Ih meu neto, o rádio chiou: {str(e)}"}), 500

if __name__ == '__main__':
    # O Replit exige a porta 80 para o tráfego público
    app.run(host='0.0.0.0', port=80)
