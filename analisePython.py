import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Carregar dados
df = pd.read_csv('NBA.csv')

# Resumo estatístico
print(df.describe())

# Verificar dados faltantes
print(df.isnull().sum())

# Visualizar a distribuição de uma variável numérica
sns.histplot(df['MP'], kde=True)
plt.show()
# Boxplot para identificar outliers
sns.boxplot(x=df['MP'])
plt.show()

# Visualizar a distribuição de uma variável numérica
sns.histplot(df['G'], kde=True)
plt.show()
# Boxplot para identificar outliers
sns.boxplot(x=df['G'])
plt.show()

# Visualizar a distribuição de uma variável numérica
sns.histplot(df['Age'], kde=True)
plt.show()
# Boxplot para identificar outliers
sns.boxplot(x=df['Age'])
plt.show()

# Visualizar a distribuição de uma variável numérica
sns.histplot(df['GS'], kde=True)
plt.show()
# Boxplot para identificar outliers
sns.boxplot(x=df['GS'])
plt.show()

# Visualizar a distribuição de uma variável numérica
sns.histplot(df['FG'], kde=True)
plt.show()
# Boxplot para identificar outliers
sns.boxplot(x=df['FG'])
plt.show()

# Visualizar a distribuição de uma variável numérica
sns.histplot(df['3P'], kde=True)
plt.show()
# Boxplot para identificar outliers
sns.boxplot(x=df['3P'])
plt.show()

# Visualizar a distribuição de uma variável numérica
sns.histplot(df['3PA'], kde=True)
plt.show()
# Boxplot para identificar outliers
sns.boxplot(x=df['3PA'])
plt.show()

# Visualizar a distribuição de uma variável numérica
sns.histplot(df['2P'], kde=True)
plt.show()
# Boxplot para identificar outliers
sns.boxplot(x=df['2P'])
plt.show()

# Visualizar a distribuição de uma variável numérica
sns.histplot(df['2PA'], kde=True)
plt.show()
# Boxplot para identificar outliers
sns.boxplot(x=df['2PA'])
plt.show()

# Visualizar a distribuição de uma variável numérica
sns.histplot(df['FT'], kde=True)
plt.show()
# Boxplot para identificar outliers
sns.boxplot(x=df['FT'])
plt.show()

# Visualizar a distribuição de uma variável numérica
sns.histplot(df['FTA'], kde=True)
plt.show()
# Boxplot para identificar outliers
sns.boxplot(x=df['FTA'])
plt.show()

# Visualizar a distribuição de uma variável numérica
sns.histplot(df['ORB'], kde=True)
plt.show()
# Boxplot para identificar outliers
sns.boxplot(x=df['ORB'])
plt.show()

# Visualizar a distribuição de uma variável numérica
sns.histplot(df['DRB'], kde=True)
plt.show()
# Boxplot para identificar outliers
sns.boxplot(x=df['DRB'])
plt.show()

# Visualizar a distribuição de uma variável numérica
sns.histplot(df['TRB'], kde=True)
plt.show()
# Boxplot para identificar outliers
sns.boxplot(x=df['TRB'])
plt.show()

sns.histplot(df['AST'], kde=True)
plt.show()
# Boxplot para identificar outliers
sns.boxplot(x=df['AST'])
plt.show()

sns.histplot(df['STL'], kde=True)
plt.show()
# Boxplot para identificar outliers
sns.boxplot(x=df['STL'])
plt.show()

sns.histplot(df['BLK'], kde=True)
plt.show()
# Boxplot para identificar outliers
sns.boxplot(x=df['BLK'])
plt.show()

sns.histplot(df['TOV'], kde=True)
plt.show()
# Boxplot para identificar outliers
sns.boxplot(x=df['TOV'])
plt.show()

sns.histplot(df['PF'], kde=True)
plt.show()
# Boxplot para identificar outliers
sns.boxplot(x=df['PF'])
plt.show()

sns.histplot(df['PTS'], kde=True)
plt.show()
# Boxplot para identificar outliers
sns.boxplot(x=df['PTS'])
plt.show()
#parte numerica da tabela
dg = df.drop(columns=['Team', 'Awards', 'Pos','Player','Player-additional'])
print(dg.dtypes)
# Matriz de correlação
corr = dg.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()
##
# Gráfico de dispersão para ver a relação entre duas variáveis
sns.scatterplot(x='FGA', y='Age', data=df)
plt.show()
# Gráfico de dispersão para ver a relação entre duas variáveis
sns.scatterplot(x='Age', y='FGA', data=df)
plt.show()

##
# Gráfico de dispersão para ver a relação entre duas variáveis
sns.scatterplot(x='2P', y='TOV', data=df)
plt.show()
# Gráfico de dispersão para ver a relação entre duas variáveis
sns.scatterplot(x='2P', y='TRB', data=df)
plt.show()
# Gráfico de dispersão para ver a relação entre duas variáveis
sns.scatterplot(x='2P', y='FTA', data=df)
plt.show()
# Gráfico de dispersão para ver a relação entre duas variáveis
sns.scatterplot(x='2P', y='2PA', data=df)
plt.show()
# Gráfico de dispersão para ver a relação entre duas variáveis
sns.scatterplot(x='2P', y='FGA', data=df)
plt.show()
# Gráfico de dispersão para ver a relação entre duas variáveis
sns.scatterplot(x='2P', y='MP', data=df)
plt.show()
# Gráfico de dispersão para ver a relação entre duas variáveis
sns.scatterplot(x='Age', y='2P', data=df)
plt.show()
sns.scatterplot(x='Age', y='3P', data=df)
plt.show()

# Gráfico de dispersão com linha de regressão entre '2P' e 'TOV'
sns.lmplot(x='2P', y='TOV', data=df, line_kws={'color': 'red'})
plt.title('Relação entre 2P e TOV')
plt.show()

# Gráfico de dispersão com linha de regressão entre '2P' e 'TRB'
sns.lmplot(x='2P', y='TRB', data=df, line_kws={'color': 'red'})
plt.title('Relação entre 2P e TRB')
plt.show()

# Gráfico de dispersão com linha de regressão entre '2P' e 'FTA'
sns.lmplot(x='2P', y='FTA', data=df, line_kws={'color': 'red'})
plt.title('Relação entre 2P e FTA')
plt.show()

# Gráfico de dispersão com linha de regressão entre '2P' e '2PA'
sns.lmplot(x='2P', y='2PA', data=df, line_kws={'color': 'red'})
plt.title('Relação entre 2P e 2PA')
plt.show()

# Gráfico de dispersão com linha de regressão entre '2P' e 'FGA'
sns.lmplot(x='2P', y='FGA', data=df, line_kws={'color': 'red'})
plt.title('Relação entre 2P e FGA')
plt.show()

# Gráfico de dispersão com linha de regressão entre '2P' e 'MP'
sns.lmplot(x='2P', y='MP', data=df, line_kws={'color': 'red'})
plt.title('Relação entre 2P e MP')
plt.show()

