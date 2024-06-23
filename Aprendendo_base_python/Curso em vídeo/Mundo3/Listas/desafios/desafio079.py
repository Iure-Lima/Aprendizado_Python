listaNumeros = []

while True:
    nu = int(input("Digite um valor: "))
    if nu not in listaNumeros:
        listaNumeros.append(nu)
    print("Valor adicionado com sucesso...")
    opc = input("Quer continuar? [S/N] ").strip().lower()
    if opc == 'n': break
print("-="*20)
listaNumeros.sort()
print(f"Você digitou os valores {listaNumeros}")