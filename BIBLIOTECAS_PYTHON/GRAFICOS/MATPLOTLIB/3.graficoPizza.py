import matplotlib.pyplot as plt;
import seaborn as sns;
import plotly.express as px;
import plotly.graph_objects as go;
import pandas as pd;

# Lendo dados
data = pd.read_excel('/home/gabrieldantas/DDN/BIBLIOTECAS_PYTHON/PANDAS/clientes_renamed.xlsx');

# Agrupando dados
data_grouped = data.groupby(['sexo']).mean().reset_index()
# print(data_grouped.columns)

fig, ax = plt.subplots(figsize=(10,10))

ax.pie(
    data_grouped['valorCredito'], 
    labels=data_grouped['sexo'], 
    autopct='%.2f%%', 
    shadow=True,
    startangle=60,
    colors=['Red', 'Seagreen'],
    explode=(0.04, 0)
)

plt.show()