# INSTALAÇÃO DO NUMPY: !pip install numpy
import numpy as np;

# CRIANDO UMA MATRIZ A PARTIR DE UMA LISTA DE VALORES:
a = np.array([1, 2, 3])

# NDIM : indica a quantidade de dimensões.
print(a.ndim)

# SHAPE : retorna uma lista de inteiros que indicam o tamanho da array em cada dimensão.
print(a.shape)

# ARANGE : Cria uma matriz a partir de um range. (inicio, fim, passo)
b = np.arange(1,101, 2)

# LINSPACE : Cria uma matriz de valores espaçados linearmente. (inicio, fim, quantidade de elementos)
c = np.linspace(0, 10, 11)

print(c)