from utilidadescev import moeda
from utilidadescev import dado


input_usuario = dado.leiaDinheiro("Digite o preço: \n")

print(moeda.resumo(input_usuario, 20, 12))
