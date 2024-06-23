from time import sleep


def pyHelp(func=""):
    funcao = func.lower().strip()
    titulo(f"Acessando Manual do comando '{funcao}'", 2)
    if func != "":
        print(cores[3])
        help(func)
        print(cores[0])
        sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end="")
    print("~" * tam)
    print(f"  {msg}  ")
    print("~" * tam)
    print(cores[0], end="")
    sleep(1)


cores = ("\033[m"  #Clear
         , "\033[42m"  #Verde
         , "\033[44m"  #Azul
         , "\033[7;40m"  #branco
         )

while True:
    titulo("SISTEMA DE AJUDA PyHELP", 1)
    func = str(input("Função ou Biblioteca > "))

    if func.upper() == "FIM": break
    pyHelp(func)
titulo("ATÉ LOGO", 1)
