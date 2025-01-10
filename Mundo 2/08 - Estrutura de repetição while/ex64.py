num = cont = soma = 0
num = int(input('Digite um número [0 para parar]: '))
while num != 0: 
    soma += num
    cont += 1 
    num = int(input('Digite um número [0 para parar]: '))
print('{} números digitados, A soma entre eles é {}'.format(cont, soma))
