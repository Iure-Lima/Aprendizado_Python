peso = float(input("Qual o seu peso? (KG) "))
altura = float(input("Qual a sua altura? (M) "))
imc = peso / (altura * altura)

print(f"O IMC dessa pessoa é {imc:.2f}")

if imc < 18.5:
    print("Você esta abaixo do peso")
elif 18.5 <= imc < 25:
    print("Parabéns, você esta com o peso ideal")
elif 25 <= imc < 30:
    print("Você esta com Sobrepeso")
elif 30 <= imc <= 40:
    print("Você esta com Obesidade")
elif imc > 40:
    print("Você esta com Obesidade Mórbida")
