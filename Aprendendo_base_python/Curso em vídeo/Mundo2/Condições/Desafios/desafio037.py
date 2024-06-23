numeroBase = int(input("Digite algum número inteiro: "))

print("""
Escolha uma das opções abaixo:
[ 1 ] Converter para BINÁRIO 
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL 
""")

opcaoEscolhida = int(input("Qual sua escolha: "))
valorConvetido = 0

if opcaoEscolhida == 1:
    valorConvetido = bin(numeroBase)
    print(f"O valor {numeroBase} convertido para BINÁRIO fica {valorConvetido[2:]}")
elif opcaoEscolhida == 2:
    valorConvetido = oct(numeroBase)
    print(f"O valor {numeroBase} convertido para OCTAL fica {valorConvetido[2:]}")
elif opcaoEscolhida == 3:
    valorConvetido = hex(numeroBase)
    print(f"O valor {numeroBase} convertido para HEXADECIMAL fica {valorConvetido[2:]}")
else:
    print("Opção escolhida invalida")