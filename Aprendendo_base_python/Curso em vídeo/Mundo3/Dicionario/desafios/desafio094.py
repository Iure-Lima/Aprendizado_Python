pessoas = []
while True:
    pessoa = {}
    pessoa['nome'] = str(input('Nome: '))

    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if pessoa['sexo'] in 'MF': break

        print("ERRO! Por favor digite apenas M ou F")

    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())

    while True:
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if continuar in 'SN': break
        print("ERRO! Por favor digite apenas S ou N")

    if continuar in 'N': break

mediaIdade = 0
for pessoa in pessoas:
    mediaIdade += pessoa['idade']
mediaIdade = mediaIdade / len(pessoas)

print(f"A) ao todo temos {len(pessoas)} pessoas cadastradas")
print(f"B) a média de idade é de {mediaIdade:.2f} anos.")
print("C) as mulheres cadastradas foram ",end="")
for pessoa in pessoas:
    if pessoa['sexo'] == 'F':
        print(f"{pessoa['nome']}, ", end="")
print("\nD) lista de pessoas que estão acima da média:")
for pessoa in pessoas:
    if pessoa['idade'] >= mediaIdade:
        print(f"    nome = {pessoa['nome']}; sexo = {pessoa['sexo']}; idade = {pessoa['idade']};")
print("<< ENCERRADO >>")