import logging
import streamlit as st
from infrastructure.logging_config import setup_logging
from application.authenticate_kaggle import authenticate_kaggle_case
from application.analyze_dataset import analyze_dataset_case

# Configurações do logging
setup_logging()


def truncate_log_file(log_file_path, max_lines=10000):
    try:
        with open(log_file_path, "r") as log_file:
            lines = log_file.readlines()

        if len(lines) > max_lines:
            with open(log_file_path, "w") as log_file:
                log_file.writelines(lines[-max_lines:]) 
    except FileNotFoundError:
        pass  


def main():
    """Função principal da aplicação Streamlit."""
    st.title("Kaggle Beverage Analysis Project")
    
    st.write("""
    Este projeto é sobre um conjunto de dados sobre vendas de bebidas,
    e realiza uma análise básica.
    """)
    
    if st.button('Autenticar com Kaggle'):
        if authenticate_kaggle_case():
            logging.info("Autenticação bem-sucedida com o Kaggle.")  
            st.success("Autenticação no Kaggle bem-sucedida!")
        else:
            logging.error("Falha na autenticação com o Kaggle.") 
            st.error("Falha na autenticação com Kaggle.")
    
    # Analisar o dataset
    if st.button('Analisar Conjunto de Dados'):
        resultado = analyze_dataset_case()
        if resultado is not None:
            logging.info("Análise do conjunto de dados realizada com sucesso.")  
            st.write("Resumo dos dados:")
            st.write(resultado)
        else:
            logging.error("Falha no download ou na análise dos dados.") 
            st.error("Falha no download ou na análise dos dados.")
    
    truncate_log_file("app.log", max_lines=10000)

    # Mostrar logs
    try:
        with open("app.log", "r") as log_file:
            logs = log_file.read()
            st.text_area("Logs da Aplicação", logs, height=300)
    except FileNotFoundError:
        st.text("Nenhum log encontrado.")


if __name__ == "__main__":
    main()
