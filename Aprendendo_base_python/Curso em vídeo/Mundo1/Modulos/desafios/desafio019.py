from random import randint
aluno1 = input("Primeiro aluno: ")
aluno2 = input("Segundo aluno: ")
aluno3 = input("Terceiro aluno: ")
aluno4 = input("Quarto aluno: ")
alunos = [aluno1,aluno2,aluno3,aluno4]
escolhido = randint(0,3)
print(f"O aluno escolhido foi {alunos[escolhido]}")