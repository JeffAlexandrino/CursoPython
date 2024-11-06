primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA ?: '))

termo = primeiro
cont = 1
mais = 10
total = 0

while mais != 0:
    total = total + mais
    while cont <= total:
        print(termo, end=' ')
        termo += razao
        cont += 1
    mais = int(input('Quantos termos vc quer mostrar a mais?  '))
print('Progressão finalizada com {} termos'.format(total))