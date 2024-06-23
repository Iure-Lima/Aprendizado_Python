def dobroMoeda(valor = 0, formatado = False):
    resultado = valor * 2
    return resultado if not formatado else moeda(resultado)


def metadeMoeda(valor = 0, formatado = False):
    resultado = valor / 2
    return resultado if not formatado else moeda(resultado)


def aumentarMoeda(valor = 0, taxa = 0, formatado = False):
    valorCalc = valor + (valor * taxa/100)
    return valorCalc if not formatado else moeda(valorCalc)


def diminuirMoeda(valor = 0, taxa = 0,formatado = False):
    valorCalc = valor - (valor * taxa / 100)
    return valorCalc if not formatado else moeda(valorCalc)


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')


def resumo(preco, aumento = 0, reducao = 0):
    print("-"*30)
    print(f"{'RESUMO DO VALOR':^30}")
    print("-"*30)

    print(f"Preço analisado: {moeda(preco)}")
    print(f"Dobro do preço: {dobroMoeda(preco, True)}")
    print(f"Metade do preço: {metadeMoeda(preco, True)}")

    if aumento != 0: print(f"{aumento}% de aumento: {aumentarMoeda(preco, aumento, True)}")
    if reducao != 0: print(f"{reducao}% de redução: {diminuirMoeda(preco, reducao, True)}")
    print("-" * 30)
