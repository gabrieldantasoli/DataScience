import plotly.graph_objects as go
import pandas as pd
from plotly.subplots import make_subplots

# Lendo dados
data = pd.read_excel('/home/gabrieldantas/DDN/BIBLIOTECAS_PYTHON/PANDAS/clientes_renamed.xlsx')

# Agrupando dados
data_grouped = data.groupby(['idade']).mean().reset_index()

# Criando subplots
fig = make_subplots(
    rows=3,
    cols=2,
    shared_yaxes=True,
    subplot_titles=("JANEIRO", "FEVEREIRO", "MARÇO", "ABRIL", "MAIO", "JUNHO")
)

# Adicionando os traços aos subplots
fig.add_trace(
    go.Scatter(
        x=data_grouped["idade"],
        y=data_grouped["PAY_AMT1"],
        line=dict(color='red', width=1.5),
        name="valor pago no mes 1"
    ),
    row=1,
    col=1
)

fig.add_trace(
    go.Scatter(
        x=data_grouped["idade"],
        y=data_grouped["PAY_AMT2"],
        line=dict(color='blue', width=1.5),
        name="valor pago no mes 2"
    ),
    row=1,
    col=2
)

fig.add_trace(
    go.Scatter(
        x=data_grouped["idade"],
        y=data_grouped["PAY_AMT3"],
        line=dict(color='green', width=1.5),
        name="valor pago no mes 3"
    ),
    row=2,
    col=1
)

fig.add_trace(
    go.Scatter(
        x=data_grouped["idade"],
        y=data_grouped["PAY_AMT4"],
        line=dict(color='orange', width=1.5),
        name="valor pago no mes 4"
    ),
    row=2,
    col=2
)

fig.add_trace(
    go.Scatter(
        x=data_grouped["idade"],
        y=data_grouped["PAY_AMT5"],
        line=dict(color='purple', width=1.5),
        name="valor pago no mes 5"
    ),
    row=3,
    col=1
)

fig.add_trace(
    go.Scatter(
        x=data_grouped["idade"],
        y=data_grouped["PAY_AMT6"],
        line=dict(color='brown', width=1.5),
        name="valor pago no mes 6"
    ),
    row=3,
    col=2
)

fig.update_yaxes(title_text="Valor pago", row=1, col=1, titlefont_size=8)
fig.update_xaxes(title_text="Valor pago", row=1, col=1, titlefont_size=8)
# Atualizando layout
fig.update_layout(height=900, width=1000, title_text="Extrato bancário dos clientes segundo o nível de escolaridade para os últimos 6 meses")

fig.show()
