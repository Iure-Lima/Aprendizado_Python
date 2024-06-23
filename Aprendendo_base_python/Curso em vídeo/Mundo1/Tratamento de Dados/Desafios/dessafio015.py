dias = int(input("Quantos dias alugado? "))
kmRodados = float(input("Quantos KM rodados? "))
total = (60 * dias) + (0.15*kmRodados)

print(f"O valor a pagra é de R${total:.2f}")