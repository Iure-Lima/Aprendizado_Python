print("Gerador de PA")
print("-="*20)
primeiroTermo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = 9 * razao + primeiroTermo
controler = primeiroTermo

while True:
    if controler > decimo: break
    print(f"{controler} ->", end=" ")
    controler += razao

print("FIM")