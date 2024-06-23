itens = (("Lápis", 1.75), ("Borracha", 2),("Caderno", 15.9),("Estojo", 25),("Transferidor", 4.2),("Compasso", 9.99),
         ("Mochila", 120.32),("Canetas", 22.3),("Livro", 34.))

print("-"*30)
print(f"{'Listagem de preços':^30}")
print("-"*30)

for tupla in itens:
    print(f"{tupla[0]:.<20}{'.'*15}R$ {tupla[1]:.2f}")