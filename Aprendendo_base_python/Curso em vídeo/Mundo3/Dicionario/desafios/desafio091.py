from random import  randint
from time import sleep
from operator import itemgetter
jogadas = {
    "Jogador1": randint(1,6),
    "Jogador2": randint(1,6),
    "Jogador3": randint(1,6),
    "Jogador4": randint(1,6),
}
ranking = dict()

print("Valores sorteados")
for k,v in jogadas.items():
    print(f"{k} tirou {v} no dado")
    sleep(1)
print("-="*15)
ranking = sorted(jogadas.items(),key=itemgetter(1),reverse=True)
for i,v in enumerate(ranking):
    print(f"Colocação {i+1}: {v[0]} com {v[1]}")