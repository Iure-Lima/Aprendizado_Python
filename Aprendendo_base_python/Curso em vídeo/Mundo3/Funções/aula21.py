def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: Início da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: Sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print("FIM")

contador(2,10,2)
help(contador)

def soma(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = soma(2,3,4)
r2 = soma(4,5,)
r3 = soma(c=7,b=9)
print(r1, r2, r3)