# import matplotlib.pyplot as plt;
# import seaborn as sns;
# import plotly.express as px;
import plotly.graph_objects as go;
import pandas as pd;

# Lendo dados
data = pd.read_excel('/home/gabrieldantas/DDN/BIBLIOTECAS_PYTHON/PANDAS/clientes_renamed.xlsx');

# Agrupando dados
data_grouped = data.groupby(['nivelEscolaridade']).mean().reset_index()
print(data_grouped.columns())

# ----------------------------------------------------
fig = go.Figure()

fig.add_trace(
    go.Bar(
        x = data_grouped['nivelEscolaridade'],
        y = data_grouped['PAY_AMT1'],
        marker_color='Red',
        name='Valor pago No mês 1'
    )
)

fig.add_trace(
    go.Bar(
        x = data_grouped['nivelEscolaridade'],
        y = data_grouped['PAY_AMT2'],
        marker_color='blue',
        name='Valor pago No mês 2'
    )
)

fig.add_trace(
    go.Bar(
        x = data_grouped['nivelEscolaridade'],
        y = data_grouped['PAY_AMT3'],
        marker_color='yellow',
        name='Valor pago No mês 3'
    )
)

fig.add_trace(
    go.Bar(
        x = data_grouped['nivelEscolaridade'],
        y = data_grouped['PAY_AMT4'],
        marker_color='green',
        name='Valor pago No mês 4'
    )
)

fig.add_trace(
    go.Bar(
        x = data_grouped['nivelEscolaridade'],
        y = data_grouped['PAY_AMT5'],
        marker_color='orange',
        name='Valor pago No mês 5'
    )
)
fig.add_trace(
    go.Bar(
        x = data_grouped['nivelEscolaridade'],
        y = data_grouped['PAY_AMT6'],
        marker_color='gray',
        name='Valor pago No mês 6'
    )
)

fig.update_layout(
    yaxis = dict(
        title="Valor pagamento em 2005",
        titlefont_size=25,
        tickfont_size=25
    ),
    xaxis = dict(
        title="Nível Escolaridade",
        titlefont_size=25,
        tickfont_size=25
    )
)

fig.show()