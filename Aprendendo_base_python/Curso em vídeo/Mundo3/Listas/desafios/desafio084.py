pessoas = []
pessoa = []

maxPessoaPeso = minPessoaPeso = 0

while True:
    pessoa.append(input("Nome: "))
    pessoa.append(float(input("Peso: ")))

    if len(pessoas) == 0:
        maxPessoaPeso = minPessoaPeso = pessoa[1]
    else:
        if pessoa[1] > maxPessoaPeso: maxPessoaPeso = pessoa[1]
        if pessoa[1] < minPessoaPeso: minPessoaPeso = pessoa[1]
    pessoas.append(pessoa[:])
    pessoa.clear()

    continuar = input("Deseja continuar: [S/N] ").strip().lower()
    if continuar in 'n': break

print("-="*20)
print(f"Ao todo temos {len(pessoas)}")
print(f"O maior peso foi de {maxPessoaPeso}", end=" ")
for p in pessoas:
    if p[1] == maxPessoaPeso: print(p[0], end=" ")
print(f"\nO menor peso foi de {minPessoaPeso}", end=" ")
for p in pessoas:
    if p[1] == minPessoaPeso: print(p[0], end=" ")