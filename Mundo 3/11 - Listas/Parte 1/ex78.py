listanum = []
max = 0
min = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        max = min = listanum[c]
    else:
        if listanum[c] > max:
            max = listanum[c]
        if listanum[c] < min:
            min = listanum[c]

print('=-' * 30)
print(f'Você digitou os valores: {listanum}')

print(f'O maior valor digitado foi: {max}.')
for i, v in enumerate(listanum):
    if v == max:
        print(f'O maior valor está na posição: {i}.')

print(f'O menor valor digitado foi: {min}.')
    if v == min:
        print(f'O menor valor está na posição {i}.')
