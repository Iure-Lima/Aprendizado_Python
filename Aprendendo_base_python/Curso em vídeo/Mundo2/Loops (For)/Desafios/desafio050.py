soma = 0
for i in range(0 , 6):
    numero = int(input(f"Digite um número {i + 1}# "))
    if numero % 2 == 0:
        soma+= numero

print(f"A soma de todos os número pares é {soma}")