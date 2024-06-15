import numpy as np;

# Instalando biblioteca que lê imagens e transforma em array
# !pip install rasterio
# pip install matplotlib
import rasterio;
from rasterio.plot import show;

# transformando a imagen em array
dataset = rasterio.open('./img.webp')
datasetArray = dataset.read(1)

print('FORMATO: ', datasetArray.shape)
print('DIMENSÃO: ', datasetArray.ndim)
print('TIPO DE DADO: ', datasetArray.dtype)
print('COMPRIMENTO DE UM ELEMENTO DA ARRAY: ', datasetArray.itemsize)
print('NÚMERO DE ELEMENTOS: ', datasetArray.size)