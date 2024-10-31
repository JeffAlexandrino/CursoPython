jeff = input('primeiro aluno:')
joao = input('segundo aluno:')
luiz = input('terceiro aluno:')
fulano = input('quarto aluno:')

import random

lista=[jeff, joao, luiz, fulano]
b=random.sample(lista, k=len(lista))

print(f'os alunos escolhidos na sequencia foram {b}')

#outra forma de fazer
from random import shuffle
shuffle(lista)
print('a ordem de apresentação será')
print(lista)
#Shuffle não mostra a lista numa ordem aleatória, ele altera a ordem dentro da lista