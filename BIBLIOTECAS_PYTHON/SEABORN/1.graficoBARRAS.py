import matplotlib.pyplot as plt;
import seaborn as sns;
# import plotly.express as px;
# import plotly.graph_objects as go;
import pandas as pd;

# Lendo dados
data = pd.read_excel('/home/gabrieldantas/DDN/BIBLIOTECAS_PYTHON/PANDAS/clientes_renamed.xlsx');

# Agrupando dados
data_grouped = data.groupby(['nivelEscolaridade']).mean().reset_index()
# print(data_grouped.columns())

# Extrato bancário dos clientes segundo o nível de escolaridade para os últimos 4 mese
fig, axes = plt.subplots(2, 2, figsize=(10, 10))

sns.barplot(data=data_grouped, x="nivelEscolaridade", y="PAY_AMT1", ax=axes[0, 0])
sns.barplot(data=data_grouped, x="nivelEscolaridade", y="PAY_AMT2", ax=axes[0, 1])
sns.barplot(data=data_grouped, x="nivelEscolaridade", y="PAY_AMT3", ax=axes[1, 0])
sns.barplot(data=data_grouped, x="nivelEscolaridade", y="PAY_AMT4", ax=axes[1, 1])

plt.tight_layout()
plt.show()

#129