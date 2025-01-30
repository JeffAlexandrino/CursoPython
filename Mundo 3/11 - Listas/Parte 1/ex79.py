num = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado. Não será adicionado.')
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
print('-=' * 30)
num.sort()
print(f'Valores digitados: {num}')