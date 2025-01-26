from random import randint

num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))  # Gera 5 números aleatórios
print(f'Os valores sorteados foram: ', end='')
for n in num:
    print(f'{n}', end=' ')
print('\n' + '=' * 40)
print(f'O maior valor sorteado foi: {max(num)}')
print(f'O menor valor sorteado foi: {min(num)}')
