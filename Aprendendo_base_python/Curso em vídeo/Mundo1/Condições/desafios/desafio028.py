from random import randint
from time import sleep

print("-="*30)
print("Vou pensar em um número entre 0 e 5. Tente Adivinhar")
print("-="*30)

numero = int(input(("Digite um número entre 0 e 5: ")))
print("PROCESSANDO...")
sleep(1)

numeroComputador = randint(0,5)

if numero == numeroComputador:
    print(f"Você ganhou, consegui acerta o número que pensei")
else:
    print(f"Ganhei! Eu pensei no número {numeroComputador} e não no {numero}!")