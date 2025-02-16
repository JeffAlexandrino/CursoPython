import random

def sorteia(numeros):
    for _ in range(5):
        numeros.append(random.randint(1, 100))
    print(f'Números sorteados: {numeros}')

def somaPar(numeros):
    soma = sum(num for num in numeros if num % 2 == 0)
    print(f'Soma dos números pares: {soma}')

numeros = []
sorteia(numeros)
somaPar(numeros)