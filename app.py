import streamlit as st

# ---- Page config ----
st.set_page_config(page_title="Home Principal", layout="wide")

# ---- CSS global ----
st.markdown("""
<style>
body, .stApp {
    background-color: #000000 !important;
}
main, .block-container {
    background-color: #000000 !important;
}
h1, h2, h3, h4, h5, h6, p, span, label, div, .stMarkdown, .stButton>button {
    color: #FFFFFF !important;
}
.stButton>button {
    background-color: #111111 !important;
    color: #FFFFFF !important;
    border: 1px solid #555 !important;
    font-size: 22px !important;
    padding: 20px !important;
    border-radius: 12px;
}

/* Cards personalizados */
.card {
    background-color: #111111;
    padding: 60px;
    border-radius: 25px;
    text-align: center;
    min-height: 250px;
    font-size: 30px;
    border: 2px solid #333;
    transition: 0.3s;
}
.card:hover {
    background-color: #222222;
    transform: scale(1.05);
    cursor: pointer;
}
</style>
""", unsafe_allow_html=True)

# ---- Logo (coloque sua imagem) ----
st.image("imagens/human_centric.png")

st.divider()
st.write("")

# ---- Layout dos cards ----
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    if st.button("Peoples", use_container_width=True):
        st.switch_page("pages/1_menu_a.py")

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    if st.button("Orgãos Públicos", use_container_width=True):
        st.switch_page("pages/2_menu_b.py")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    if st.button("Empresas", use_container_width=True):
        st.switch_page("pages/3_menu_c.py")
    st.markdown('</div>', unsafe_allow_html=True)
