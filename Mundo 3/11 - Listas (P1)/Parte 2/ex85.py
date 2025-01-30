numeros = [[], []]  # Lista para armazenar pares e ímpares separadamente

for i in range(7):
    valor = int(input(f"Digite o {i+1}º valor: "))
    if valor % 2 == 0:
        numeros[0].append(valor)  #Adiciona o valor na lista de pares
    else:
        numeros[1].append(valor)  #Adiciona o valor na lista de ímpares

# Ordena as listas de pares e ímpares
numeros[0].sort()
numeros[1].sort()

# Exibe os valores pares e ímpares em ordem crescente
print(f"Valores pares: {numeros[0]}")
print(f"Valores ímpares: {numeros[1]}")