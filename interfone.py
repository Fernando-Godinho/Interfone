import streamlit as st
import pandas as pd
import urllib.parse

# Função para carregar os dados do CSV e organizá-los em um dicionário
def carregar_dados():
    csv_path = 'interfone.csv'
    df = pd.read_csv(csv_path, delimiter=';', encoding='utf-8-sig')
    
    # Ajuste os nomes das colunas de acordo com o CSV
    col_predio = 'predio'
    col_apartamento = 'apartamento'
    col_nome = 'nome'
    col_telefone = 'telefone'
    
    dados_predios = {}
    for _, row in df.iterrows():
        predio = row[col_predio]
        apartamento = str(row[col_apartamento]).split('.')[0]  # Remove decimais
        nome = row[col_nome]
        telefone = row[col_telefone]
        
        if predio not in dados_predios:
            dados_predios[predio] = {}
        dados_predios[predio][apartamento] = {'nome': nome, 'telefone': telefone}
    
    return dados_predios

# Função para exibir os dados no Streamlit
def exibir_dados(dados_predios):
    st.title("Agenda Interfone")
    
    for predio, apartamentos in dados_predios.items():
        with st.expander(f"Prédio {predio}"):
            for apt, info in sorted(apartamentos.items()):
                apt_label = urllib.parse.quote(f"Apartamento {apt}")
                st.button(f"Apartamento {apt}", key=apt_label)
                st.write(f"Nome: {info['nome']}")
                st.write(f"Telefone: {info['telefone']}")

# Carrega os dados e exibe no Streamlit
dados_predios = carregar_dados()
exibir_dados(dados_predios)
