jogador = {}
jogador['nome'] = input("Nome do jogador: ")
num_partidas = int(input(f"Total de partidas do jogador {jogador['nome']}: "))
jogador['gols'] = []

for i in range(num_partidas):
    gols = int(input(f"Total de gols na partida {i+1}: "))
    jogador['gols'].append(gols)

jogador['total'] = sum(jogador['gols'])

print("-=" * 30)
print(jogador)
print("-=" * 30)

for chave, valor in jogador.items():
    print(f"O campo {chave} tem o valor {valor}")
print("-=" * 30)
print(f"O jogador {jogador['nome']} jogou {num_partidas} partidas.")
for i, gols in enumerate(jogador['gols']):
    print(f"    => Na partida {i+1}, fez {gols} gols.")
print(f"Foi um total de {jogador['total']} gols.")