
import streamlit as st
import pandas as pd
import urllib.parse

# Função para carregar os dados do CSV e organizá-los em um dicionário
def carregar_dados():
    csv_path = 'interfone.csv'
    df = pd.read_csv(csv_path, delimiter=';')
    
    # Ajuste os nomes das colunas de acordo com o CSV
    col_predio = 'predio'
    col_apartamento = 'apartamento'
    col_nome = 'nome'
    col_telefone = 'telefone'
    
    dados_predios = {}
    for _, row in df.iterrows():
        predio = row[col_predio]
        apartamento = str(row[col_apartamento]).split('.')[0]  # Remover a parte decimal do apartamento
        nome = row[col_nome]
        telefone = str(row[col_telefone]).split('.')[0]  # Remover a parte decimal do telefone
        
        if predio not in dados_predios:
            dados_predios[predio] = {}
        
        if apartamento not in dados_predios[predio]:
            dados_predios[predio][apartamento] = []
        
        dados_predios[predio][apartamento].append((nome, telefone))
    
    return dados_predios

# Função principal do app
def main():
    st.title("INTERFONE DIGITAL")
    st.subheader("Condomínio Quinta do Bosque III")

    # CSS para centralizar e definir o tamanho dos botões
    st.markdown("""
        <style>
        .center-button {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 10px;
        }
        .center-button button {
            width: 200px;
            height: 50px;
            font-size: 16px;
        }
        </style>
        """, unsafe_allow_html=True)

    # Carregar os dados do CSV
    dados_predios = carregar_dados()

    # Escolher o prédio
    predio = st.selectbox("Escolha o prédio:", list(dados_predios.keys()))

    if predio:
        # Escolher o apartamento
        apartamento = st.selectbox("Escolha o apartamento:", list(dados_predios[predio].keys()))
        
        if apartamento:
            # Mostrar os nomes e números de telefone
            st.subheader(f"Contatos do apartamento {apartamento}:")
            contatos = dados_predios[predio][apartamento]
            for nome, telefone in contatos:
                url_whatsapp = f"https://wa.me/55{telefone}"
                
                button_label = f"Abrir WhatsApp: {nome}"
                
                # Centralizar o botão e definir tamanho
                button_html = f"""
                <div class="center-button">
                    <a href="{url_whatsapp}" target="_blank">
                        <button>{button_label}</button>
                    </a>
                </div>
                """
                st.markdown(button_html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
