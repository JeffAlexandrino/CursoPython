from datetime import date

def voto(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento

    if idade < 16:
        return "NEGADO"
    elif 16 <= idade < 18 or idade > 65:
        return "OPCIONAL"
    else:
        return "OBRIGATÓRIO"

ano = int(input("Ano de nascimento: "))
print(f"Com {ano} anos: voto {voto(ano)}")
