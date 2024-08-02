import matplotlib.pyplot as plt;
import seaborn as sns;
# import plotly.express as px;
# import plotly.graph_objects as go;
import pandas as pd;

# Lendo dados
data = pd.read_excel('/home/gabrieldantas/DDN/BIBLIOTECAS_PYTHON/PANDAS/clientes_renamed.xlsx');

# Agrupando dados
data_grouped = data.groupby(['idade']).mean().reset_index()
# print(data_grouped.columns)

# Extrato bancário dos clientes segundo o nível de escolaridade para os últimos 4 mese
fig, axes = plt.subplots(2, 2, figsize=(10, 10))

sns.lineplot(data=data_grouped, x='idade', y='PAY_AMT1', palette="set2", ax=axes[0, 0]).set(title="Extrato 1")
sns.lineplot(data=data_grouped, x='idade', y='PAY_AMT2', palette="set2", ax=axes[0, 1]).set(title="Extrato 2")
sns.lineplot(data=data_grouped, x='idade', y='PAY_AMT3', palette="set2", ax=axes[1, 0]).set(title="Extrato 3")
sns.lineplot(data=data_grouped, x='idade', y='PAY_AMT4', palette="set2", ax=axes[1, 1]).set(title="Extrato 4")

plt.show()