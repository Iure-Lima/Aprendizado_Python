media = 0
idadeHomemMaisVelho = 0
nomeHomemMiasVelho = ""
totalMulherosComMenosDeVinte = 0

for i in range(0,4):
    print(f"-----{i + 1} PESSOA-----")
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().lower()

    media += idade

    if sexo == "m":
        if idadeHomemMaisVelho < idade:
            idadeHomemMaisVelho = idade
            nomeHomemMiasVelho = nome
    elif sexo == "f":
        if idade < 20: totalMulherosComMenosDeVinte += 1

media = media / 4

print(f"A média de idade do grupo é de {media:.1f} anos")
print(f"O homem mais velhor tem {idadeHomemMaisVelho} anos e se chama {nomeHomemMiasVelho}")
print(f"Ao todo são {totalMulherosComMenosDeVinte} mulheres com menos de 20 anos")