sexo = input("Informe o sexo [M/F]: ").strip().lower()

while sexo not in 'mf':
    sexo = input("Dados Inválidos. Por favor, informe seu sexo novamente: ")
print(f"Sexo {sexo.upper()} registrado com sucesso.")