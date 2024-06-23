from random import randint
from time import sleep

print("""
Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
""")

opcaoJogador = int(input("Qual é a sua jogada? "))
opcaoComputador = randint(0,2)
textoVencedor = ""

sleep(1)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
sleep(1)
print("-="*5)

if opcaoJogador == 0 and opcaoComputador == 0:
    print("Jogador jogou pedra")
    print("Computador jogou pedra")
    textoVencedor = "Empate"
elif opcaoJogador == 0 and opcaoComputador == 1:
    print("Jogador jogou pedra")
    print("Computador jogou papel")
    textoVencedor = "Computador Ganhou"
elif opcaoJogador == 0 and opcaoComputador == 2:
    print("Jogador jogou pedra")
    print("Computador jogou tesoura")
    textoVencedor = "Jogador Ganhou"
if opcaoJogador == 1 and opcaoComputador == 0:
    print("Jogador jogou papel")
    print("Computador jogou pedra")
    textoVencedor = "Jogador Ganhou"
elif opcaoJogador == 1 and opcaoComputador == 1:
    print("Jogador jogou papel")
    print("Computador jogou papel")
    textoVencedor = "Empate"
elif opcaoJogador == 1 and opcaoComputador == 2:
    print("Jogador jogou papel")
    print("Computador jogou tesoura")
    textoVencedor = "Computador Ganhou"
if opcaoJogador == 2 and opcaoComputador == 0:
    print("Jogador jogou tesoura")
    print("Computador jogou pedra")
    textoVencedor = "Computador Ganhou"
elif opcaoJogador == 2 and opcaoComputador == 1:
    print("Jogador jogou tesoura")
    print("Computador jogou papel")
    textoVencedor = "Jogador Ganhou"
elif opcaoJogador == 2 and opcaoComputador == 2:
    print("Jogador jogou tesoura")
    print("Computador jogou tesoura")
    textoVencedor = "Empate"


print("-="*5)
print(f"{textoVencedor}")