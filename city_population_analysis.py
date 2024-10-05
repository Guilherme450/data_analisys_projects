import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Importando os dados em formato csv(comma separated value)
data = 'Wprld population growth rate by cities 2024.csv'

# Inicializando os dados em um datafame
df = pd.read_csv(data)

# ANÁLISE EXPLORATÓRIA DE DADOS (EDA)
print(df.head(10))

# Extraindo informações sobre os dados.
print(df.info())

# Excluir linhas com valores ausentes
df.dropna(inplace=True)

print(df.isnull().sum())

# Aplincado estatística descritiva
print(df.describe(include='all').T)

# Re-formatando os dados
df.loc[df['Continent'] == 'Oceana', 'Continent'] = 'Oceania'

# media da taxa de crescimento de cada país

growth_rate_by_country = df.groupby('Country')['Growth Rate'].mean()

top_growth_rate_country = growth_rate_by_country.sort_values(ascending=False)

less_growth_rate_country = growth_rate_by_country.sort_values(ascending=True)

top_growth_rate_country = top_growth_rate_country[: 10]
less_growth_rate_country = less_growth_rate_country[: 10]

print(top_growth_rate_country)
print("-*-" * 10)
print(less_growth_rate_country)

bar_top_growth_rate = px.bar(top_growth_rate_country, title='Top Growth Rate by Country')
#bar_top_growth_rate.show()

fig = px.bar(df, x='Continent', title='Continentes com cidades mais populosas')

fig2 = px.histogram(df, x='Growth Rate', marginal='box')

#fig.show()
#fig2.show()

#fig = plt.figure(figsize=(8, 5))
#sns.boxplot(df, x='Continent', y='Growth Rate', hue='Continent')

#fig.savefig('anova_continent_growth_rate.pdf')

def growth_rate_analysis():
    fig = plt.figure(figsize=(8, 5))

    plt.subplots_adjust(
        top=0.954,
        wspace=0.32,
        hspace=0.415
    )

    plt.subplot(2, 2, 1)
    sns.histplot(df, x='Growth Rate', color='skyblue')
    plt.title('Histograma Growth Rate')

    plt.subplot(2, 2, 2)
    sns.kdeplot(df, x='Growth Rate', fill=True)
    plt.title('Kernel Density Estimation of Growth Rate')

    plt.subplot(2,2,3)
    sns.barplot(top_growth_rate_country, color='skyblue')
    plt.title('Top 10 high Growth Rate')
    plt.xticks(rotation=45)

    plt.subplot(2,2,4)
    sns.barplot(less_growth_rate_country, color='skyblue')
    plt.title('Top 10 Less Growth Rate')
    plt.xticks(rotation=45)

    fig.savefig('growth_rate_analysis.pdf')

    return fig

# matriz de correlação
def heat_map():
    numeric_variables = df.select_dtypes(include=np.number).columns

    corr_matrix = df[numeric_variables].corr()

    fig = plt.figure(figsize=(8, 5))

    sns.heatmap(corr_matrix, cmap='coolwarm', 
                fmt='.2f', vmin=-1, vmax=1, 
                annot=True, square=True, linewidths=.8)
    fig.savefig('heatmap.pdf')
    
    return fig
