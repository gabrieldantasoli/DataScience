import pandas as pd;

data = pd.read_excel('/home/gabrieldantas/DDN/BIBLIOTECAS_PYTHON/PANDAS/clientes_renamed.xlsx');

print('---------------------------------')
# Acessando os rótulos das linhas
print(data.index)

print('---------------------------------')
#Acessando os rótulos das colunas
print(data.columns) #ou data.keys()

print('---------------------------------')
# Acessando os valores
print(data.values) # ou data.to_numpy()

print('---------------------------------')
# identificando os tipos de dados 
print(data.dtypes)
