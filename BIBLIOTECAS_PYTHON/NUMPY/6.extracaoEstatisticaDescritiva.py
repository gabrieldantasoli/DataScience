import numpy as np;
import rasterio;
from rasterio.plot import show;

dataset = rasterio.open('/home/gabrieldantas/DDN/BIBLIOTECAS_PYTHON/NUMPY/img.webp')
datasetArray = dataset.read(1)

# Calculando a média
print('Média: ', datasetArray.mean())

# Calculando o desvio padrão
print('DP: ', datasetArray.std())

# Valor minimo
print('MIN: ', datasetArray.min())

# Valor máximo
print('MAX: ', datasetArray.max())

# Somando todos os valores
print('Sum: ', datasetArray.sum())

#identificando valores unicos
unique_values = np.unique(datasetArray)
print(unique_values)