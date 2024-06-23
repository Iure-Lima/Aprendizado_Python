salario = float(input("Qual é o salário do funcionário? R$"))
newSalario = 0
if salario <= 1250:
    newSalario = salario + (salario*(15/100))
else:
    newSalario = salario + (salario * (10/ 100))


print(f"Quem ganhava R${salario:.2f} passa a ganhar R${newSalario:.2f} agora")