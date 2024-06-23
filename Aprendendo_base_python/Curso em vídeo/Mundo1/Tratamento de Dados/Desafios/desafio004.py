valorUser = input("Digite algo aqui: ")

print("O tipo primitivo é String")
print(f"É um número inteiro: {valorUser.isnumeric()}")
print(f"É um número decimal: {valorUser.isdecimal()}")
print(f"É composto apenas por letras: {valorUser.isalpha()}")
print(f"É composto por letras ou número: {valorUser.isalnum()}")
print(f"É esta toda em minúsculo: {valorUser.islower()}")
print(f"É esta toda em mainúsculo: {valorUser.isupper()}")