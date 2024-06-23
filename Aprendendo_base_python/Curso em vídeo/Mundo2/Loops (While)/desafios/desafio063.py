print("Sequencia de Fibonacci")
print("-=" * 30)
totalTermos = int(input("Quantos termos você quer mostrar: "))
contTermos = 0
anterior = 0
atual = 1
proximoNumero = 1

while contTermos < totalTermos:
    print(f"{anterior} ", end = "-> ")
    proximoNumero = atual + anterior
    anterior = atual
    atual = proximoNumero
    contTermos+=1

print("FIM")