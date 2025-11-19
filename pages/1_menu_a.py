import streamlit as st
from datetime import date

# CONFIG
st.set_page_config(page_title="Peoples", layout="wide")

# Inicializa estado de preenchimento
if "preencheu" not in st.session_state:
    st.session_state.preencheu = False

# CSS
st.markdown("""
<style>
body, .stApp { background-color: #000000 !important; }
main, .block-container { background-color: #000000 !important; }
label, h1, h2, h3, p, span, div { color: white !important; }
</style>
""", unsafe_allow_html=True)

# TÍTULO PRINCIPAL
st.title("Peoples")

# ABAS
abas = st.tabs(["ℹ️ Formulário", "💻 Aprendizado"])


# ABA 1 – FORMULÁRIO

with abas[0]:

    st.title("📋 Formulário de Cadastro – Inclusão e Letramento Digital")

    st.markdown(
        "Preencha as informações abaixo para contribuir com o mapeamento de desigualdade "
        "digital e acesso à tecnologia na cidade de São Paulo."
    )

    st.write("---")

    with st.form("formulario_inclusao_digital"):

        # DADOS PESSOAIS

        st.subheader("🧑‍💼 Dados Pessoais")
        nome = st.text_input("Nome completo")
        email = st.text_input("Email")
        telefone = st.text_input("Telefone")
        nascimento = st.date_input("Data de nascimento", min_value=date(
            1920, 1, 1), max_value=date.today())

        st.write("---")

        # LOCALIZAÇÃO

        st.subheader("📍 Localização")
        distrito = st.text_input("Distrito")
        zona = st.selectbox("Zona de São Paulo", [
                            "Zona Norte", "Zona Sul", "Zona Leste", "Zona Oeste", "Centro"])

        st.write("---")

        # SITUAÇÃO SOCIOECONÔMICA

        st.subheader("💰 Situação Socioeconômica")
        renda = st.number_input("Renda mensal (R$)", min_value=0, step=100)
        empregado = st.selectbox("Está empregado?", ["sim", "não"])
        tipo_emprego = st.selectbox(
            "Tipo de emprego", ["formal", "informal", "desempregado"])
        pessoas_residencia = st.number_input(
            "Pessoas na residência", min_value=1, max_value=15)

        st.write("---")

        # ACESSO DIGITAL

        st.subheader("💻 Acesso Digital")
        possui_pc = st.selectbox("Possui computador?", ["Sim", "Não"])
        acesso_internet = st.selectbox(
            "Possui acesso à internet?", ["Sim", "Não"])
        velocidade_net = st.selectbox("Velocidade da internet", [
                                      "baixa", "média", "alta"])
        dispositivo = st.selectbox(
            "Seu principal dispositivo de acesso",
            ["celular", "notebook", "computador de mesa", "computador público"]
        )

        st.write("---")

        # LETRAMENTO DIGITAL

        st.subheader("📚 Letramento Digital")
        nivel_digital = st.selectbox(
            "Nível atual de habilidade digital",
            ["iniciante", "básico", "intermediário", "avançado"]
        )
        autonomia = st.slider(
            "Autonomia digital (0 = nenhuma, 10 = total)", 0, 10, 3)
        conhecimento_tecnico = st.slider(
            "Conhecimento técnico (0 a 10)", 0, 10, 2)

        st.write("---")

        # INTERESSES PROFISSIONAIS

        st.subheader("🎯 Interesses Profissionais")
        interesse_prof = st.selectbox(
            "Área de interesse profissional",
            [
                "Tecnologia", "Administração", "Vendas", "Design", "Programação",
                "Marketing", "Logística", "Suporte Técnico", "Não tenho certeza"
            ]
        )

        interesse_curso = st.selectbox(
            "Tem interesse em fazer cursos na área de tecnologia?", ["sim", "não"])

        curso_interesse = st.selectbox(
            "Qual curso tem interesse?",
            [
                "Pacote Office",
                "Programação",
                "IA Básica",
                "Redes Sociais",
                "Excel Avançado",
                "Lógica de Programação",
                "Não tenho nenhum curso"
            ]
        )

        horario = st.selectbox("Melhor horário para estudar", [
                               "manhã", "tarde", "noite", "madrugada"])

        st.write("---")

        enviado = st.form_submit_button("Enviar formulário")

    # RESPOSTA DO FORMULÁRIO

    if enviado:
        st.success(
            "✔ Cadastro enviado com sucesso! Obrigado por contribuir para nosso projeto! 🙏")
        st.subheader("📌 Dados Recebidos:")

         # Ativa o estado global
        st.session_state.preencheu = True

        dados_usuario = {
            "nome": nome,
            "email": email,
            "telefone": telefone,
            "nascimento": str(nascimento),
            "distrito": distrito,
            "zona": zona,
            "renda": renda,
            "empregado": empregado,
            "tipo_emprego": tipo_emprego,
            "pessoas_residencia": pessoas_residencia,
            "possui_computador": possui_pc,
            "acesso_internet": acesso_internet,
            "velocidade": velocidade_net,
            "dispositivo": dispositivo,
            "nivel_digital": nivel_digital,
            "autonomia_digital": autonomia,
            "conhecimento_tecnico": conhecimento_tecnico,
            "interesse_profissional": interesse_prof,
            "interesse_curso": interesse_curso,
            "curso_interesse": curso_interesse,
            "horario": horario,
        }

        st.json(dados_usuario)

# ABA 2 – GAMEFICAÇÃO
with abas[1]:
    st.title("🎁 Aprendizado")

    if not st.session_state.preencheu:
        st.warning("⚠️ Preencha o formulário para desbloquear os vídeos educativos!")
    else:
        st.success("🎉 Parabéns! Você desbloqueou os vídeos educativos 👇")

        videos = [
            ("Introdução à Computação", "https://www.youtube.com/embed/HD13eq_Pmp8"),
            ("Como usar o Google Drive", "https://www.youtube.com/embed/qE7MAfIoB1I"),
            ("Aprenda Lógica de Programação", "https://www.youtube.com/embed/mc3TKp2XzhI"),
            ("Como usar o Excel Básico", "https://www.youtube.com/embed/mO5DUjMZJx8"),
            ("Segurança digital para iniciantes", "https://www.youtube.com/embed/uF0wzYLpQos"),
        ]

        cols = st.columns(2)

        for i, (titulo, url) in enumerate(videos):
            with cols[i % 2]:
                st.markdown(f"#### 🎥 {titulo}")
                st.video(url)
                st.write("---")

