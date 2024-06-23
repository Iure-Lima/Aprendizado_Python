velocidade = int(input("Qual a velocidade atua do carro? "))

if velocidade > 80:
    print("Você ultrapassou o limite de 80KM por hora")
    print(f"Você recebeu uma multa de R${(velocidade - 80) *7}")


print("Tenha um bom dia e dirija com segurança!")