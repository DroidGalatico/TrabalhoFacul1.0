import streamlit as st

def renderizar_pesquisa(df):
    st.subheader("Encontre seu Medicamento")
    
    col_pesquisa, col_filtro = st.columns([3, 1])
    with col_pesquisa:
        termo = st.text_input("Digite o nome:", placeholder="Ex: Dipirona...")
    with col_filtro:
        usos = sorted(list(set(df["Uso Principal"])))
        filtro = st.selectbox("Categoria:", ["Todas"] + usos)

    # Filtragem (Lógica simples de UI)
    df_filtrado = df.copy()
    if termo:
        df_filtrado = df_filtrado[
            df_filtrado["Medicamento"].str.contains(termo, case=False) | 
            df_filtrado["Marca Ref."].str.contains(termo, case=False)
        ]
    if filtro != "Todas":
        df_filtrado = df_filtrado[df_filtrado["Uso Principal"] == filtro]

    st.divider()

    if not df_filtrado.empty:
        st.success(f"{len(df_filtrado)} encontrados.")
        st.dataframe(
            df_filtrado.style.format({
                "Farma A": "R$ {:.2f}", "Farma B": "R$ {:.2f}", 
                "Farma C": "R$ {:.2f}", "Melhor Preço": "R$ {:.2f}", 
                "Economia": "R$ {:.2f}"
            }),
            use_container_width=True, hide_index=True, height=600
        )
    else:
        st.warning("Nenhum resultado.")