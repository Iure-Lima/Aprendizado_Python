numero = int(input("Digite um número para calcular o fatorial: "))
valorFinal = 1
print(f"Calculando {numero}! = ", end="")
while numero != 0:
    valorFinal *= numero
    if numero != 1: print(f"{numero} X ", end="")
    else: print(f"{numero}", end="")
    numero-=1
print(f" = {valorFinal}")