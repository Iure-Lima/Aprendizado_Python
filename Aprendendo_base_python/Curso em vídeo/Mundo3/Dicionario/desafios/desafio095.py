jogadores = []

while True:
    jogador = {}
    jogador['nome'] = str(input('Nome do jogador: '))
    total_partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    gols = []
    for i in range(0, total_partidas):
        gols.append(int(input(f"    Quantos gols na partida {i}? ")))
    jogador["gols"] = gols[:]
    jogador["total"] = sum(gols)
    del gols
    jogadores.append(jogador.copy())

    while True:
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if continuar in 'SN': break
        print("Digite apenas S ou N")
    if continuar in 'N': break


print("-="*20)
print("code", end=' ')
for i in jogador.keys():
    print(f"{i:<15}", end="")
print()
for i, jogador in enumerate(jogadores):
    print(f"{i:>2}", end="")
    for j in jogador.values():
        print(f"{str(j):<15}",end="")
    print()
while True:
    busca = int(input("Mostrar dados de qual jogador? (999) para parar "))
    if busca == 999: break

    if busca >= 0 and busca <= len(jogadores):
        print(f"Levantamento do jogador {jogadores[busca]['nome']}")
        for i, g in enumerate(jogadores[busca]['gols']):
            print(f"    No jogo {i} fez {g} gols.")
    else:
        print("\033[31mERRO! Digite um valor valido!\033[m")