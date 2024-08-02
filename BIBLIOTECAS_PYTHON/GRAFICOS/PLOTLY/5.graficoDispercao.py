import matplotlib.pyplot as plt;
import seaborn as sns;
import plotly.express as px;
import plotly.graph_objects as go;
import pandas as pd; 

# Lendo dados
data = pd.read_excel('/home/gabrieldantas/DDN/BIBLIOTECAS_PYTHON/PANDAS/clientes_renamed.xlsx')

fig = px.scatter(data, x="PAY_0", y="PAY_AMT1", color="estadoCivil", size="valorCredito", title="Síntese da situação dos clientes segundo o estado civil")

fig.show()