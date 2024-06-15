# INSTALAÇÃO: !pip install pandas
import pandas as pd;

# Criando uma Series
clientes = [
    'Gabriel Dantas',
    'Maria cecília',
    'José dp Grau'
]

indices = [0, 1, 2]

serie = pd.Series(
    data=clientes,
    index=indices,
    name='Nome dos clientes'
)
print(clientes)
print(type(clientes))
print(serie)

print('------------------------------------------')

df = pd.DataFrame({
    'nome': [
        'Gabriel Dantas',
        'Maria cecília',
        'José do Grau'
    ],
    'idade': [ 20, 10, 47 ],
    'sexo': ['H', 'M', 'H'],  
})

print(df['nome'])