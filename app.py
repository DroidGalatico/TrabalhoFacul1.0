import streamlit as st
from src.services import ServicoCotacao
from src.ui import renderizar_dashboard, renderizar_pesquisa

st.set_page_config(page_title="EcoMed | Enterprise", page_icon="💊", layout="wide")
st.markdown("""
    <style>
    .banner-header {
        /* Degradê azul escuro para dar contraste com o fundo preto */
        background: linear-gradient(90deg, #101820 0%, #243b55 100%);
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 8px solid #FF4B4B; /* Faixa vermelha lateral */
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3); /* Sombra para dar profundidade */
        margin-bottom: 25px;
    }
    .banner-title {
        color: #f0f2f6; /* Branco gelo */
        font-size: 2.2rem;
        font-weight: 700;
        margin: 0;
    }
    .banner-subtitle {
        color: #cfd8dc; /* Cinza claro */
        font-size: 1rem;
        margin-top: 5px;
    }
    </style>
    
    <div class="banner-header">
        <h1 class="banner-title">💊 EcoMed | Monitor Estruturado</h1>
    </div>
""", unsafe_allow_html=True)

@st.cache_data
def carregar_dados_negocio():
    servico = ServicoCotacao()
    return servico.gerar_dataframe_atualizado()

df_global = carregar_dados_negocio()

aba1, aba2 = st.tabs(["📊 Visão Geral", "🔍 Pesquisa Avançada"])

with aba1:
    renderizar_dashboard(df_global)

with aba2:
    renderizar_pesquisa(df_global)