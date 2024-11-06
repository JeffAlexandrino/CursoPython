v = int(input('Digite o valor: '))
fatorial = 1

for i in range(1, v + 1):
    fatorial *= i

print("O fatorial de {} é {}.".format(v, fatorial))

