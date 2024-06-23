import datetime

pessoa = {}

pessoa["Nome"] = str(input('Nome: ')).capitalize()
dataAtual = datetime.date.today().year
pessoa["Idade"] = dataAtual - int(input('Ano de Nascimento: '))
pessoa["Carteira de trabalho"] = int(input('Carteira de trabalho (0 não tem): '))

if pessoa["Carteira de trabalho"] != 0:
    pessoa["Ano de Contratação"] = int(input("Ano de contratação: "))
    pessoa["Salário"] = float(input("Salário: R$ "))



print("-="*20)
for k, v in pessoa.items():
    print(f"- {k} tem o valor {v}")