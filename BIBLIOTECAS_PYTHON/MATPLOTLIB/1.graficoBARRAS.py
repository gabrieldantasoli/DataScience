# !pip install seaborn
# !pip install plotly

import matplotlib.pyplot as plt;
import seaborn as sns;
import plotly.express as px;
import plotly.graph_objects as go;
import pandas as pd;

data = pd.read_excel('/home/gabrieldantas/DDN/BIBLIOTECAS_PYTHON/PANDAS/clientes_renamed.xlsx')

# Agrupando dados
data_grouped = data.groupby(['nivelEscolaridade']).mean().reset_index()

# GRÁFICO COM A MATPLOTLIB
# Média do valor de crédito concedido segundo o nível de escolaridade
plt.figure(
    figsize=(10, 10)
)
plt.bar(data_grouped['nivelEscolaridade'], data_grouped['valorCredito'])
plt.title('Média do Valor de Crédito por Nível de Escolaridade')
plt.xlabel('Nível de Escolaridade')
plt.ylabel('Média do Valor de Crédito')
plt.xticks(rotation=45)  # Rotaciona os labels do eixo x para melhor visualização
plt.tight_layout()  # Ajusta automaticamente os parâmetros da figura para dar espaço aos labels
plt.show()  # Mostra o gráficoplt.title('Média do Valor de Crédito por Nível de Escolaridade')

# print(data.columns)