## llenar una lista
x = []
N= 10
for i in range (N + 1):
    x.append(i**2)
print(x)

## comprenhension list

y = [i**2 for i in range (N+1)]
print(y)
## numeros impares
z = [2*i+1 for i in range (N+1)]
print(z)

#haciendo saltos

r = list(range(2*N))
print(r[0::2])
print(r[1::2])

