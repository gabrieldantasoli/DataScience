import pandas as pd;

data = pd.read_csv("/home/gabrieldantas/DDN/BIBLIOTECAS_PYTHON/PANDAS/credit_card_clients.csv")
print(data)

data_grouped = data.groupby(['EDUCATION']).mean().reset_index()
print(data_grouped)