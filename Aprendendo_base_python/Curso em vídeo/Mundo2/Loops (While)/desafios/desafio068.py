from random import randint
print("-="*13)
print("Vamos jogar ímpar ou par")
vence = 0

while True:
    print("-=" * 13)
    jogadorDedos = int(input("Digite um valor de 0 a 10: "))
    parImpar = input("Par ou Impar? [P/I] ").strip().lower()
    computadorDedos = randint(0, 10)
    somaDedos = jogadorDedos + computadorDedos

    print("-"*50)
    print(f"Você jogou {jogadorDedos} e o computador {computadorDedos}. O total deu {somaDedos} {'PAR' if somaDedos % 2 == 0 else 'IMPAR'}")
    print("-"*50)

    if somaDedos % 2 == 0:
        if parImpar == "p":
            print("Você venceu")
            print("Vamos jogar novamente ...")
            vence+=1
        else:
            print("Você perdeu")
            break
    else:
        if parImpar == "i":
            print("Você venceu")
            print("Vamos jogar novamente ...")
            vence+=1
        else:
            print("Você perdeu")
            break
print(f"GAME OVER, você venceu {vence} vezes")