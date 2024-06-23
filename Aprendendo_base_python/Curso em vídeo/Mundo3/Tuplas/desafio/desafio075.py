valores = (int(input("Digite um número: ")),int(input("Digite outro número: ")),
           int(input("Digite mais um número: ")),int(input("Digite o último número: ")))
print(f"Os valores digitados foram {valores}")
print(f"O número 9 apareceu {valores.count(9)} vezes")
if 3 in valores:
    print(f"O valor 3 apareceu na {valores.index(3) + 1} posição")
else: print("O valor 3 não foi encontrado na lista")
print(f"Os valores pares digitados foram ", end="")
for n in valores:
    if n % 2 == 0: print(n, end=" ")