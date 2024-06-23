print("="*20)
print("10 Termos de uma PA")
print("="*20)

primeiroTermo = int(input("Primeiro Termo: "))
razao = int(input("Razão: "))

for c in range(primeiroTermo, razao * 10 + primeiroTermo, razao):
    print(f"{c} -> ", end="")
print("ACABOU")