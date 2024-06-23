from random import randint

print("-"*30)
print(f"{'JOGA NA MEGA SENA':^30}")
print("-"*30)

jogos = int(input("Quantos jogos você quer sortear? "))
print(f"Sorteando {jogos} jogo(s)")
cont = 0
while True:
    jogo = [randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100)]
    jogo.sort()
    print(f"Jogo {cont +1}: {jogo}")
    cont+=1
    if cont >= jogos: break
print("BOA SORTE!")