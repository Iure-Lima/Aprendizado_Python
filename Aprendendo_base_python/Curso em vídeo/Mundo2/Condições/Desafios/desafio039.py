import datetime as dt
anoNascimento = int(input("Digite seu ano de nascimento: "))
anoAtual = dt.date.today().year
idade = anoAtual - anoNascimento

print(f"Vocẽ nasceu em {anoNascimento} tem {idade} anos em {anoAtual}")
if idade < 18:
    anosFaltante = 18 - idade
    print(f"Ainda falta {anosFaltante} anos para o alistamento")
    print(f"Seu alistamento será em {anoAtual + anosFaltante}")
elif idade > 18:
    anosPassados = idade - 18
    print(f"Você já deveriá ter se alistado há {anosPassados} anos")
    print(f"Seu alistamento foi em {anoAtual - anosPassados}")
else:
    print("Você se alista esse ano")