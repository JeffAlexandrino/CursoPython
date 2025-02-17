import moeda

# input_usuario = float(input("Digite o preço: \n"))
input_usuario = 423

print(f"A metade de {input_usuario} é {moeda.metade(input_usuario)}")
print(f"O dobro de {input_usuario} é {moeda.dobro(input_usuario)}")
print(f"Aumentando 10%, temos {moeda.aumentar(input_usuario, 10)}")
print(f"Diminuindo 10%, temos {moeda.diminuir(input_usuario, 10)}")
