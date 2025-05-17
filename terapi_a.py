!pip install gradio
!pip install google-generativeai

# ✅ Importação das bibliotecas
import gradio as gr
from getpass import getpass
import google.generativeai as genai

# ✅ Coleta segura da API Key
def obter_api_key():
    """
    Função para obter a API Key do Gemini de forma segura.
    """
    api_key = getpass("Cole sua API Key do Gemini aqui (ela não será salva): ")
    return api_key

# ✅ Configuração da API do Gemini
def configurar_gemini(api_key):
    """
    Função para configurar a API do Gemini com a chave fornecida.

    Args:
        api_key (str): A API Key do Gemini.
    """
    genai.configure(api_key=api_key)

# ✅ Inicialização do modelo do Gemini
def inicializar_modelo():
    """
    Função para inicializar o modelo de geração de texto do Gemini.

    Returns:
        genai.GenerativeModel: O modelo do Gemini inicializado.
    """
    modelo = genai.GenerativeModel("gemini-2.0-flash")
    return modelo

# Declare global variables that will be used by Gradio functions
global nome_usuario, bot_nome, sintomas, chat, modelo # Added modelo here

# Initialize chat and modelo to None initially
chat = None
modelo = None

# ✅ Função para iniciar a conversa
def iniciar_conversa(nome, opcao, ans, dep, tdah, luto, suicida): # Removed modelo as an argument
    """
    Função para iniciar a conversa com o bot.

    Args:
        nome (str): Nome do usuário.
        opcao (str): Opção de bot ("Thales" ou "Felícia").
        ans (str): Resposta sobre ansiedade.
        dep (str): Resposta sobre tristeza ou desmotivação.
        tdah (str): Resposta sobre foco e concentração.
        luto (str): Resposta sobre perdas recentes.
        suicida (str): Resposta sobre pensamentos de desistência.
        # Removed modelo from args
    Returns:
        str: Mensagem de boas-vindas formatada.
    """
    global nome_usuario, bot_nome, sintomas, chat, modelo # Access global modelo

    # Ensure modelo is initialized before using it
    if modelo is None:
        raise ValueError("O modelo do Gemini não foi inicializado corretamente.")

    nome_usuario = nome
    bot_nome = "Thales" if opcao == "Thales" else "Felícia"

    sintomas = {
        "ansiedade": ans,
        "depressao": dep,
        "tdah": tdah,
        "luto": luto,
        "ideacao_suicida": suicida
    }

    alerta = ""
    if "sim" in suicida.lower() or "já" in suicida.lower():
        alerta = "⚠️ Isso é muito importante. Você não está sozinhx. Se estiver em perigo, ligue para o CVV – 188. ❤️"

    boas_vindas = (
        f"{bot_nome}: Muito prazer, {nome}! 🌿\n\n"
        "Estou aqui para te ouvir, com carinho. Pode começar a desabafar quando quiser."
    )

    chat = modelo.start_chat()  # Initialize the chat using the global modelo
    return f"{alerta}\n\n{boas_vindas}".strip()



# ✅ Função para responder à mensagem da pessoa usuária
def responder_ia(mensagem_usuario, historico_chat):
    """
    Função para gerar a resposta da IA à mensagem do usuário.

    Args:
        mensagem_usuario (str): A mensagem do usuário.
        historico_chat (list): O histórico da conversa até o momento (managed by ChatInterface).

    Returns:
        str: A resposta da IA.
    """
    global chat, nome_usuario, bot_nome, modelo # Access global modelo

    print(f"Função responder_ia chamada com mensagem: '{mensagem_usuario}'")
    print(f"Histórico do chat recebido: {historico_chat}")

    # Ensure modelo is initialized before using it
    if modelo is None:
        print("Erro: Modelo da IA não disponível.")
        return "Erro interno: Modelo da IA não disponível."

    # The chat object is initialized in iniciar_conversa.
    # Gradio's ChatInterface manages the history and passes it.
    # We don't need to re-initialize chat or pass history to start_chat here.
    if chat is None:
        print("Erro: Objeto 'chat' não inicializado.")
        return "Erro: Converse com a IA primeiro clicando em 'Iniciar Conversa'."


    if mensagem_usuario.lower() in ["sair", "tchau", "pare", "obrigado"]:
        resposta = f"{bot_nome}: Foi um prazer te ouvir, {nome_usuario}. Volte sempre que quiser conversar. 💛"
        print(f"Resposta de saída gerada: '{resposta}'")
        return resposta

    prompt = f"""
Você é {bot_nome}, uma inteligência artificial terapêutica acolhedora, gentil e empática.
Está conversando com {nome_usuario}, uma pessoa que está enfrentando desafios emocionais e precisa ser ouvida com carinho.
Responda com escuta ativa, conselhos suaves, empatia profunda e incentivo para continuar desabafando.

A pessoa disse:
\"\"\"{mensagem_usuario}\"\"\"
"""
    print(f"Prompt enviado para o modelo:\n{prompt}")
    try:
        # Send the message. ChatInterface automatically handles history.
        response = chat.send_message(prompt)
        resposta_ia = response.text
        print(f"Resposta da IA recebida: '{resposta_ia}'")
        # Return only the text response. ChatInterface appends to the history.
        return resposta_ia

    except Exception as e:
        erro = f"{bot_nome}: Desculpe, houve um erro técnico: {repr(e)}"
        print(f"Erro ao obter resposta da IA: {erro}")
        # Return an error message if something goes wrong
        return erro


# ✅ Criação da interface Gradio com os blocos individuais
def construir_interface_blocos():
    cor_fundo_principal = "#c7b18d"
    cor_texto_verde_escuro = "#2E8B57"
    cor_verde_destaque = "#556B2F"
    cor_verde_secundario_bordas = "#6B8E23"
    cor_verde_super_claro_inputs = "#F0FFF0"
    cor_texto_branco = "#FFFFFF"
    cor_verde_claro_alternativo = "#98FB98"

    with gr.Blocks(
        title="TerapI.A 🌿",
        theme=gr.themes.Soft(primary_hue=gr.themes.colors.green)
    ) as demo:
        # Start of CSS head
        demo.head += f"""
<style>
/* Cor de fundo geral da página e container principal do Gradio */
body, .gradio-container {{
    background-color: {cor_fundo_principal} !important;
    color: {cor_texto_verde_escuro} !important; /* Cor de texto padrão */
    font-family: 'Inter', sans-serif;
}}

/* Títulos principais e textos de markdown */
.prose h1, .prose h3, .gr-markdown p {{
    color: {cor_texto_verde_escuro} !important;
}}
.gr-markdown div {{ /* Para os divs de centralização */
    color: {cor_texto_verde_escuro} !important;
}}

/* Caixas de texto (Textbox) e seus labels */
.gr-form .gr-block-label > span, /* Labels de blocos como Textbox, Radio */
.gr-form .gr-checkbox-label span {{ /* Labels de checkboxes, se houver */
    color: {cor_texto_verde_escuro} !important;
    font-weight: 500 !important;
}}

.gr-textbox textarea, .gr-textbox input {{
    background-color: {cor_verde_super_claro_inputs} !important;
    border: 1px solid {cor_verde_secundario_bordas} !important;
    color: {cor_texto_verde_escuro} !important;
    border-radius: 8px !important;
}}
.gr-textbox textarea:focus, .gr-textbox input:focus {{
    border-color: {cor_verde_destaque} !important;
    box-shadow: 0 0 0 2px rgba(85, 107, 47, 0.25) !important; /* Sombra verde no foco */
}}

/* Botões (Button) */
.gr-button {{
    background-color: {cor_verde_destaque} !important; /* Verde destaque para o fundo */
    color: {cor_texto_branco} !important; /* Texto branco */
    border: none !important;
    border-radius: 8px !important;
    padding: 10px 18px !important;
    font-weight: 500 !important;
    transition: background-color 0.2s ease-in-out, transform 0.1s ease;
}}
.gr-button:hover {{
    background-color: {cor_verde_secundario_bordas} !important; /* Tom mais claro ou diferente no hover */
    transform: translateY(-1px);
}}
.gr-button:active {{
    transform: translateY(0px);
}}

/* Componente Radio */
.gr-radio .gr-input-choice {{
    border: 1px solid {cor_verde_secundario_bordas} !important;
    background-color: {cor_verde_super_claro_inputs} !important; /* Fundo verde super claro */
    color: {cor_texto_verde_escuro} !important; /* Texto verde escuro */
    border-radius: 8px !important;
    margin-bottom: 5px !important;
}}
.gr-radio .gr-input-choice.selected {{
    background-color: {cor_verde_destaque} !important; /* Fundo verde destaque */
    color: {cor_texto_branco} !important; /* Texto branco */
    border-color: {cor_verde_destaque} !important;
}}

/* Chatbot */
.chatbot-container {{
    height: 400px; /* This line should be treated as literal text */
    overflow-y: auto;
    border: 1px solid {cor_verde_secundario_bordas};
    border-radius: 8px;
    padding: 10px;
    background-color: #f9f9f9;
}}
.chatbot-message {{
    padding: 8px 12px;
    border-radius: 10px;
    margin-bottom: 8px;
    max-width: 75%;
    word-wrap: break-word;
}}
.user-message {{
    background-color: {cor_verde_claro_alternativo};
    color: {cor_texto_verde_escuro};
    align-self: flex-end;
}}
.bot-message {{
    background-color: {cor_verde_destaque};
    color: {cor_texto_branco};
    align-self: flex-start;
}}
.message-row {{
    display: flex;
    width: 100%;
    margin-bottom: 5px;
}}
.user-row {{
    justify-content: flex-end;
}}
.bot-row {{
    justify-content: flex-start;
}}

</style>
"""
        # End of CSS head

        gr.Markdown("<div style='display: flex; justify-content: center;'><h1 style='font-size: 2.5em; font-weight: 600;'>🌿 TerapI.A</h1></div>")
        gr.Markdown("<div style='display: flex; justify-content: center; font-size: 1.1em;'>Inteligência Artificial para Apoio Emocional</div>")
        gr.Markdown("Bem-vinde! Preencha abaixo como tem se sentido e inicie uma conversa com Thales ou Felícia.")

        with gr.Row():
            nome_input = gr.Textbox(label="Seu nome", placeholder="Digite seu nome")
            opcao_bot = gr.Radio(choices=["Thales", "Felícia"], label="Escolha quem vai te atender:", value="Thales")

        ans = gr.Textbox(label="Ansiedade", placeholder="Você sente ansiedade com frequência? Como ela se manifesta?", lines=2)
        dep = gr.Textbox(label="Tristeza ou desmotivação", placeholder="Você se sente sem energia ou motivado(a)?", lines=2)
        tdah = gr.Textbox(label="Foco e concentração", placeholder="Tem tido dificuldades com foco, impulsividade ou inquietação?", lines=2)
        luto = gr.Textbox(label="Perdas recentes", placeholder="Você passou por alguma perda importante recentemente? Como tem lidado?", lines=2)
        suicida = gr.Textbox(label="Pensamentos de desistência", placeholder="Nos últimos dias, você teve pensamentos sobre morte, em desistir ou que a vida não vale a pena?", lines=2)

        botao_iniciar = gr.Button("Iniciar Conversa")
        saida_boasvindas = gr.Textbox(label="Mensagem de boas-vindas:", lines=4, interactive=False)

        # Use the modified responder_ia that returns only text
        botao_iniciar.click(
            iniciar_conversa,
            inputs=[nome_input, opcao_bot, ans, dep, tdah, luto, suicida],
            outputs=saida_boasvindas
        )

        gr.Markdown("### 💬 Agora você pode conversar com sua IA terapêutica abaixo:")
        # Use gr.Chatbot directly and pass the function to ChatInterface
        chatbot_interface = gr.ChatInterface(
            fn=responder_ia, # responder_ia function is suitable for ChatInterface
            chatbot=gr.Chatbot(label="Conversa", height=450, bubble_full_width=False),
            textbox=gr.Textbox(placeholder="Escreva sua mensagem aqui...", label="Você:", scale=7),
            submit_btn="Enviar",
            # The 'clear_btn' argument is valid for ChatInterface.
            # Re-adding it as it was removed in the user's last code block.
            clear_btn="Limpar Conversa"
        )
    return demo

# ✅ Executa o app
if __name__ == "__main__":
    api_key = obter_api_key()
    configurar_gemini(api_key)
    modelo = inicializar_modelo()
    # Call the function that uses ChatInterface
    app = criar_interface()
    app.launch(share=True)
