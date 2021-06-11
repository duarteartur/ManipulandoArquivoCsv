import pandas as pd

df = pd.read_csv('./onepice_fruits.csv')

print("______________\n", df["Devil Fruit"])

print(
    "______________\n", df.loc[(df["Character"] == "Marshall D. Teach") &
                               (df["Devil Fruit"] == "Yami Yami no Mi"),
                               ["Character", "Devil Fruit"]])

#TRABALHANDO COM DATAFRAME ALEATÓRIO
#leitura de dados

df_data = {
    'pais': ['Brasil', 'Argentina', 'Argentina', 'Brasil', 'Chile', 'Chile'],
    'ano': [2005, 2006, 2005, 2006, 2007, 2008],
    'populacao': [170.1, 30.5, 32.2, 172.6, 40.8, 42.0]
}
df = pd.DataFrame(df_data)
print(df)

#manipulação de dados
print("_______________\n", df.loc[(df["pais"] == "Argentina")], "\n")

print(
    "_______________\n",
    df.loc[(df["pais"] == "Argentina") & (df["ano"] == 2005),
           ["pais", "ano"]], "\n")

print(
    "_______________\n",
    df.loc[(df["pais"] == "Chile") & (df["populacao"] == 40.8),
           ["pais", "populacao"]], "\n")

#limpeza de dados
df_pais = {
    'pais': ['Brasil', 'Argentina', '', 'Brasil', 'Chile', ''],
    'ano': [2005, 2006, 2005, 2006, 2007, 2008],
    'populacao': [170.1, 30.5, 32.2, 172.6, 40.8, 0]
}
dtfr = pd.DataFrame(df_pais)
print(dtfr, "\n")
print(dtfr['pais'] == "", "\n")
print(dtfr['populacao'].isnull())
print(dtfr['populacao'] == 0)

#Descritivo e exploração de dados com pandas (groupbys)
print("groupby")
print(df.groupby('pais')['ano'].mean())

#insights
from matplotlib import pyplot as plt

plt.plot([1, 2, 3, 4, 5, 6], [6, 3, 6, 1, 2, 3])
