import pandas as pd;

data = pd.read_excel("/home/gabrieldantas/DDN/BIBLIOTECAS_PYTHON/PANDAS/clientes_renamed.xlsx")

# Extraindo um sumário das estatísticas descritivas
# COUNT = Total de valores não nulos
# MEAN  = média dos valores
# STD   = desvio padrão dos valores
# MIN   = mínimo
# 3 quartis abaixo
# 25%   = 25% abaixo e 75% acima
# 50%   = 50% abaixo e 50% acima
# 75%   = 75% abaixo e 25% acima
# MAX   = máximo 
print(data.describe())

print(data[['ID','PAY_AMT5']].describe())