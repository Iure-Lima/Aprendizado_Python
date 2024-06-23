import os
from time import sleep


def criarArquivo(name = "arquivo.txt"):
    if not os.path.exists(f"programa/{name}"):
        try:
            arquivo = open(f"programa/{name}", "w")
            arquivo.close()
        except FileNotFoundError:
            print(f"O arquivo {name} não foi encontrado.")
        else:
            print(f"Arquivo {name} criado com sucesso")
    sleep(1)


def lerArquivo(name = "arquivo.txt"):
    try:
        with open(f"programa/{name}", "r") as arquivo:
            for line in arquivo.readlines():
                conteudo = line.replace("\n", "")
                valores = conteudo.split(";")
                print(f"{valores[0].strip().capitalize():<30} {valores[1].strip():>3} anos")
                sleep(0.5)
    except Exception:
        print("ERRO de leitura do arquivo, tente novamente mais tarde")


def adicionarPessoa(nome, idade, nomeArquivo = 'arquivo.txt'):
    try:
        with open(f"programa/{nomeArquivo}", "a") as arquivo:
            arquivo.write(f"{nome};{idade}\n")
    except Exception:
        print("ERRO de escrita do arquivo, tente novamente mais tarde")
    else:
        print(f"Novo registro de {nome} adicionado.")
