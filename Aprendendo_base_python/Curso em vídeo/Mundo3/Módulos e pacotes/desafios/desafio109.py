import moedav1.moeda as mo

p = float(input("Digite um preço: R$"))
print(f"A metade de {mo.moeda(p)} do preço é R${mo.metadeMoeda(p,True)}")
print(f"A o dobro de {mo.moeda(p)} é R${mo.dobroMoeda(p, True)}")
print(f"Com o aumento de 10%, o valor de {mo.moeda(p)} fica por {mo.aumentarMoeda(p, 10, True)}")