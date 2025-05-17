# ✅ Instalação do pacote
!pip install -q google-generativeai

import os
from getpass import getpass
import google.generativeai as genai

# ✅ Coleta segura da API Key (não fica visível no Colab ou GitHub)
API_KEY = getpass("Cole sua API Key do Gemini aqui (ela não será salva): ")
genai.configure(api_key=API_KEY)

# ✅ Inicializa o modelo com chat (mantém o contexto)
model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

# ✅ Início da conversa terapêutica
print("Olá! Bem-vinde ao TerapI.A 🌿")
nome = input("Qual é o seu nome? ")
print(f"\nMuito prazer, {nome}! 💛")

print("\nAntes de começarmos, com quem você gostaria de conversar hoje?")
print("1. Thales (voz masculina empática)")
print("2. Felícia (voz feminina acolhedora)")
opcao = input("Digite 1 ou 2: ")

bot_nome = "Thales" if opcao == "1" else "Felícia"
print(f"\nPerfeito! {bot_nome} está aqui com você agora. Vamos conversar com calma e segurança, tudo bem? 🤗")

print(f"\n{bot_nome}: Antes de tudo, gostaria de entender um pouquinho como você tem se sentido nos últimos 30 dias.")
sintomas = {}

sintomas["ansiedade"] = input("\nVocê tem sentido ansiedade com frequência? Como ela se manifesta para você? ")
sintomas["depressao"] = input("\nVocê tem se sentido triste, sem energia ou desmotivado na maior parte do tempo? ")
sintomas["tdah"] = input("\nVocê sente dificuldade em se concentrar, manter o foco ou controlar impulsos? ")
sintomas["luto"] = input("\nVocê está passando ou passou recentemente por alguma perda importante? Como tem lidado com isso? ")
sintomas["ideacao_suicida"] = input("\nVocê já teve pensamentos relacionados à morte ou desistência da vida nos últimos dias? ")

if "sim" in sintomas["ideacao_suicida"].lower() or "já" in sintomas["ideacao_suicida"].lower():
    print("\n⚠️ Isso é muito importante. Você não está sozinhx. Se estiver em perigo, ligue gratuitamente para o CVV – 188. ❤️")

print(f"\n{bot_nome}: Obrigado por compartilhar isso comigo, {nome}. Agora, o espaço é seu. 🌼")
print("Pode me contar qualquer coisa que esteja pesando no seu coração. Estou aqui para ouvir, sem julgamentos.\n")

# ✅ Loop da conversa terapêutica
while True:
    entrada = input(f"{nome}: ")
    if entrada.lower() in ["sair", "obrigado", "tchau", "pare"]:
        print(f"\n{bot_nome}: Foi um prazer te ouvir, {nome}. Volte sempre que quiser conversar. Cuide-se com carinho. 💛")
        break

    prompt = f"""
Você é {bot_nome}, uma inteligência artificial terapêutica acolhedora, gentil e empática.
Está conversando com {nome}, uma pessoa que está enfrentando desafios emocionais e precisa ser ouvida com carinho.
Responda com escuta ativa, conselhos suaves, empatia profunda e incentivo para continuar desabafando.

A pessoa disse:
\"\"\"{entrada}\"\"\"

Sua resposta (com empatia e acolhimento):
"""

    try:
        response = chat.send_message(prompt)
        print(f"\n{bot_nome}: {response.text.strip()}\n")
    except Exception as e:
        print(f"\n{bot_nome}: Houve um problema ao tentar responder agora. Erro técnico: {repr(e)}\n")
