import moedav1.moeda as mo

p = float(input("Digite um preço: R$"))
print(f"A metade do preço é R${mo.metadeMoeda(p)}")
print(f"A o dobro é R${mo.dobroMoeda(p)}")
print(f"Com o aumento de 10%, o valor é {mo.aumentarMoeda(p, 10)}")