expr = input("Digite a expressão: ")
pilha = []
for sim in expr:
    if sim == '(':
        pilha.append("(")
    elif sim == ")":
        if len(pilha) > 0:
            pilha.pop()
        else: pilha.append(")")
        break
if len(pilha) == 0:
    print("Expressão valida")
else:
    print("Expressão invalida")