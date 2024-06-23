alunos = []

while True:
    aluno = []
    notas = []
    aluno.append(str(input('Nome: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    aluno.append(notas[:])
    alunos.append(aluno[:])

    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'N': break

print("-="*20)
print("No.  NOME      MÉDIA")
print("-"*20)
for index, aluno in enumerate(alunos):
    print(f"{index}     {aluno[0]}      {((aluno[1][0] + aluno[1][0]) / 2):.2f}")
print("-"*20)
print("-="*20)
while True:
    opc = int(input("Mostrar notas de qual aluno? (999 para interromper) "))
    if opc == 999: break
    if opc > len(alunos) - 1:
        print("Opção invalida")
        continue
    print(f"Notas de {alunos[opc][0]} são {alunos[opc][1]}")
    print("-" * 30)