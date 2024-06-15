import pandas as pd;

data = pd.read_excel('/home/gabrieldantas/DDN/BIBLIOTECAS_PYTHON/PANDAS/clientes_renamed.xlsx');

# iterrows : permite iteramos nas linhas do dataframe como se fossem uma série.

for index,row in data.iterrows():
    print(index)
    print(row)

# Acessando uma coluna
print(data['nivelEscolaridade'])
print(data.ID)

# Acessando MÚLTIPLAS COLUNAS
print(data[['valorCredito', 'idade', 'nivelEscolaridade']])

# Filtrando Colunas
print(data.filter(
    like='PAY'
))