#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random

def exibeResposta_GUI(texto, resposta, nome):
    # Assuming resposta is a string or an object that has a .resposta method
    return resposta  # This may need to be adjusted based on your actual implementation

def saudacao_GUI(nome):
    frases = [
        'Bom dia! Meu nome é ' + nome + '. Como vai você?',
        'Olá!',
        'Oi, tudo bem?'
    ]
    return random.choice(frases)  # Passando a lista de frases

def salva_sugestao(sugestao):
    with open('BaseDeConhecimento.txt', 'a+') as conhecimento:
        conhecimento.write('Chatbot: ' + sugestao + '\n')

def buscaResposta_GUI(texto):
    with open('BaseDeConhecimento.txt', 'r') as conhecimento:
        for linha in conhecimento:
            if jaccard(texto, linha) > 0.3:
                prox_linha = conhecimento.readline()
                if "Chatbot:" in prox_linha:
                    return prox_linha.strip()
        with open('BaseDeConhecimento.txt', 'a+') as conhecimento:
            conhecimento.write('Chatbot: ' + texto + '\n')
        return "Me desculpe, não sei o que falar"

def jaccard(textoUsuario, textoBase):
    textoUsuario = limpa_frase(textoUsuario)
    textoBase = limpa_frase(textoBase)
    if len(textoBase) < 1:
        return 0
    palavras_usuario = textoUsuario.split()
    palavras_base = textoBase.split()
    palavras_em_comum = sum(1 for palavra in palavras_usuario if palavra in palavras_base)
    return palavras_em_comum / len(palavras_base)

def limpa_frase(frase):
    tirar = ["?", "!", "...", ".", ",", "Cliente: ", "\n"]
    for t in tirar:
        frase = frase.replace(t, "")
    return frase.upper()


# In[ ]:




