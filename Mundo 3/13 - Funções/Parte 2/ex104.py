def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except ValueError:
            print("Erro! Digite um número inteiro válido.")
            continue
        else:
            return n

# Exemplo de uso
n = leiaInt("Digite um n: ")
print(f"Você digitou o número {n}")