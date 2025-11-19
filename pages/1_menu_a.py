import streamlit as st

st.set_page_config(page_title="Peoples", layout="wide")

# ---- CSS padrão ----
st.markdown("""
<style>
body, .stApp { background-color: #000000 !important; }
main, .block-container { background-color: #000000 !important; }
* { color: white !important; }
</style>
""", unsafe_allow_html=True)

st.title("Peoples")

abas = st.tabs(["🏠 Home", "ℹ️ Sobre nós", "💻 Soluções", "🗂 Tech review"])

with abas[0]:
    st.header("Home do Menu A")
    st.write("Bem-vindo ao Menu A!")
    st.title("Formulario")
    form = st.form("my_form")
    form.slider("Inside the form")
    st.slider("Outside the form")

    form.form_submit_button("Submit")

with abas[1]:
    st.header("Sobre nós")
    st.write("Descrição da equipe / empresa / produto...")

with abas[2]:
    st.header("Soluções")
    st.write("Aqui ficam as soluções do Menu A.")

with abas[3]:
    st.header("Tech Review")
    st.write("Conteúdos técnicos e revisões.")
