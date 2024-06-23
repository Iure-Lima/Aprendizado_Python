jogador = {}

jogador["nome"] = str(input('Nome do Jogador: '))
total_partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
gols = []

for i in range(0, total_partidas):
    gols.append(int(input(f"    Quantos gols na partida {i}? ")))

jogador["gols"] = gols[:]
jogador["total"] = sum(gols)
del gols

print("-="*20)
print(jogador)
print("-="*20)
for k,v in jogador.items():
    print(f"O campo {k} tem o valor {v}")
print("-="*20)
print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas.")
for i,n in enumerate(jogador['gols']):
    print(f"  => Na partida {i}, fez {n} gols.")