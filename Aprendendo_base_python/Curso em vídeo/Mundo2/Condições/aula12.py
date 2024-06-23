name = input("Digite o seu nome: ").lower()

if name == "iure":
    print("Seu nome é muito diferente")
elif name == "gustavo":
    print("Seu nome é legal")
elif name == "pedro" or name == "maria" or name == "paulo":
    print("Seu nome é bem popular no Brasil")
elif name in "luana bruna elisa":
    print("Belo nome feminino")
else:
    print("Seu nome é bem comum")

print(f"Tenha um bom dia {name}!")