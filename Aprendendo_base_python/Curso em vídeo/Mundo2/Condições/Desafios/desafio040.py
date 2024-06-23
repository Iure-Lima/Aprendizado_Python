primeiraNota = float(input("Primeira nota: "))
segundaNota = float(input("Segunda nota: "))

media = (primeiraNota + segundaNota) / 2

if media < 5:
    print(f"Sua média é {media:.1f}, REPROVADO")
elif media >= 7:
    print(f"Sua média é {media:.1f}, APROVADO COM HONRA")
elif media > 5:
    print(f"Sua média é {media:.1f}, APROVADO")
else:
    print(f"Sua média é {media:.1f}, PASSOU POR POUCO")