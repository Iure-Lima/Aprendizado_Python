listaNumeros = []
menor = 0
maior = 0

for i in range(0,5):
    number = int(input(f"Digite um valor para a posição {i}: "))
    listaNumeros.append(number)
    if i == 0:
        menor = number
        maior = number
    else:
        if number < menor: menor = number
        if number > maior: maior = number


print("-="*20)
print(f"Voçê digitou os valores {listaNumeros}")
print(f"O maior valor digitado foi {maior} nas posições ",end="")
for i, j in enumerate(listaNumeros):
    if j == maior:
        print(f"{i}...", end="")
print(f"\nO menor valor digitado foi {menor} nas posições ",end="")
for i, j in enumerate(listaNumeros):
    if j == menor:
        print(f"{i}...", end="")