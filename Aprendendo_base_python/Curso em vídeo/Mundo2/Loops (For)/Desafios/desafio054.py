from datetime import date
now = date.today().year

contMenor = 0
contMaior = 0

for c in range(0,7):
    anoNascimento = int(input(f"Em que ano a {c + 1} pessoa nasceu? "))
    idade = now - anoNascimento

    if idade >= 18:
        contMaior += 1
    else:
        contMenor += 1

print(f"Ao todo tivemos {contMaior} pessoas maiores de idade.")
print(f"E também tivemos {contMenor} pessoas menores de idade.")
