def notas(*n, sit=False):
    dic = {"Total": len(n), "Maior": max(n), "Menor": min(n), "Média": sum(n) / len(n)}
    if sit:
        media = dic["Média"]
        situacao = ""
        if media <= 5:
            situacao = "Lastimavel"
        elif media < 7:
            situacao = "Ruim"
        elif media < 9:
            situacao = "Boa"
        elif media > 9:
            situacao = "Excelente"
        dic["Situação"] = situacao
    return dic


res = notas(5.5, 6.2, 2.6, sit=True)
print(res)
