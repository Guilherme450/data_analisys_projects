# Análise de despesas diárias no período de uma semana em Caxias.

# Importar bibliotecas úteis para o armazenamento, modelagem e análise dos dados.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-dark")

# Inserindo os dados obtidos durante uma semana.
dados = {
    'gastos_totais': [13.5, 6, 5, 50.5, 6, 2, 0, 6, 6, 7, 24.5, 22.4],
    'dias_da_semana': np.arange(1, 13),
    'gastos_diários_transportes': [12.5, 5, 5, 5, 5, 5, 5, 5, 5, 15, 5, 6.4],
    'gastos_diários_alimentação': [1, 1, 0, 1, 1, 2, 0, 1, 1, 2, 19.5, 11],
    'gastos_diários_outros': [0, 0, 0, 44.9, 0, 0, 0, 0, 0, 0, 0, 0]
}

# criando um dataframe dos dados.
df = pd.DataFrame(dados)

print(df)

# resumo estatistico dos gastos totais diários.
summary_gastos_totais = df['gastos_totais'].describe()

print(summary_gastos_totais)

# contar as frequências dos dados de transporte e alimentação.
count_transport = (df['gastos_diários_transportes'].sum() / df['gastos_totais'].sum()) * 100
count_eating = (df['gastos_diários_alimentação'].sum() / df['gastos_totais'].sum()) * 100
count_outros = (df['gastos_diários_outros'].sum() / df['gastos_totais'].sum()) * 100 

valores = [count_transport,count_eating, count_outros]
labels = ['Transporte', 'Alimentação', 'Outros']

sum_gastos_totais = df['gastos_totais'].sum()

print(f'Soma dos Gastos Totais: {sum_gastos_totais}')

# Mostrar um gráfico de barras dias x gastos totais.
fig, ax = plt.subplots(2, 2, figsize=(9, 6), num='Análise de Gastos de: 01/04/24 a 14/04/24')

plt.subplots_adjust(
    left=0.055,
    bottom=0.069,
    top=0.952,
    right=0.97,
    wspace=0.189,
    hspace=0.324
)

ax[0, 0].bar(df['dias_da_semana'], df['gastos_totais'], color='#DA70D6')
ax[0, 0].plot(df['dias_da_semana'], df['gastos_totais'], color='purple', marker='o')
ax[0, 0].set_title('Gastos diários totais')
ax[0, 0].set_xlabel('Dias')
ax[0, 0].set_ylabel('Gastos totais (R$)')
ax[0, 0].grid()

ax[0, 1].pie(valores, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#9D00FF', '#DA70D6', '#800080'])
ax[0, 1].set_title('Gastos por área')

ax[1, 0].hist(df['gastos_diários_transportes'], color= '#800080', edgecolor='white')
ax[1, 0].set_title('Frequência de gastos com trasporte')
ax[1, 0].set_ylabel('Frequência')
ax[1, 0].set_xlabel('Gastos (R$)')

ax[1, 1].hist(df['gastos_diários_alimentação'], color= '#800080', edgecolor='white')
ax[1, 1].set_title('Frequência de gastos com alimentação')
ax[1, 1].set_ylabel('Frequência')
ax[1, 1].set_xlabel('Gastos (R$)')

plt.show()