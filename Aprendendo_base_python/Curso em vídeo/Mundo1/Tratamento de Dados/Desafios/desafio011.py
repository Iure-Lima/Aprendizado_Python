largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))
area = largura * altura
tinta = area / 2
print(f"Sua parede tem a dimensão de {largura}x{altura} e sua área é de {area:.3f}m².")
print(f"Para pinta essa parede, você precisará de {tinta}l de tinta.")