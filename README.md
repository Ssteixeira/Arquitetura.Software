# Arquitetura de Software
Sabrinna de Souza T Santos 

## Análise Netflix Movies and TV Shows

Este projeto é um **app interativo em Streamlit** para explorar o catálogo de filmes e séries da Netflix.  
Permite filtrar por gênero, país e ano, além de visualizar gráficos e insights sobre lançamentos, categorias mais populares e top países com mais títulos.

---

## Funcionalidades

- Filtros interativos na **barra lateral**:
  - Gêneros
  - Países
  - Intervalo de anos
- Menu lateral com seções:
  - **Visão Geral**: tabela filtrada
  - **Filmes vs Séries**: gráfico de pizza comparando quantidade
  - **Top Países**: gráfico de barras com os 10 países com mais títulos
  - **Lançamentos por Ano**: gráfico de linha com lançamentos ao longo dos anos
- Gráficos interativos utilizando **Altair**
- Layout estilizado com CSS customizado
- Rodapé com créditos

---

## Utilizado

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)

---

## Como rodar o projeto localmente

1. Clone o repositório:
```bash

streamlit run app.py


