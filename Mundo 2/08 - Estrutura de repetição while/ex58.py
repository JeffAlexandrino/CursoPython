from random import randint

computador = randint(0, 10)
print('Sou seu computador... Pensei em um número entre 0 e 10.')
print('Qual foi?')

acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Seu número: '))
    palpites += 1
    if jogador == computador:
        acertou = True
        print('Acertou!')  
    else:
        if jogador < computador:
            print('Mais, tente de novo.')
        elif jogador > computador:
            print('Menos, tente de novo.')

print('Acertou em {} tentativas.'.format(palpites))
