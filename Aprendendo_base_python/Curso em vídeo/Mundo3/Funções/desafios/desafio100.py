from random import randint


def radomNumber(lista,number=5):
    print(f"Sorteando {number} valores da lista: ", end="")
    for i in range(0, number):
        numberRadom = randint(1, 10)
        print(f'{numberRadom}', end=" ")
        listaNumeros.append(numberRadom)
    print("PRONTO!")


def somaPares(lista):
    print(f"Somando os valores pares de {listaNumeros}, temos ", end="")
    somaParesResult = 0
    for number in listaNumeros:
        if number % 2 == 0:
            somaParesResult += number
    print(somaParesResult)


listaNumeros = list()
radomNumber(lista=listaNumeros)
somaPares(listaNumeros)
