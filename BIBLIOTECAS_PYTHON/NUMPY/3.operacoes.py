import numpy as np;

data = np.array([[1, 2], [3,4]])

ones = np.ones([2, 2])

# Somando dois arrays
sum = data + ones
print(sum)

print('---------------------------------------')
# Subtraindo dois arrays
sub = data - ones
print(sub)

print('---------------------------------------')
a = np.arange(1, 16)
b = np.zeros_like(a)
c = np.ones_like(a)

# Multiplicando dois arrays
mul = a * b
print(mul)

print('---------------------------------------')
# Dividindo dois arrays
div = a / a
print(div)

print('---------------------------------------')
# Somando array e constante
sumCons = a + 5
print(sumCons)

print('---------------------------------------')
# Multiplicando array e constante
mulCons = a * 100
print(mulCons)