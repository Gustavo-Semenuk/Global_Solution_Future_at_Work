import streamlit as st

st.set_page_config(page_title="Orgãos Públicos", layout="wide")

st.markdown("""
<style>
body, .stApp { background-color: #000000 !important; }
main, .block-container { background-color: #000000 !important; }
* { color: white !important; }
</style>
""", unsafe_allow_html=True)

st.title("Orgãos Públicos")

abas = st.tabs(["Dashboard", "Relatórios", "Exportar"])

with abas[0]:
    st.subheader("Dashboard")
    st.write("Gráficos e métricas aqui.")

with abas[1]:
    st.subheader("Relatórios")
    st.write("Conteúdo de relatórios.")

with abas[2]:
    st.subheader("Exportar dados")
    st.write("Opções de exportação.")
