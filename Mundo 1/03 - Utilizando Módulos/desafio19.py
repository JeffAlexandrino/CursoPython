jeff=str(input('primeiro aluno:'))
joao=str(input('segundo aluno:'))
luiz=str(input('terceiro aluno:'))
fulano=str(input('quarto aluno:'))

lista=[jeff, joao, luiz, fulano]

import random

s=random.choice(lista)
print(f'o aluno escolhido foi {s}')