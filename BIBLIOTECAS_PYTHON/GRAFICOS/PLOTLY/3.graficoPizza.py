from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd

# Lendo dados
data = pd.read_excel('/home/gabrieldantas/DDN/BIBLIOTECAS_PYTHON/PANDAS/clientes_renamed.xlsx')

# Agrupando dados
data_grouped = data.groupby(['sexo']).mean().reset_index()

fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}]])

fig.add_trace(go.Pie(labels=data_grouped['sexo'], values=data_grouped['PAY_AMT1'], name="Janeiro"), 1, 1)
fig.add_trace(go.Pie(labels=data_grouped['sexo'], values=data_grouped['PAY_AMT2'], name="Fevereiro"), 1, 2)

fig.update_traces(hole=.3)

fig.update_layout(
    title_text="Extrato de pagamento de Janeiro e Fevereiro, de acordo com o sexo",
    annotations=[
        dict(text="Janeiro", x=.2, y=.5, font_size=14, showarrow=False),
        dict(text="Fevereiro", x=.81, y=.5, font_size=14, showarrow=False)
    ]
)

fig.show()

fig.write_html("extrato_sexo.html")