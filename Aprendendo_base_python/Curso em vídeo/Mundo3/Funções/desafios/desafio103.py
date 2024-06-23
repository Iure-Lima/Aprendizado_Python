def jogador(nome = "", gols = "0"):
    texto = ""
    if gols.isnumeric(): gols = int(gols)
    else: gols = 0

    if nome != "": texto = f"O jogador {nome} fez {gols} gol(s) no campeonato."
    else: texto = f"O jogador <desconhecido> fez {gols} gol(s) no campeonato."

    return texto


nome = input('Nome do jogador: ').capitalize()
gols = input("Quantidade de gols: ")
print(jogador(nome,gols))