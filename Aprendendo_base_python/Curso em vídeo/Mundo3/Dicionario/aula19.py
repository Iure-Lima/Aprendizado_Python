pessoa = {"nome":"Iure","sexo":"M","idade":20}
#print(pessoa["idade"])
for k,v in pessoa.items():
    #print(f"{k} = {v}")
    pass

brasil = []
estado1 = {'uf':'Rio de Janeiro','sigla':'RJ'}
estado2 = {'uf':'São Paulo','sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0])
print(brasil[0]["uf"])
print(brasil[0]["sigla"])
print(brasil[1])