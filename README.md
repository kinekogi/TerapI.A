
# 🌿 TerapI.A – Inteligência Artificial para Apoio Emocional

**TerapI.A** é uma iniciativa que utiliza inteligência artificial para oferecer suporte emocional e psicológico acessível a todas as pessoas. Nosso objetivo é ajudar quem não tem acesso a terapias convencionais, fornecendo um espaço seguro para desabafos, conselhos e técnicas validadas da psicologia.

> ⚠️ **TerapI.A não substitui atendimento psicológico ou psiquiátrico profissional.**  
> Em caso de emergência, procure ajuda médica ou entre em contato com o **CVV – 188** (gratuito, sigiloso e disponível 24h).

---

## ✨ Funcionalidades

- 🧠 **Chat com IA empática**, baseada em técnicas comprovadas da psicologia.
- 🌬️ Orientação sobre **técnicas de respiração e relaxamento**.
- 💬 Possibilidade de **desabafar livremente ou pedir conselhos**.
- 📞 Encaminhamento para **serviços de emergência emocional** como o CVV (188).
- 🙋‍♀️ Escolha do tipo de atendente (voz feminina ou masculina da IA).
- 📆 Respostas personalizadas com base nos **sintomas relatados nos últimos 30 dias**.

---

## 🚀 Como usar no Google Colab

1. Acesse o notebook TerapI.A no Google Colab.
2. Execute todas as células.
3. Cole sua **API Key do Google Gemini** no campo seguro quando solicitado.
4. Escolha com quem deseja conversar (Thales ou Felícia).
5. Siga o fluxo de perguntas e inicie sua conversa com a IA.

---

## 💡 Exemplos do que você pode dizer

- "Estou me sentindo ansioso todos os dias antes de dormir."
- "Quero aprender a controlar melhor a minha respiração."
- "Não sei com quem conversar, posso desabafar aqui?"

---

## 🔐 Segurança da API

Este projeto **NÃO armazena nem expõe sua chave da API**.  
A chave é solicitada de forma segura com `getpass()` e **não deve ser incluída diretamente no código**.

### ✅ Correto:
```python
from getpass import getpass
API_KEY = getpass("Cole sua API Key do Gemini aqui: ")
```

---

## 🤝 Agradecimentos

Este projeto foi inspirado e desenvolvido com base na **Imersão IA da [Alura](https://www.alura.com.br/)**, que tornou acessível o uso de tecnologias de ponta de forma criativa e humana.  

Também agradecemos à equipe do **Google Gemini** pelo desenvolvimento de uma API poderosa que possibilita interações mais empáticas e naturais com inteligência artificial.

Gratidão a todas as pessoas envolvidas no movimento por uma IA mais acolhedora e voltada para o bem-estar mental. 🌼💛


## 🔐 Segurança da API

Este projeto **NÃO armazena nem expõe sua chave da API**.  
A chave é solicitada de forma segura com `getpass()` e **não deve ser incluída diretamente no código**.

### ✅ Correto:
```python
API_KEY = getpass("Cole sua API Key do Gemini aqui: ")
