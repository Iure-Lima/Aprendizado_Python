print("Gerador de PA")
print("-="*20)
primeiroTermo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = razao * 9 + primeiroTermo
controler = primeiroTermo

while True:
    if controler > decimo:
        print("PAUSE")
        maisTermos = int(input("Mostrar mais quantos termos: "))
        if maisTermos == 0:
            break
        else:
            newDecimo = razao * maisTermos + controler
            while controler > newDecimo:
                print(f"{controler} ->", end=" ")
                controler += razao
            print("PAUSE")
    print(f"{controler} ->", end=" ")
    controler += razao

print("FIM")

