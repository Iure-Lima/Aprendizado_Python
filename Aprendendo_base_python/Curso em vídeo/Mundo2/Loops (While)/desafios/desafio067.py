
while True:
    numeroTabuada = int(input("Quer ver a tabuada de que valor: "))
    print("-" *40)

    if numeroTabuada < 0 : break

    for i in range(1,11):
        print(f"{numeroTabuada} X {i} = {numeroTabuada * i}")
    print("-" *40)
print("Programa de tabuada encerrado")