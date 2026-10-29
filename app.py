import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Dashboard - Atividade 07", page_icon="📊", layout="wide"
)

with st.sidebar:
    st.header("👤 Informações do Aluno")
    st.markdown("**Nome:** Bernardo Garajau Silva")
    st.markdown("**Número da Chamada:** 06")  
    st.markdown("**Turma:** 3D1")
    st.markdown("---")
    st.markdown("**Instituição:** Colégio Cotemig")

st.title("📊 Dashboard Analítico - Atividade de Fixação 07")
st.markdown(
    "Painel interativo contendo a visualização e análise dos gráficos da"
    " Atividade 06."
)
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 1. Vendas por Categoria e Região")
    st.image("imagens/grafico_barras.png", use_container_width=True)
    st.info(
        "**Análise:** O gráfico de barras demonstra o desempenho de vendas"
        " médias por categoria, evidenciando quais regiões lideram o"
        " faturamento."
    )

with col2:
    st.markdown("### 2. Distribuição Salarial")
    st.image("imagens/grafico_boxplot.png", use_container_width=True)
    st.info(
        "**Análise:** O boxplot exibe a dispersão salarial por departamento,"
        " destacando a mediana e a presença de valores atípicos (outliers)."
    )

with col3:
    st.markdown("### 3. Altura vs. Peso")
    st.image("imagens/grafico_dispersao.png", use_container_width=True)
    st.info(
        "**Análise:** O gráfico de dispersão ilustra a correlação positiva entre"
        " a altura e o peso dos indivíduos, segmentada por sexo."
    )

st.markdown("---")

col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("### 4. Distribuição de Idades")
    st.image("imagens/grafico_distribuicao.png", use_container_width=True)
    st.info(
        "**Análise:** O histograma com curva KDE mostra a concentração etária dos"
        " clientes, evidenciando faixas demográficas predominantes."
    )

with col5:
    st.markdown("### 5. Frequência de Chamados")
    st.image("imagens/grafico_frequencia.png", use_container_width=True)
    st.info(
        "**Análise:** Apresenta a contagem de chamados por tipo de atendimento,"
        " apontando 'Dúvida' como a demanda mais recorrente."
    )

with col6:
    st.markdown("### 6. Movimento de Clientes (Heatmap)")
    st.image("imagens/grafico_heatmap.png", use_container_width=True)
    st.info(
        "**Análise:** O mapa de calor destaca os horários e dias da semana com"
        " maior fluxo de clientes, facilitando o dimensionamento de equipe."
    )

st.markdown("---")

col7, col8, col9 = st.columns(3)

with col7:
    st.markdown("### 7. Evolução Diária de Vendas")
    st.image("imagens/grafico_linhas.png", use_container_width=True)
    st.info(
        "**Análise:** Permite comparar a tendência de crescimento das vendas"
        " diárias ao longo do tempo entre diferentes lojas."
    )

with col8:
    st.markdown("### 8. Faturamento por Canal")
    st.image("imagens/grafico_pizza.png", use_container_width=True)
    st.info(
        "**Análise:** O gráfico circular detalha a participação percentual de"
        " cada canal de venda no faturamento total da empresa."
    )

with col9:
    st.markdown("### 9. Renda vs. Gasto Mensal")
    st.image("imagens/grafico_regressao.png", use_container_width=True)
    st.info(
        "**Análise:** A linha de regressão exibe o comportamento linear direto"
        " entre o aumento da renda mensal e o respectivo consumo."
    )
