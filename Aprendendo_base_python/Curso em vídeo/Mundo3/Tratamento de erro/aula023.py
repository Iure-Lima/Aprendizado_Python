try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except ZeroDivisionError as erro:
    print(f"Divisão por zero não pode acontecer")
except (ValueError, TypeError) as erro:
    print("Você forneceu dados invalidos")
except Exception as erro:
    print(f"Ocorreu um erro {erro.__class__}")
else: print(f'O resultado é {r:.1f}')
finally: print("Programa Finalizado")