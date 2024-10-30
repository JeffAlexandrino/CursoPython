num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end = '')
        tot += 1
    else: 
        print('\033[031m', end = '')
    print('{} '.format(c), end='')
print('\n\33[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('Por isso ele é primo.')
else: 
    print('Por isso ele é não é primo.')
