def linha(tamanho = 30):
    print('-' * tamanho)


def cabecalho(msg):
    linha()
    print(msg.center(30))
    linha()


def leiaInt(msg):
    while True:
        try:
            numeroInteiro = int(input("Digite um número inteiro: "))
        except (ValueError, TypeError):
            print(f"[ERROR] Forneca uma número inteiro valido")
        else:
            return numeroInteiro


def menu(lista):
    cabecalho("MENU PRINCIPAL")
    for index, item in enumerate(lista):
        print(f"{index+1} - {item}")
    linha()
    opc = leiaInt("Sua opção: ")
    return opc