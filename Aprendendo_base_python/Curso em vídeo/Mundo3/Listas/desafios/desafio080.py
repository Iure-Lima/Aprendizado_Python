lista = list()

for i in range(0,5):
    num = int(input("Digite um valor: "))
    if i == 0 or num > lista[-1]:
        lista.append(num)
        print("Adicionado ao final da lista.")
    else:
        pos = 0
        while True:
            if num <= lista[pos]:
                lista.insert(pos,num)
                print(f"Adicionado na posição {pos} da lista")
                break
            pos+=1

print(f"Os valores digitados foram: {lista}")