def ajuda(comando):
    help(comando)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print('\033[1;30;47m', end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print('\033[m', end='')

while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = input('Função ou Biblioteca > ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)