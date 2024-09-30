
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Lendo o arquivo gasolina.csv
df = pd.read_csv('gasolina.csv')

# Criando o gráfico de linha
plt.figure(figsize=(10, 6))
sns.lineplot(x='dia', y='venda', data=df, marker='o')

# Adicionando título e rótulos aos eixos
plt.title('Variação do preço da gasolina ao longo dos dias')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')

# Salvando o gráfico como gasolina.png
plt.savefig('gasolina.png')
