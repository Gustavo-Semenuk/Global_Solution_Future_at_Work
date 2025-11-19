import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Orgãos Públicos", layout="wide")

st.markdown("""
<style>
body, .stApp { background-color: #000000 !important; }
main, .block-container { background-color: #000000 !important; }
* { color: white !important; }
</style>
""", unsafe_allow_html=True)

st.title("Orgãos Públicos")

abas = st.tabs(["Dashboard"])

with abas[0]:
    st.header("Dashboard - Análise por UF")
    st.write("Gráficos e métricas do projeto aqui.")

    url = "https://app.powerbi.com/view?r=eyJrIjoiYzJhMTgzNTItNDc2ZC00YWFjLWE3MjgtYWQyODI4NzlhYWRmIiwidCI6IjExZGJiZmUyLTg5YjgtNDU0OS1iZTEwLWNlYzM2NGU1OTU1MSIsImMiOjR9"

    components.iframe(url, width=1500, height=800)

