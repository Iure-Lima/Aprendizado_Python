min = 0
max = 0

for i in range(0,5):
    peso = float(input(f"Peso da {i + 1} pessoa: "))

    if i == 0:
        min = peso
        max = peso
        continue

    if peso < min: min = peso
    if peso > max: max = peso

print(f"O maior peso foi de {max}KG")
print(f"O menor peso foi de {min}KG")