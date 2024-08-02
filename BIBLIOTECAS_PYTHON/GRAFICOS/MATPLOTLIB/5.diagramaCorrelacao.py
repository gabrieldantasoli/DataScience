import matplotlib.pyplot as plt;
import seaborn as sns;
import plotly.express as px;
import plotly.graph_objects as go;
import pandas as pd; 

# Lendo dados
data = pd.read_excel('/home/gabrieldantas/DDN/BIBLIOTECAS_PYTHON/PANDAS/clientes_renamed.xlsx')

data.drop(["Unnamed: 0", "ID"], axis=1, inplace=True)

plt.figure(figsize=(20,20))

sns.heatmap(data.corr(), annot=True, cmap='coolwarm')

plt.show()