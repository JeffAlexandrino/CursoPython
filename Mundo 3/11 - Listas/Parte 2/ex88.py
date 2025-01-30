import random

def gerar_palpites(qtd_jogos):
    palpites = []
    for _ in range(qtd_jogos):
        jogo = sorted(random.sample(range(1, 61), 6))
        palpites.append(jogo)
    return palpites

def main():
    print("-=" * 20)
    print("   Gerador de palpites da MEGA SENA!     ")
    print("-=" * 20)
    qtd_jogos = int(input("Quantos jogos você quer gerar? "))
    palpites = gerar_palpites(qtd_jogos)
    
    print("\nPalpites gerados:")
    for i, jogo in enumerate(palpites, 1):
        print(f"Jogo {i}: {jogo}")

if __name__ == "__main__":
    main()