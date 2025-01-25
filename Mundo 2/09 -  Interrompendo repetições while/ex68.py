from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    comp = randint(0, 10)
    total = jogador + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P/I]?: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {comp}. Total de {total}.', end=' ')
    print('Deu PAR' if total % 2 == 0 else 'Deu ÍMPAR')
    if tipo == 'P':  # Jogador escolheu PAR
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':  # Jogador escolheu ÍMPAR
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar mais uma vez...')
print(f'Fim de jogo! Você venceu {v} vezes.')
