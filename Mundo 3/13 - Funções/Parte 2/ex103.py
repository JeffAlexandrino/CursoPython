def ficha(nome='<desconhecido>', gols=0):
    """
    Exibe a ficha de um jogador de futebol.
    
    :param nome: Nome do jogador (opcional)
    :param gols: Número de gols marcados pelo jogador (opcional)
    """
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

# Programa principal
nome_jogador = input('Nome do jogador: ').strip()
gols_jogador = input('Número de gols: ').strip()

if gols_jogador.isdigit():
    gols_jogador = int(gols_jogador)
else:
    gols_jogador = 0

if nome_jogador == '':
    ficha(gols=gols_jogador)
else:
    ficha(nome_jogador, gols_jogador)