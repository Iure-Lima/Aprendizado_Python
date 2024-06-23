lista = list()
listaPares = list()
listaImpares = list()

while True:
    lista.append(int(input("Digite um valor: ")))
    op = input("Quer continuar? [S/N] ").strip().lower()
    if op == 'n': break

for num in lista:
    if num % 2 == 0: listaPares.append(num)
    else: listaImpares.append(num)

print("-="*20)
print(f"A lista completa é {lista}")
print(f"A lista de pares é {listaPares}")
print(f"A lista de impares é {listaImpares}")