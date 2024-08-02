import matplotlib.pyplot as plt;
import seaborn as sns;
import plotly.express as px;
import plotly.graph_objects as go;
import pandas as pd; 

# Lendo dados
data = pd.read_excel('/home/gabrieldantas/DDN/BIBLIOTECAS_PYTHON/PANDAS/clientes_renamed.xlsx');

# Agrupando dados
data_grouped = data.groupby(['idade']).mean().reset_index()

plt.figure(
    figsize=(10,10)
)

plt.plot(data_grouped['idade'], data_grouped['valorCredito'])

plt.title('Valor de crédito por idade')
plt.xlabel('Idade')
plt.ylabel('Média do Valor de Crédito')
plt.tight_layout()  # Ajusta automaticamente os parâmetros da figura para dar espaço aos labels

plt.grid(color='lightgray')
plt.show()  # Mostra o gráficoplt.title('Média do Valor de Crédito por Nível de Escolaridade')

