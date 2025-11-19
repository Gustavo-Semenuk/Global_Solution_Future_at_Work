import streamlit as st

st.set_page_config(page_title="Empresas", layout="wide")

st.markdown("""
<style>
body, .stApp { background-color: #000000 !important; }
main, .block-container { background-color: #000000 !important; }
* { color: white !important; }
</style>
""", unsafe_allow_html=True)

st.title("Empresas")

abas = st.tabs(["Mapa", "Coordenadas", "Geolocalização"])

with abas[0]:
    st.subheader("Mapa")
    st.write("Aqui vai o mapa futuramente.")

with abas[1]:
    st.subheader("Coordenadas")
    st.write("Consulta de lat/long.")

with abas[2]:
    st.subheader("Geolocalização")
    st.write("Integrações de endereço.")
