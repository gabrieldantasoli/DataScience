# pip install openpyxl
import pandas as pd;

data = pd.read_csv('/home/gabrieldantas/DDN/BIBLIOTECAS_PYTHON/PANDAS/credit_card_clients.csv')

# INFO = informações técnicas sobre o dataframe
print(data.info())

# Visiualizando as primeiras linhas
print(data.head(10)) # qtd de linhas

# visualizando as ultimas linhas
print(data.tail(10)) # qtd de linhas

# dimensão
print('FORMATO: ', data.shape, ' DIMENSÃO: ', data.ndim)

# Renomeando colunas do dataframe
print('-------------------------------------------')
data_renamed = data.rename(columns={
    'LIMIT_BAL': 'valorCredito',
    'SEX': 'sexo',
    'EDUCATION': 'nivelEscolaridade',
    'MARRIAGE': 'estadoCivil',
    'AGE': 'idade'
})

#excluindo colunas
data_renamed.drop(["default payment next month"], axis=1, inplace=True)

print(data_renamed.info())
# Escrevendo dados tabulares
data_renamed.to_excel("clientes_renamed.xlsx")