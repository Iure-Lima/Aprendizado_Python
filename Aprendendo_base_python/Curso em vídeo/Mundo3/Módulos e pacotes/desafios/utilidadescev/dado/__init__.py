def leiaDinheiro(msg):
    while True:
        valor = input(msg).replace(',', '.').strip()
        if not valor.isalpha() and valor != "": return float(valor)

        print(f'\033[31mERRO: "{valor}" é um preço invalido!\033[m')