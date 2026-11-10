import streamlit as st
st.set_page_config(
    page_title="Carbono do Solo + IA | Projeto Científico",
    page_icon="",
    layout="wide", # Permite que o conteúdo ocupe a largura total da tela
    initial_sidebar_state="collapsed" # Esconde a sidebar por padrão, ideal para landing pages
    )

st.markdown("""
<style>
/* Fonte Book Antiqua em toda a página */
html, body, [class*="st-"] {
    font-family: "Book Antiqua", "Palatino Linotype",
                 "Palatino", serif !important;
}

/* Títulos */
h1, h2, h3, h4, h5, h6 {
    font-family: "Book Antiqua", "Palatino Linotype",
                 "Palatino", serif !important;
    font-weight: 700 !important;
}

/* Botões */
.stButton button {
    font-family: "Book Antiqua", "Palatino Linotype",
                 "Palatino", serif !important;
}
</style>
""", unsafe_allow_html=True)


st.title("Carbono do Solo + IA | Projeto da Disciplina de IA🌱")
with st.container(border=True): # border=True adiciona uma borda sutil se o tema permitir
    st.title(" Do Solo aos Dados: Estimando Carbono Orgânico com IA")
col_texto, col_imagem = st.columns([1, 1])
with col_texto:
    st.header("Conheça o projeto")
    st.write(
        "Vamos investigar como os atributos químicos do solo podem ajudar "
        "a estimar o carbono orgânico em áreas agrícolas da África Ocidental."
    )
with col_imagem:
    # st.image exibe uma imagem a partir de um endereço da internet.
    st.image(
        "https://www.isda-africa.com/img/isdasoil/isdasoil-home_hu_7ad6d14f83d440d9.webp",
        caption="Fonte: https://www.isda-africa.com/",
        use_container_width=True
    )
st.write('---')
st.header('Nossa equipe')
st.write('Conheça nosso grupo:')


col_eduardo, col_alex, col_jackelyne= st.columns(3)

with col_eduardo:
    with st.container(border=True):
        st.image(
            'eduardo.jpeg',
            width = 220
        )
        st.subheader('Eduardo Santana')
        st.write('Doutorando no PPGCA-AGRO')

with col_alex:
    with st.container(border=True):
        st.image(
            'alex.jpeg',
            width = 220
        )
        st.subheader('Alex Delva')
        st.write('Mestrando no PPGCA-AGRO')

with col_jackelyne:
    with st.container(border=True):
        st.image(
            'jakelyne.jpeg',
            width = 220
        )
        st.subheader('Jakelyne Ferreira')
        st.write('Doutoranda no PPGCA-AGRO')

st.write("---")

st.header("🔎 Qual é o desafio científico?")
st.write(
    "O carbono orgânico é uma característica importante para compreender "
    "a qualidade e o funcionamento do solo. O desafio é identificar quais "
    "atributos químicos ajudam a estimar sua concentração."
)

# Três colunas para apresentar informações curtas em formato de cartões.
col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.subheader("🌱 O que estudar?")
        st.write("Carbono orgânico em amostras de solo superficial.")

with col2:
    with st.container(border=True):
        st.subheader("🧪 Quais informações?")
        st.write("Atributos químicos, como pH, cálcio, magnésio e fósforo.")

with col3:
    with st.container(border=True):
        st.subheader("🤖 Para quê?")
        st.write("Avaliar se a inteligência artificial consegue estimar o carbono orgânico.")

st.write("---")

st.header("🗺️ De onde vêm os dados?")

col_isda, = st.columns(1)

with col_isda:
    with st.container(border=False):


        st.image(
            'logo_isda.jpg',
            width = 220
        )
        st.image(
            'logo_kangle.png',
                        width = 220
        )
        
st.write(
    "O estudo utiliza dados da base iSDA Africa, considerando amostras "
    "de solo superficial, na camada de 0 a 20 cm."
)

# Apresenta três números importantes em colunas.
col_dado1, col_dado2, col_dado3 = st.columns(3)

with col_dado1:
    with st.container(border=True):
        st.subheader("2.134")
        st.write("Registros inicialmente elegíveis")

with col_dado2:
    with st.container(border=True):
        st.subheader("2.109")
        st.write("Registros completos para a análise")

with col_dado3:
    with st.container(border=True):
        st.subheader("15")
        st.write("Atributos químicos candidatos")

# Segunda imagem ilustrativa, relacionada ao solo e às plantas.
st.image(
    "https://images.unsplash.com/photo-1416879595882-3373a0480b5b?auto=format&fit=crop&w=1200&q=80",
    caption="O solo e suas características são a base do estudo.",
    use_container_width=True
)
st.write("---")

st.header("⚙️ Como a pesquisa será realizada?")
st.write("O planejamento está organizado em quatro etapas principais:")

col_etapa1, col_etapa2, col_etapa3, col_etapa4 = st.columns(4)

with col_etapa1:
    with st.container(border=True):
        st.subheader("1. 🔍 Explorar")
        st.write("Conhecer os dados, observar distribuições e verificar possíveis problemas.")

with col_etapa2:
    with st.container(border=True):
        st.subheader("2. 📊 Analisar")
        st.write("Investigar as relações entre o carbono orgânico e os atributos químicos.")

with col_etapa3:
    with st.container(border=True):
        st.subheader("3. 🤖 Modelar")
        st.write("Treinar e comparar modelos de aprendizado de máquina.")

with col_etapa4:
    with st.container(border=True):
        st.subheader("4. ✅ Validar")
        st.write("Testar os modelos em grupos de áreas geograficamente separados.")



st.write("---")

st.header("🧪 Variáveis Estudadas")

st.write(
    "Atributos químicos utilizados para estimar "
    "o carbono orgânico do solo."
)

# Variável resposta
with st.container(border=True):

    st.subheader("🌱 Variável resposta")

    st.write("**C org — Carbono orgânico**")

    st.write("Unidade: g/kg")


# Variáveis preditoras
st.subheader("🔬 Atributos químicos preditores")

# Criando três colunas
col1, col2, col3 = st.columns(3)


with col1:

    st.write("🧲 **Al — Alumínio**")
    st.write("🧪 **B — Boro**")
    st.write("🦴 **Ca — Cálcio**")
    st.write("⚙️ **Cu — Cobre**")
    st.write("⚡ **CE — Condutividade elétrica**")

with col2:

    st.write("🧲 **Fe — Ferro**")
    st.write("🧪 **Mg — Magnésio**")
    st.write("🔬 **Mn — Manganês**")
    st.write("🌿 **N — Nitrogênio total**")
    st.write("⚗️ **pH — Potencial hidrogeniônico**")

with col3:

    st.write("🌱 **P — Fósforo**")
    st.write("🧂 **K — Potássio**")
    st.write("🧪 **Na — Sódio**")
    st.write("🌋 **S — Enxofre**")
    st.write("🔬 **Zn — Zinco**")

st.write("---")

st.header("🤖 Quais modelos serão avaliados?")
col_modelo1, col_modelo2, col_modelo3, col_modelo4 = st.columns(4)
with col_modelo1:
    with st.container(border=True):
        st.subheader("Elastic Net")
        st.write("Modelo estatístico com regularização.")

with col_modelo2:
    with st.container(border=True):
        st.subheader("Random Forest")
        st.write("Conjunto de árvores de decisão.")

with col_modelo3:
    with st.container(border=True):
        st.subheader("Gradient Boosting")
        st.write("Combina árvores construídas em sequência.")

with col_modelo4:
    with st.container(border=True):
        st.subheader("SVR")
        st.write("Modelo de regressão baseado em vetores de suporte.")

st.write("---")

st.header("📍 Como saberemos se os modelos funcionam?")
st.write(
    "Será utilizada validação espacial em cinco grupos. Assim, o desempenho "
    "será avaliado em áreas que não participaram do treinamento de cada rodada."
)

col_validacao1, col_validacao2, col_validacao3 = st.columns(3)

with col_validacao1:
    st.subheader("🗺️ Separação espacial")
    st.write("As amostras serão organizadas em cinco grupos geográficos.")

with col_validacao2:
    st.subheader("📏 Métrica principal: MAE")
    st.write("O erro absoluto médio indica o tamanho médio dos erros, em g/kg.")

with col_validacao3:
    st.subheader("🛡️ Evitar vazamento")
    st.write("O pré-processamento e o ajuste serão feitos somente com os dados de treinamento.")

st.write("---")

st.header("🎯 O que esperamos descobrir?")
st.write(
    "Esperamos identificar quais atributos químicos oferecem informações "
    "úteis para estimar o carbono orgânico e verificar se essa capacidade "
    "se mantém em diferentes áreas."
)

st.info(
    "Importante: estes são resultados esperados. As conclusões só poderão "
    "ser apresentadas depois da execução e avaliação dos modelos."
)


