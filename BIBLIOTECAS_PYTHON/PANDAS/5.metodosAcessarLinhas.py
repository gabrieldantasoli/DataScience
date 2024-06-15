import pandas as pd;

data = pd.read_excel('/home/gabrieldantas/DDN/BIBLIOTECAS_PYTHON/PANDAS/clientes_renamed.xlsx');

# # Acessar linha pelo ID
# print(data.loc[0])

# # Acessar linhas por intervalo
# print(data.loc[0:2])


# # Acessar linhas por intervalo e atributo
# print(data.loc[0:100, ['idade', 'sexo']])

# # Acessar linhas por posição
# print(data.iloc[0:10, 0:5])

# Acessar linhas a partir de máscaras booleanas
print(data[data['ID'] % 2 == 0])
