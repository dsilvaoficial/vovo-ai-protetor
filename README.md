# 👴🛡️ VovôAI Protetor: Inteligência Artificial contra Golpes Financeiros

O **VovôAI Protetor** é uma solução de impacto social que utiliza Processamento de Linguagem Natural (PLN) para proteger pessoas em situação de vulnerabilidade digital — especialmente idosos — contra fraudes, golpes de engenharia social e mensagens maliciosas.

---

## 📖 Sobre o Projeto
Muitas vezes, idosos são alvos de criminosos virtuais devido à linguagem complexa e táticas de pressão psicológica. O VovôAI atua como um tradutor de segurança: ele recebe mensagens suspeitas, analisa o contexto e responde de forma didática, utilizando um sotaque cearense acolhedor para quebrar a barreira técnica e gerar confiança no usuário.

### Como funciona:
1. **Entrada de Dados**: O usuário cola uma mensagem suspeita (SMS, WhatsApp ou E-mail) na interface.
2. **Análise Heurística e Semântica**: O sistema envia o texto para o modelo Gemini da Google, que avalia padrões comuns de golpes (links falsos, urgência artificial, pedidos de dinheiro).
3. **Resposta Humanizada**: A IA não apenas diz "é golpe", mas explica *por que* aquilo é perigoso e como o usuário deve proceder.

---

## 🛠️ Arquitetura Técnica

O projeto foi estruturado seguindo as melhores práticas de desenvolvimento web com Python:

* **Backend**: Desenvolvido em **Python** utilizando o micro-framework **Flask**, garantindo uma aplicação leve e escalável.
* **Inteligência Artificial**: Integração com a **Google Gemini API** (`gemini-2.5-flash-lite`), configurada com instruções de sistema (System Instructions) para manter uma persona consistente e segura.
* **Segurança de Dados**: Implementação de **Variáveis de Ambiente (`os.environ`)** para gestão de credenciais. As chaves de API são armazenadas em segredo (Secrets), impedindo o vazamento de dados sensíveis em repositórios públicos.
* **Frontend**: Interface responsiva construída com **HTML5** e **CSS3**, organizada em diretórios padrões (`templates/` e `static/`).

---

## ⚙️ Configuração do Ambiente

Para rodar este projeto localmente ou em um ambiente de nuvem:

1. Instale as dependências: `pip install -r requirements.txt`
2. Configure a variável de ambiente `GEMINI_API_KEY` com sua chave da Google AI Studio.
3. Execute o comando: `python main.py`

---

## 🔗 Demonstração e Contatos

* **Aplicação em Nuvem**: [Acesse o VovôAI Protetor](https://vovo-ai-protetor--deusirenee.replit.app)
* **Instagram do Projeto**: [@vovoaiproteto](https://www.instagram.com/vovoaiproteto)
* **Instagram Dev**: [@devdsilvads](https://www.instagram.com/devdsilvads)
* **LinkedIn Profissional**: [D-Silva-com](https://www.linkedin.com/in/d-silva-com)

---
*Este projeto é parte do meu portfólio como Desenvolvedora de Software Júnior, focado em ética na IA e acessibilidade digital.*
