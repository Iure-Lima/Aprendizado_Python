valorCasa = float(input("Qual o valor da casa? R$"))
salarioComprador = float(input("Quanto é o seu sálario? R$"))
anosDeFinanciamento = int(input("Quantos anos de financiamento?"))

prestacao = valorCasa / (anosDeFinanciamento * 12)
minimo = salarioComprador * 0.3

print(f"Uma casa no valor de R${valorCasa} para ser pago em {anosDeFinanciamento} anos fica R${prestacao:.2f} por mês")

if prestacao >= minimo:
    print("\nA parcela exece 30% do sálario, EMPRESTIMO NEGADO!")
elif prestacao <= minimo:
    print("\nEMPRESTIMO APROVADO!")
else:
    print("Algo de errado não esta certo")