numero = int(input("Digite um número: "))
cont = 0

for c in range(1, numero+1):
    if numero % c == 0:
        print(f"\033[0;33m{c}\033[m", end=" ")
        cont+=1
        continue

    print(f"\033[0;31m{c}\033[m", end=" ")

print(f"\nO número {numero} foi divisivel {cont} vezes")
if cont == 2:
    print("E por isso esse número é primo")
else:
    print("E por isso esse número não é primo")