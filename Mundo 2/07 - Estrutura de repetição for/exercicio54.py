import datetime

anoAtual = datetime.datetime.now().year
anosNascimentos = []

maioridade = 18
maiores = 0
menores = 0

for c in range(7):
    ano = int(input(f"Digite o ano de nascimento da pessoa {c + 1}: "))
    anosNascimentos.append(ano)

for ano in anosNascimentos:
    idade = anoAtual - ano  
    if idade >= maioridade:
        maiores += 1  
    else:
        menores += 1  
print(f"Total de pessoas maiores de idade: {maiores}")
print(f"Total de pessoas menores de idade: {menores}")
