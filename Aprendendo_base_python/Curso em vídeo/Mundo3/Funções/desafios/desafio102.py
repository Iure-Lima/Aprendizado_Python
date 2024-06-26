def fatorial(n, show=False):
    """
    -> Calcula o fatorial
    :param n: O número a ser calculado
    :param show: (opcional) Mostra ou não a conta
    :return: O valor fatorial de um numero
    """
    resultado = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end="")
            if c > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
        resultado *= c

    return resultado


print(fatorial(5, True))
