print("="*20)
print("BANCO CEV")
print("="*20)
dinheiroASacar = int(input("Quanto você quer sacar? R$"))
cedula = 50
totalCedula = 0
while True:
    if dinheiroASacar >= cedula:
        dinheiroASacar -= cedula
        totalCedula+=1
    else:
        if totalCedula != 0: print(f"Total de {totalCedula} cédulas de R${cedula}")
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1

        totalCedula = 0
        if dinheiroASacar == 0:
            break
print("="*30)
print("Volte sempre ao BANCO CEV")