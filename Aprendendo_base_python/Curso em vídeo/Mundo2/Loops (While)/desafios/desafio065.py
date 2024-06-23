totalNumeros = media = maiorValor = menorValor = 0
opcao = 's'
while opcao == "s":
    numero = int(input("Digite um número: "))
    totalNumeros+= 1
    media+= numero

    if totalNumeros == 1:
        menorValor = numero
        maiorValor = numero

    if numero < menorValor: menorValor = numero
    if numero > maiorValor: maiorValor = numero

    opcao = input("Deseja continuar? [S/N] ").strip().lower()

media = media/totalNumeros
print(f"Você digitou {totalNumeros} números e a média foi {media}")
print(f"O maior valor foi {maiorValor} e o menor valor foi {menorValor}")