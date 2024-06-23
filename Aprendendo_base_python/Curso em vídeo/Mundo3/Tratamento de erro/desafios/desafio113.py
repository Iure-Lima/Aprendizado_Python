def leiaInt(msg):
    while True:
        try:
            numeroInteiro = int(input("Digite um número inteiro: "))
        except (ValueError, TypeError):
            print(f"[ERROR] Valor invalido")
        else:
            return numeroInteiro

def leiaFloat(msg):
    while True:
        try:
            numeroReal = float(input("Digite um número real: "))
        except (ValueError, TypeError):
            print(f"[ERROR] Valor invalido")
        else:
            return numeroReal


inteiro = leiaInt("Digite um número inteiro: ")
real = leiaFloat("Digite um valor real: ")
print(f"O valor Inteiro é {inteiro} e o valor Real é {real}")