from datetime import date
anoNascimento = int(input("Ano de Nascimento: "))
anoAtual = date.today().year
idade = anoAtual - anoNascimento

print(f"O atleta tem {idade} anos")

if 4 <= idade <= 9:
    print("Atleta da classe MIRIM")
elif 10 <= idade <= 14:
    print("Atleta da classe INFANTIL")
elif 15 <= idade <= 19:
    print("Atleta da classe JUNIOR")
elif 20 <= idade <= 25:
    print("Atleta da classe SÊNIOR")
elif idade > 25:
    print("Atleta da classe MASTER")
else:
    print("Não pode ser atleta")