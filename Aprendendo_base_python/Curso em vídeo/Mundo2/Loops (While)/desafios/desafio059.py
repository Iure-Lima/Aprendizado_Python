primeiroValor = int(input("Primeiro valor: "))
segundoValor = int(input("Segundo valor: "))

while True:
    print("""
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] novos núemro
    [ 5 ] sair do programa 
    """)

    escolha = int(input("Qual a sua opção? "))

    if escolha == 1:
        print(f"A soma de {primeiroValor} + {segundoValor} = {primeiroValor + segundoValor}")
    elif escolha == 2:
        print(f"A multiplicação de {primeiroValor} X {segundoValor} = {primeiroValor * segundoValor}")
    elif escolha == 3:
        maior = 0
        if primeiroValor > segundoValor: maior = primeiroValor
        elif segundoValor > primeiroValor: maior = segundoValor
        print(f"Entre {primeiroValor} e {segundoValor} o maior é {maior}")
    elif escolha == 4:
        print("Informe novos número: ")
        primeiroValor = int(input("Primeiro valor: "))
        segundoValor = int(input("Segundo valor: "))

    elif escolha == 5:
        print("Fechando o programa")
        break
    else:
        print("Opção invalida!")
        continue

    print("=-"*20)