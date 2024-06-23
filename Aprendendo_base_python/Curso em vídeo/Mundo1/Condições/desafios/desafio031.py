distanciaViagem = int(input("Qual a distancia da viagem em KM: "))
preco = 0

if distanciaViagem > 200:
    preco = distanciaViagem*0.45
else:
    preco = distanciaViagem*0.50

print(f"Você está preste a começar uma viagem de {distanciaViagem:.1f}Km")
print(f"E o preço da sua passagem será de R${preco:.2f}")