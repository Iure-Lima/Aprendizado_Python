maiorDeIdade = homensCadastrados = mulheresComMenosDe20 = 0
while True:
    print("-" * 20)
    print("CADASTRE UMA PESSOA")
    print("-" * 20)
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().lower()

    if idade > 18: maiorDeIdade += 1
    if sexo == "m": homensCadastrados+=1
    if sexo == "f" and idade < 20: mulheresComMenosDe20 += 1

    print("-" * 20)
    continuar = input("Dejesa continuar [S/N}: ").strip().lower()
    if continuar == "n": break

print(f"Total de pessoas com mais de 18 anos: {maiorDeIdade}")
print(f"Ao todo temos {homensCadastrados} homens cadastrados")
print(f"Temos {mulheresComMenosDe20} mulheres com menos de 20 anos")