fraseOriginal = input("Digite uma frase: ").strip().replace(" ", "").upper()
fraseInvertida = ""

for index in range(len(fraseOriginal) - 1, -1, -1):
    fraseInvertida += fraseOriginal[index]
fraseInvertida.upper()
print(f"O inverso de de {fraseOriginal} é {fraseInvertida}")

if fraseOriginal == fraseInvertida:
    print("Temos um palíndro")
else:
    print("Não temos um palíndro")