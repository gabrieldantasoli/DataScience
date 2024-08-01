import pandas as pd;

data = pd.read_csv("/home/gabrieldantas/DDN/BIBLIOTECAS_PYTHON/PANDAS/credit_card_clients.csv")
print(data)

# Removendo duplicatas
# drop_duplicates()
data1 = data.drop_duplicates(
    subset='ID',  # Especifica uma coluna ou lista de rótulos de colunas. Padrão None
    keep='first', # fisrt = só deixa a primeira
                  # last  = só deixa a ultima
                  # False = elimina todas as duplicatas
    inplace=False # remove linhas como duplicatas se True
)
print(data1)