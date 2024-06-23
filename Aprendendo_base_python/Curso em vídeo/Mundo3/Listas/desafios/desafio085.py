valores = [[],[]]

for i in range(0,7):
    valor = int(input(f'Digite o {i+1} um valor: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
print("-="*20)
print(f"Os valores pares digitados foram: {valores[0]}")
print(f"Os valores impares digitados foram: {valores[1]}")