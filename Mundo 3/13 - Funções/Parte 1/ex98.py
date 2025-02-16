from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = -passo

    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= passo
        print('FIM!')

# a) de 1 até 10, de 1 em 1
contador(1, 10, 1)
print('-=' * 20)
# b) de 10 até 0, de 2 em 2
contador(10, 0, 2)
print('-=' * 20)
# c) uma contagem personalizada
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)