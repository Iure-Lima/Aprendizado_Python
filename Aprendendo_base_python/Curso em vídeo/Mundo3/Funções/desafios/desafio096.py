def areaTerreno(largura, comprimento):
    area = largura * comprimento
    print(f"A área de um terreno {largura:.1f} x {comprimento:.1f} é de {area}m²")


print("Controle de terrenos")
print("-"*20)
largura = float(input("Largura: "))
comprimento = float(input("Comprimento: "))
areaTerreno(largura, comprimento)