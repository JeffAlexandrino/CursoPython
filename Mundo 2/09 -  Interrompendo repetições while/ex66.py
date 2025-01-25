soma = cont = 0
while True: 
    num = int(input('Digite um valor (1000 para parar): '))
    if num == 1000:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}.')