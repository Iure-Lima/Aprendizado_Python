from datetime import date


def vontar(anoNascimento):
    hoje = date.today()
    idade = hoje.year - int(anoNascimento)

    if idade < 16: return f"Com {idade} anos: NÂO VOTA"
    elif 16 <= idade < 18 or idade > 65: return f"Com {idade} anos: VOTO Opcional"
    elif idade > 18: return f"Com {idade} anos: VOTO Obrigátorio"


nas = int(input('Digite o ano de nascimento: '))
print(vontar(nas))
