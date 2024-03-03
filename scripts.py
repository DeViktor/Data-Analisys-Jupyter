import pandas as pd

table = pd.DataFrame({ "nome": ["teste1", "teste2"], "idade": ["18", "19"]})

aux = pd.read_csv('./datas/fifa.csv')

#aux[["Name", "Nationality"]]
table.to_csv("teste_criar_csv", index=False)