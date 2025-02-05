import random
import time  # Importação correta para a função sleep

resultados = {
    'Jogador 1': random.randint(1, 6),
    'Jogador 2': random.randint(1, 6),
    'Jogador 3': random.randint(1, 6),
    'Jogador 4': random.randint(1, 6)
}

print("Resultados dos jogadores:")
for jogador, resultado in resultados.items():
    print(f"{jogador} tirou {resultado} no dado.")
    time.sleep(1) 

resultados_ordenados = sorted(resultados.items(), key=lambda item: item[1], reverse=True)
print('-=' * 20)
print("\nClassificação dos jogadores:")
for i, (jogador, resultado) in enumerate(resultados_ordenados, start=1):
    print(f"{i}º lugar: {jogador} com {resultado} no dado.")
    time.sleep(1)  