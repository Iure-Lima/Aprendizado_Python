from time import sleep


def maiorValor(*nuns):
    if len(nuns) == 0: maxNum = 0
    else: maxNum = max(nuns)

    print("-=" * 20)
    print("Analisando os valores passados")
    for num in nuns:
        print(f'{num} ', end='')
        sleep(0.3)
    print(f"Foram informado {len(nuns)} valores ao todo")
    print(f"O maior valor informado foi {maxNum}")


maiorValor(2, 9, 4, 5, 7, 1)
maiorValor(4, 7, 0)
maiorValor(1, 2)
maiorValor(6)
maiorValor()
