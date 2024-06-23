string = 'Linha 1\nLinha 2\nLinha 3'
lines = string.splitlines()
multi = "\n".join(lines)


string2 = 'Linha 1\nLinha 2\nLinha 3'
lines2 = string.splitlines()
stringMu = ""
for line in lines2:
    stringMu = line
print(lines2[0])