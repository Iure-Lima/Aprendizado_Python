from time import sleep


def contador(i, f, p):

    if p < 0: p *= -1
    if p == 0: p = 1

    print("-=" * 18)
    print(f"  Contagem de {i} até {f} de {p} em {p}")
    print("-=" * 18)

    if i < f:
        cont = i
        while cont <= f:
            print(cont, end=" ")
            sleep(0.5)
            cont += p
    else:
        cont = i
        while cont >= f:
            print(cont, end=" ")
            sleep(0.5)
            cont -= p
    print("Fim!")


contador(1, 10, 1)
contador(10, 0, 2)
print("Agora personalize a contagem")
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)
