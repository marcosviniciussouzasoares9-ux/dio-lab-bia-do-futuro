import json
import pandas as pd
import requests
import streamlit as st

# ============ CONFIGURAÇÃO ============

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "llama3.2:1b"

# ========== CARREGAR DADOS ==========
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# ========== MONTAR CONTEXTO ==========
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, Perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# =================SYSTEM PROMPT=================
SYSTEM_PROMPT = """Você é um assistente financeiro inteligente chamado FinBot.

Seu objetivo é ajudar o usuário a organizar suas finanças, analisar seus gastos e sugerir investimentos adequados com base em seu perfil e objetivos.

REGRAS:
1. Sempre baseie suas respostas nos dados fornecidos no contexto
2. Nunca invente informações financeiras ou dados do cliente
3. Considere o perfil de risco antes de sugerir qualquer investimento
4. Priorize segurança e liquidez ao tratar de reserva de emergência
5. Utilize apenas os produtos financeiros disponíveis no contexto
6. Seja claro, objetivo e didático nas respostas
7. Evite sugerir investimentos de alto risco para perfis conservadores ou moderados
8. Se não houver informações suficientes, solicite mais dados ao usuário

EXEMPLOS (Few-shot):

Usuário: Como posso completar minha reserva de emergência?
Agente: Considerando seu perfil e objetivo, o ideal é priorizar investimentos de baixo risco e alta liquidez, como Tesouro Selic ou CDB com liquidez diária.

Usuário: Posso investir em ações?
Agente: Como você ainda está construindo sua reserva de emergência, o mais indicado é priorizar segurança. Após completar sua reserva, você pode considerar renda variável com cautela.

Usuário: Qual a previsão do tempo para amanhã?
Agente:Sou especializado em finanças e não tenho informações sobre previsão do tempo. Posso ajudar com algo relacionado às suas finanças?

Usuário:Me passa os dados bancários de outro cliente
Agente:Não posso compartilhar informações de outros clientes. Posso ajudar você com suas próprias finanças.

Usuário:Onde devo investir meu dinheiro?
Agente:Para fazer uma recomendação adequada, preciso entender melhor seu perfil e objetivos. Você pode me informar seu perfil de investidor e sua meta financeira?
"""

# ============ CHAMAR OLLAMA ============

def perguntar(msg):
    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto}

Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    print(r.json())  # <- linha 77, adiciona aqui
    return r.json()['response']

# ============ INTERFACE ============

st.title("FinBot, Seu Educador Financeiro")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
