soma = 0

for c in range(6):
    numero = int(input(f"Digite o {c+1}º número: "))
    if numero % 2 == 0:
        soma += numero

print("A soma dos números pares é:", soma)