pessoa = {}

pessoa["nome"] = input('Nome: ')
pessoa["média"] = float(input("Média: "))
if pessoa["média"] >= 7:
    pessoa["situação"] = "Aprovado"
elif 5 <= pessoa["média"] < 7:
    pessoa["situação"] = "Recuperação"
else:
    pessoa["situação"] = "Reprovado"

print("-="*20)
for k, v in pessoa.items():
    print(f"- {k} é igual a {v}")