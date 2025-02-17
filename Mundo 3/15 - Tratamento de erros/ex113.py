def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("Erro! Digite um número inteiro válido.")
            continue
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("Erro! Digite um número real válido.")
            continue
        else:
            return n

# Exemplo de uso
n_int = leiaInt("Digite um número inteiro: ")
print(f"Você digitou o número inteiro {n_int}")

n_float = leiaFloat("Digite um número real: ")
print(f"Você digitou o número real {n_float}")