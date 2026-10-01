# Author: Raphael Campos Squilaro
# Project: Access a Google Sheet

# -------- LIBRARIES --------
import streamlit as st # pip install streamlit
import pandas as pd # pip install pandas
import json
from google import genai # pip install google-genai

# -------- CONFIGURATIONS --------
with open("token.json", "r") as arquivo:
    dados = json.load(arquivo)

# Create a client for Google
client = genai.Client(api_key=dados["api_key"])

# -------- ID Of Sheet --------
PLANILHA_ID = dados["PLANILHA_ID"]

# -------- URL for reading of Pandas --------
url = f"https://docs.google.com/spreadsheets/d/{PLANILHA_ID}/export?format=xlsx"

# -------- INTERFACE --------

# Set title of the page
st.title("🤖 AGENTES DE IA - VENDAS")

# Reading sheet online
dados = pd.read_excel(url)

st.subheader("Dados da planilha")
st.dataframe(dados)

pergunta = st.text_input("O que deseja saber?")

if st.button ("Pergunte!") and pergunta:
    contexto = dados.to_string(index=False)

    prompt = f"""
    Você é um agente de análise de vendas.
    Responda à pergunta usando SOMENTE os dados da planilha abaixo.
    Planilha: {contexto}
    Pergunta: {pergunta}
    Responda de forma simples e direta.
    """

    resposta = client.models.generate_content(
        model= "gemini-3.5-flash-lite",
        contents= prompt
    )
    
    st.subheader("Respontas")
    st.write(resposta.text)
