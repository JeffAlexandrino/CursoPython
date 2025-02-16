people = []
while True:
    person = {}
    person['name'] = input("Nome: ")
    person['sex'] = input("Sexo [M/F]: ").strip().upper()
    person['age'] = int(input("Idade: "))
    people.append(person)
    
    continue_prompt = input("Quer continuar? [S/N]: ").strip().upper()
    if continue_prompt == 'N':
        break
print('-=' * 30)
# A) Quantas pessoas foram cadastradas
total_people = len(people)
print(f"A) Total de pessoas cadastradas: {total_people}")

# B) A média de idade
total_age = sum(person['age'] for person in people)
average_age = total_age / total_people
print(f"B) Média de idade: {average_age:.2f}")

# C) Uma lista com as mulheres
women = [person['name'] for person in people if person['sex'] == 'F']
print(f"C) Lista de mulheres: {', '.join(women)}")

# D) Uma lista de pessoas com idade acima da média
above_average = [person['name'] for person in people if person['age'] > average_age]
print(f"D) Pessoas com idade acima da média: {', '.join(above_average)}")
