teste = list()
galera = list()

teste.append("Iure")
teste.append(20)
galera.append(teste.copy())

galera2 = [["Lima", 34],["Lino",23],["Bui",60],["Sorocaba",32]]
for pessoa in galera2:
    #print(pessoa)
    pass

pessoas = list()
dados = list()

for i in range(0,3):
    dados.append(input("Qual seu nome: "))
    dados.append(int(input("Qual sua idade: ")))
    pessoas.append(dados[:])
    dados.clear()
print(pessoas)