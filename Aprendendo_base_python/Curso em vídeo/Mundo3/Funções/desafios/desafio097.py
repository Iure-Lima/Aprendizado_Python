def printMsg(msg):
    msgLen = len(msg) + 4
    print("~"*msgLen)
    print(f"{msg: ^{msgLen}}")
    print("~"*msgLen)


printMsg('Iure Lima')
printMsg('Curso de python no Youtube')
printMsg("CeV")