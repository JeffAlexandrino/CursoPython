tot18 = totH = totM20 = 0
while True:
    age = int(input('Idade: '))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if age >= 18:
        tot18 += 1
    if sex == 'M':
        totH += 1
    if sex == 'F' and age < 20
        totM20 += 1
    resp = ' '
    while resp not in 'SN': 
        resp  = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Total de Homens: {totH}')
print(f'Total de mulheres com menos de 20 anos: {totM20}')
