import numpy as np;

a = np.arange(0, 100)
print('Formato: ', a.shape, '\nDimensão: ', a.ndim)
print(a)

print('--------------------------------------------------------------')

# RESHAPE : altera o formato da matriz
b = a.reshape(10, 10)
print('Formato: ', b.shape, '\nDimensão: ', b.ndim)
print(b)

print('--------------------------------------------------------------')

# Convertendo 1D em 2D
c = a[np.newaxis]
print('Formato: ', c.shape, '\nDimensão: ', c.ndim)
print(c)

print('--------------------------------------------------------------')

# Criando arrays de tamanhos dados.
d = np.ones([2,2])
print(d)