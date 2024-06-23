def leiaNumero(msg = "Digite um número: "):
    num = 0
    ok = False
    while not ok:
        valor = input(msg)
        if valor.isnumeric():
            num = int(valor)
            ok = True
        else: print("Erro! Digite um número válido.")
    return num


n = leiaNumero("Digite um número: ")
print(f"Você acabou de digitar o valor {n}")