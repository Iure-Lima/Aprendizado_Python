somatorio = 0
cont = 0

for i in range(1, 501, 2):
    if i % 3 == 0:
        cont+=1
        somatorio += i
print(f"A soma dos {cont} valores solicitados é {somatorio}")