import plotly.express as px;
import pandas as pd; 

# Lendo dados
data = pd.read_excel('/home/gabrieldantas/DDN/BIBLIOTECAS_PYTHON/PANDAS/clientes_renamed.xlsx')

fig = px.violin(
    data, 
    x="estadoCivil", 
    y="valorCredito", 
    box=True,
    color="sexo", 
    title="Valor de crédito concedido segundo o estado civil"
)

fig.show()