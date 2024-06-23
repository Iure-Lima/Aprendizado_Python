matrix = [[0,0,0],[0,0,0],[0,0,0]]
somaValoresPares = 0
somaValoresTerceiraColuna = 0
maiorValorSegundaLinha = 0

for i in range(0,3):
    for j in range(0,3):
        matrix[i][j] = int(input(f"Digite um valor para [{i},{j}]: "))
        if matrix[i][j] % 2 == 0: somaValoresPares+= matrix[i][j]
        if j == 2: somaValoresTerceiraColuna+= matrix[i][j]
        if i == 1:
            if maiorValorSegundaLinha <= matrix[i][j]:
                maiorValorSegundaLinha = matrix[i][j]


print("-="*20)
for i in range(0,3):
    for j in range(0,3):
        print(f"[{matrix[i][j]:^5}]", end=" ")
    print()
print("-="*20)
print(f"A soma dos valores pares é {somaValoresPares}")
print(f"A soma dos valores da terceira coluna é {somaValoresTerceiraColuna}")
print(f"O maior valor da segunda linha é {maiorValorSegundaLinha}")
