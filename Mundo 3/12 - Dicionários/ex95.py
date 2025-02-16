time = []
while True:
    jogador = {}
    jogador['nome'] = input("Nome do jogador: ")
    num_partidas = int(input(f"Total de partidas de {jogador['nome']}: "))
    jogador['gols'] = []
    for i in range(num_partidas):
        gols = int(input(f"  Gols na partida {i+1}: "))
        jogador['gols'].append(gols)
    jogador['total'] = sum(jogador['gols'])
    time.append(jogador)
    
    while True:
        resp = input("Quer continuar? [S/N]: ").strip().upper()
        if resp in 'SN':
            break
        print("Apenas S ou N.")
    if resp == 'N':
        break

print("-=" * 25)
print(f"{'Cod':<4}{'Nome':<15}{'Gols':<20}{'Total':<6}")
print("-" * 50)
for i, jogador in enumerate(time):
    print(f"{i:<4}{jogador['nome']:<15}{str(jogador['gols']):<20}{jogador['total']:<6}")
print("-" * 50)
