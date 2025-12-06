# 💊 EcoMed | Monitor de Preços ODS

> **Status do Projeto:** 🚀 Em Desenvolvimento (Versão 1.0)

## 📋 Sobre o Projeto

O **EcoMed** é uma aplicação desenvolvida em Python para monitoramento e comparação de preços de medicamentos essenciais.

Este projeto justifica-se pela necessidade crescente de consumidores e empresas monitorarem os preços de medicamentos em diferentes farmácias, promovendo maior **transparência** e **economia** no processo de compra.

A ferramenta foi projetada para atender a uma demanda social por soluções ágeis e confiáveis, alinhando-se diretamente aos **Objetivos de Desenvolvimento Sustentável (ODS) da ONU**, com foco especial no **ODS 3: Saúde e Bem-estar**.

---

## ⚙️ Funcionalidades Principais

- **📊 Dashboard Interativo:** Visão geral do mercado com métricas de economia média e listagem completa dos 50 medicamentos mais comuns.
- **🔍 Pesquisa Inteligente:** Busque rapidamente por nome comercial (ex: *Viagra*) ou princípio ativo (ex: *Sildenafila*).
- **🏷️ Filtros por Categoria:** Segmentação eficiente por uso (ex: *Pressão Alta*, *Diabetes*, *Antibióticos*).
- **💰 Comparador de Preços:** Simulação automática de variação de valores entre diferentes farmácias (A, B e C), destacando o melhor preço.
- **📱 Design Responsivo:** Interface moderna e adaptável (Dark Mode nativo) construída com Streamlit.

---

## 🛠 Tecnologias Utilizadas

O projeto foi construído utilizando uma arquitetura robusta e modular:

- **Linguagem:** [Python 3.10+](https://www.python.org/)
- **Frontend/Backend:** [Streamlit](https://streamlit.io/) (Para criação rápida de Data Apps)
- **Manipulação de Dados:** [Pandas](https://pandas.pydata.org/)
- **Arquitetura:** MVC (Model-View-Controller) para organização de código.

---

## 🚀 Guia de Instalação e Execução

Siga o passo a passo abaixo para rodar o projeto na sua máquina local.

### 1. Clonar o Repositório
Abra o seu terminal (CMD, PowerShell ou Git Bash) e execute:

```bash
git clone [https://github.com/DroidGalatico/TrabalhoFacul1.0.git](https://github.com/DroidGalatico/TrabalhoFacul1.0.git)
cd TrabalhoFacul1.0
2. Criar e Ativar o Ambiente Virtual
Recomendamos usar um ambiente virtual para isolar as dependências do projeto.

🪟 No Windows:

PowerShell

python -m venv venv
.\venv\Scripts\activate
🐧/🍎 No Linux ou Mac:

Bash

python3 -m venv venv
source venv/bin/activate
Dica: Ao ativar com sucesso, você verá (venv) aparecendo no início da linha do terminal.

3. Instalar Dependências
Com o ambiente ativado, instale todas as bibliotecas necessárias de uma vez:

Bash

pip install -r requirements.txt
4. Executar o Sistema
Tudo pronto! Para abrir a aplicação no seu navegador, digite:

Bash

streamlit run app.py
O projeto abrirá automaticamente no endereço: http://localhost:8501

Para Parar: Vá no terminal e pressione Ctrl + C.

📂 Estrutura do Projeto
O código segue uma organização profissional para facilitar a manutenção:

Plaintext

TrabalhoFacul1.0/
├── app.py                  # 🏁 Arquivo Principal (Ponto de entrada)
├── requirements.txt        # 📦 Lista de dependências do projeto
├── README.md               # 📄 Documentação (Você está aqui)
└── src/                    # 🧠 Código Fonte
    ├── data/               # Banco de Dados (Lista de Medicamentos)
    ├── services/           # Regras de Negócio (Cálculos e Simulações)
    └── ui/                 # Interface Visual (Telas e Gráficos)
🤝 Contribuição
Este é um projeto acadêmico de código aberto. Sugestões, correções e melhorias são sempre bem-vindas!

Desenvolvido por DroidGalatico