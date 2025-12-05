import streamlit as st
from datetime import datetime

def renderizar_dashboard(df):
    st.subheader("Visão Geral do Mercado")
    c1, c2, c3 = st.columns(3)
    c1.metric("Itens Monitorados", len(df))
    c2.metric("Média de Economia", f"R$ {df['Economia'].mean():.2f}")
    c3.metric("Atualização", datetime.now().strftime("%d/%m/%Y"))
    
    st.dataframe(df, use_container_width=True, hide_index=True, height=500)