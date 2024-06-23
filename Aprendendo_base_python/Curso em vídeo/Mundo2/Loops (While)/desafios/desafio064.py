soma = 0
totalNumber = 0

while True:
    number = int(input("Digite um número [999 para parar]: "))
    if number != 999:
        soma += number
        totalNumber +=1
    else: break
print(f"Você digitou {totalNumber} número e sua soma é {soma}")