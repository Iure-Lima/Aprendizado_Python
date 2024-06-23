primeiroValor = int(input("Digite o primeiro valor: "))
segundoValor = int(input("Digite o segundo valor: "))
terceiroValor = int(input("Digite o terceiro valor: "))

menor = primeiroValor
maior = primeiroValor

if segundoValor < primeiroValor and segundoValor < terceiroValor:
    menor = segundoValor
if terceiroValor < primeiroValor and terceiroValor < segundoValor:
    menor = terceiroValor

if segundoValor > primeiroValor and segundoValor > terceiroValor:
    maior = segundoValor
if terceiroValor > primeiroValor and terceiroValor > segundoValor:
    maior = terceiroValor

print(f"O menor valor é {menor}")
print(f"O maior valor é {maior}")