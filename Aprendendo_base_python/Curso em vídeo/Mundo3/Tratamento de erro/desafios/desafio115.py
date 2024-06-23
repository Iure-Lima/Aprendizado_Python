import programa.interface as inter
from time import sleep
import programa.arquivos as ar

#inter.cabecalho('SISTEMA DE ARQUIVO V1.0')
ar.criarArquivo("pessoas.txt")
while True:

    try:
        resposta = inter.menu(['Ver pessoas cadastradas', 'Cadastrar pessoas', 'Sair do sistema'])
        if resposta == 1:
            inter.cabecalho("Ver pessoas cadastradas")
            ar.lerArquivo("pessoas.txt")
        elif resposta == 2:
            inter.cabecalho("Cadastrar pessoas")
            nome = str(input("Nome: ")).strip()
            idade = int(input("Idade: "))
            ar.adicionarPessoa(nome, idade, "pessoas.txt")
        elif resposta == 3:
            inter.cabecalho("Saindo do sistema")
            break
        else:
            print("Fornceça uma opção valida")
        sleep(2)

    except KeyboardInterrupt:
        print("Programa interrompido")
        break
