import pandas as pd;

data = pd.read_csv("/home/gabrieldantas/DDN/BIBLIOTECAS_PYTHON/PANDAS/credit_card_clients.csv")

# # Identificando os valores não nulos
# print(data.notnull())

# # Identificando os valores nulos
# print(data.isnull())

# # Somandos os valores nulos
# print(data.isnull().sum())

# # Somando os valores não nulos
# print(data.notnull().sum())

# # Filtrando valores
# dataFiltered = data[data['ID'].notnull()]
# print(dataFiltered)

# Excluindo linhas com valores nulos --- #NOTNA()
# data2 = data[data['ID'].notna()]
# print(data2)

# Outra forma de excluir valores nulos --- #DROPNA()
date3 = data.dropna(how='all')
print(date3)
