# README
Projeto Sprint 5

# Dashboard de Anúncios de Veículos

## Sobre o projeto

Este projeto consiste em um aplicativo web interativo desenvolvido com Python, Streamlit, Pandas e Plotly Express. O objetivo é permitir a exploração de um conjunto de dados de anúncios de veículos usados por meio de gráficos interativos.

## Funcionalidades

- **Histograma de quilometragem:** permite visualizar a distribuição da quilometragem dos veículos anunciados.
- **Gráfico de dispersão entre preço e ano do modelo:** permite explorar a relação entre o ano do modelo do veículo e seu preço anunciado.
- **Dashboard interativo:** permite gerar os gráficos por meio de botões.

## Tecnologias utilizadas

- Python
- Pandas
- Streamlit
- Plotly Express

## Conjunto de dados

O aplicativo utiliza o arquivo `vehicles_us.csv`, que contém informações sobre anúncios de veículos usados.

## Como executar o aplicativo

1. Instale as bibliotecas necessárias:

   ```bash
   pip install -r requirement.txt
   ```

2. Execute o aplicativo:

   ```bash
   python -m streamlit run app.py
   ```

O Streamlit informará o endereço local para acessar o aplicativo, geralmente `http://localhost:8501`.

## Objetivo do projeto

Este projeto tem como objetivo praticar a análise exploratória de dados e a criação de visualizações interativas com Python, facilitando a exploração e a compreensão de informações sobre anúncios de veículos usados.
