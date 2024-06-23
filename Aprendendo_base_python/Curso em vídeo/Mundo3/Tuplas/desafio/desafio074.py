from random import randint
valorSorteados = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
maiorValor = max(valorSorteados)
menorValor = min(valorSorteados)

print("Os valores sorteados são: ", end="")
for number in valorSorteados:
    print(number,end=" ")
print(f"\nO maior valor é {maiorValor}")
print(f"O menor valor é {menorValor}")