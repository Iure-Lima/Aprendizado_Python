from random import  randint

escolhaRobo = randint(0,10)
numeroTentativas = 0
print("Sou um computador ...")
print("Acabei de pensar em um número entre 0 e 10.")
print("Será que você consegue adivinhar qual foi? ")

while True:
    numeroTentativas += 1
    escolhaUsuario = int(input("Qual o seu palpite? "))

    if escolhaRobo == escolhaUsuario:
        break
    else:
        if escolhaUsuario > escolhaRobo:
            print("Menos... Tente outra vez.")
        else:
            print("Mais... Tente outra vez")


print(f"Acertou com {numeroTentativas} tantativas. Parabéns")