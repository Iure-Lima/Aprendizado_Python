salario = float(input("Qual o sálario do funcionario? R$"))
aumento = salario + (salario*(15/100))
print(f"Um funcionário que ganhava R${salario:.2f}, com 15% de aumento, passa a receber R${aumento:.2f}")