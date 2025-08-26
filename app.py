import pandas as pd
import altair as alt
import streamlit as st
import logging

# 1️⃣ Configuração da página
st.set_page_config(
    page_title="Análise Netflix",
    page_icon="🎬",
    layout="wide"
)

# Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 2️⃣ CSS e estilo divertido
st.markdown(
    """
    <style>
        .stApp { background: #fff; color: #222; }
        h1 {
            text-align: center;
            color: #e50914;
            font-size: 2.5em !important;
            font-weight: bold;
        }
        .description {
            font-size: 1.1em;
            text-align: center;
            color: #222;
            padding: 10px;
            border-radius: 8px;
            background: rgba(255,255,255,0.85);
            margin-bottom: 18px;
        }
        .stButton>button {
            background: #e50914;
            color: white;
            border-radius: 10px;
            font-size: 1em;
            font-weight: bold;
            padding: 8px 18px;
            border: none;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background: #b20710;
            transform: scale(1.04);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 3️⃣ Título e descrição
st.title("🎬 Análise Netflix Movies and TV Shows")
st.markdown(
    """
    <div class="description">
    Explore o catálogo da Netflix! 📺 <br>
    Filtre por gênero, país e ano no menu lateral, veja os lançamentos e descubra quais categorias são mais populares.
    </div>
    """,
    unsafe_allow_html=True
)

# 4️⃣ Carregar o dataset
@st.cache_data
def load_data():
    df = pd.read_csv('data/netflix_titles.csv')
    for col in ['listed_in', 'country', 'type']:
        df[col] = df[col].astype('category')
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    df['year_added'] = df['date_added'].dt.year.astype('Int64')
    return df

df = load_data()
st.subheader("Preview do Dataset")
st.dataframe(df.head())

# 5️⃣ Filtros interativos na barra lateral
st.sidebar.header("Filtros Interativos")

genres = st.sidebar.multiselect(
    "Selecione os gêneros:",
    options=df['listed_in'].dropna().unique(),
    default=df['listed_in'].dropna().unique()
)

countries = st.sidebar.multiselect(
    "Selecione os países:",
    options=df['country'].dropna().unique(),
    default=df['country'].dropna().unique()
)

year_range = st.sidebar.slider(
    "Selecione o intervalo de anos:",
    min_value=int(df['year_added'].min() or 2000),
    max_value=int(df['year_added'].max() or 2025),
    value=(int(df['year_added'].min() or 2000), int(df['year_added'].max() or 2025))
)

# Aplicar filtros
filtered_df = df[
    (df['listed_in'].isin(genres)) &
    (df['country'].isin(countries)) &
    (df['year_added'] >= year_range[0]) &
    (df['year_added'] <= year_range[1])
]

# Menu lateral de navegação
menu = st.sidebar.radio("Seções", ["Visão Geral", "Filmes vs Séries", "Top Países", "Lançamentos por Ano"])

if menu == "Visão Geral":
    st.subheader("Tabela Filtrada")
    st.dataframe(filtered_df)
elif menu == "Filmes vs Séries":
    st.subheader("🎬 Filmes vs Séries")
    type_counts = filtered_df['type'].value_counts().reset_index()
    type_counts.columns = ['Tipo', 'Quantidade']
    pie_chart = alt.Chart(type_counts).mark_arc(innerRadius=50, outerRadius=100).encode(
        theta='Quantidade',
        color='Tipo',
        tooltip=['Tipo', 'Quantidade']
    )
    st.altair_chart(pie_chart, use_container_width=True)
elif menu == "Top Países":
    st.subheader("🌍 Top 10 Países com Mais Títulos")
    top_countries = filtered_df['country'].value_counts().head(10).reset_index()
    top_countries.columns = ['País', 'Quantidade']
    bar_countries = alt.Chart(top_countries).mark_bar(color="#363837").encode(
        y=alt.Y('País', sort='-x'),
        x='Quantidade',
        tooltip=['País', 'Quantidade']
    ).properties(height=400)
    st.altair_chart(bar_countries, use_container_width=True)
elif menu == "Lançamentos por Ano":
    st.subheader("📈 Lançamentos por Ano")
    year_counts = filtered_df['year_added'].value_counts().sort_index().reset_index()
    year_counts.columns = ['Ano', 'Quantidade']
    line_chart = alt.Chart(year_counts).mark_line(color="#ffe400").encode(
        x=alt.X('Ano:O', title='Ano'),
        y='Quantidade',
        tooltip=['Ano', 'Quantidade']
    ).properties(width=800, height=400)
    st.altair_chart(line_chart, use_container_width=True)

# 1️⃣1️⃣ Rodapé
st.markdown(
    """
    <div style="text-align: center; padding: 20px; color: #888;">
        Desenvolvido por Sabrinna | Dados da Netflix via Kaggle
    </div>
    """,
    unsafe_allow_html=True
)
