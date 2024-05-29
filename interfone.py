import streamlit as st
import pandas as pd
import urllib.parse

# Função para carregar os dados do CSV e organizá-los em um dicionário
def carregar_dados():
    csv_path = 'interfone.csv'
    df = pd.read_csv(csv_path, delimiter=';', dtype={"apartamento": float}, na_values='')
    
    # Ajuste os nomes das colunas de acordo com o CSV
    col_predio = 'predio'
    col_apartamento = 'apartamento'
    col_nome = 'nome'
    col_telefone = 'telefone'
    
    dados_predios = {}
    for _, row in df.iterrows():
        predio = str(row[col_predio])
        apartamento = int(row[col_apartamento])  # Convertendo para inteiro e depois para string
        nome = row[col_nome]
        telefone = str(row[col_telefone])
        
        if predio not in dados_predios:
            dados_predios[predio] = {}
        
        if apartamento not in dados_predios[predio]:
            dados_predios[predio][apartamento] = []
        
        dados_predios[predio][apartamento].append((nome, telefone))
    
    return dados_predios

# Função principal do app
def main():
    st.title("App de Entregas do Motoboy")

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
                url_whatsapp = f"https://wa.me/{urllib.parse.quote(telefone)}"
                st.write(url_whatsapp)
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
