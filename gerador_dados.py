import pandas as pd
from faker import Faker
import random

fake = Faker("pt_BR")

# -------------------------
# 1. IMPORTAR CSV REAL
# -------------------------

df_mapa = pd.read_csv(r"D:\Faculdade\Global_Solution_Future_at_Work\data_sets\Mapa da desigualdade 2024.csv")

# Ajustar nome da coluna de Pontuação, trocar vírgula por ponto
df_mapa["Pontuação"] = (
    df_mapa["Pontuação"]
    .astype(str)
    .str.replace(",", ".")
    .astype(float)
)

# Criar classificação de vulnerabilidade:
# 0–30 → alta, 31–60 → média, 61–96 → baixa
def classificar_vulnerabilidade(pontuacao):
    if pontuacao <= 30:
        return "alta"
    elif pontuacao <= 60:
        return "media"
        # 61 a 96
    return "baixa"

df_mapa["Vulnerabilidade"] = df_mapa["Pontuação"].apply(classificar_vulnerabilidade)


# -------------------------
# 2. ADICIONAR ZONAS DE SP
# -------------------------

# Mapeamento aproximado (base usado por estudos urbanos)
zonas_sp = {
    "Moema": "Zona Sul",
    "Butantã": "Zona Oeste",
    "Vila Mariana": "Zona Sul",
    "Itaim Bibi": "Zona Sul",
    "Lapa": "Zona Oeste",
    "Pinheiros": "Zona Oeste",
    "Santana": "Zona Norte",
    "Brasilândia": "Zona Norte",
    "Casa Verde": "Zona Norte",
    "Itaquera": "Zona Leste",
    "São Mateus": "Zona Leste",
    "Cidade Tiradentes": "Zona Leste",
    "Guaianases": "Zona Leste",
    "Sapopemba": "Zona Leste",
    "Jabaquara": "Zona Sul",
    "Campo Limpo": "Zona Sul",
    "Capão Redondo": "Zona Sul",
    "Grajaú": "Zona Sul",
    # Se algum distrito não estiver mapeado → "Desconhecida"
}

df_mapa["Zona"] = df_mapa["Distrito"].map(zonas_sp).fillna("Desconhecida")

# Transformar em dicionário para consulta
distritos_info = df_mapa.set_index("Distrito")[["Zona", "Vulnerabilidade"]].to_dict(orient="index")


# -------------------------
# 3. GERAÇÃO DE USUÁRIOS
# -------------------------

interesses = [
    "Tecnologia", "Administração", "Vendas", "Design",
    "Programação", "Marketing", "Logística", "Suporte Técnico",
]

cursos = [
    "Pacote Office",
    "Programação",
    "IA Básica",
    "Redes Sociais",
    "Excel Avançado",
    "Lógica de Programação",
    "Não tenho nenhum curso"
]

dados = []
distritos_lista = list(distritos_info.keys())

for i in range(20000):

    distrito = random.choice(distritos_lista)
    zona = distritos_info[distrito]["Zona"]
    vulnerabilidade = distritos_info[distrito]["Vulnerabilidade"]

    # -------------------------
    # Parâmetros por VULNERABILIDADE
    # -------------------------
    if vulnerabilidade == "alta":
        renda = random.randint(600, 2500)
        nivel_digital = random.choice(["iniciante", "iniciante", "básico"])
        velocidade = random.choice(["baixa", "baixa", "media"])
        possui_pc = random.choice([0, 0, 1])
    elif vulnerabilidade == "media":
        renda = random.randint(1500, 5000)
        nivel_digital = random.choice(["básico", "intermediário"])
        velocidade = random.choice(["media", "baixa", "alta"])
        possui_pc = random.choice([0, 1, 1])
    else:  # baixa
        renda = random.randint(3500, 15000)
        nivel_digital = random.choice(["intermediário", "avançado"])
        velocidade = random.choice(["media", "alta"])
        possui_pc = random.choice([1, 1, 1])

    dados.append({
        "ID": i + 1,
        "Nome": fake.name(),
        "Email": fake.email(),
        "Telefone": fake.phone_number(),

        "Estado": "São Paulo",
        "Cidade": "São Paulo",
        "Distrito": distrito,
        "Zona": zona,
        "Vulnerabilidade": vulnerabilidade,

        "Renda_mensal": renda,
        "Empregado": random.choice(["sim", "não"]),
        "Tipo_emprego": random.choice(["formal", "informal", "desempregado"]),

        "Possui_computador": possui_pc,
        "Velocidade_internet": velocidade,
        "Dispositivo_principal": random.choice(["celular", "celular", "notebook"]),

        "Nivel_digital": nivel_digital,
        "Autonomia_digital": random.randint(0, 10),
        "Conhecimento_tecnico": random.randint(0, 10),

        "Interesse_profissional": random.choice(interesses),
        "Interesse_curso": random.choice(["sim", "não"]),
        "Curso_interesse": random.choice(cursos),

        "Pessoas_na_residencia": random.randint(1, 8),
        "Data_cadastro": fake.date_this_decade().strftime("%d/%m/%Y"),
    })

df_final = pd.DataFrame(dados)
df_final.to_csv(
    r"D:\Faculdade\Global_Solution_Future_at_Work\data_sets\usuarios_vulnerabilidade_com_mapa.csv",
    index=False,
    sep=";"
)

print(df_final.head())



