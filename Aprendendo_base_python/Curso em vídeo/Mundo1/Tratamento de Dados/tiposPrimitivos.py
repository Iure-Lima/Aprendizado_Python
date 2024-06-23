inteiro = int("6") #Converte uma String para inteiro
real = float("6.3") #Converte uma String para um número real
logico = bool("True") #Converte uma String para um valor logico
string = str(5) #Converte um número para um valor string

print(inteiro)
print(real)
print(logico)
print(string)

#Nova forma de print

print(f"hello {inteiro}")

#métodos is

n = "05439"
print(n.isnumeric()) #Retorna True

n = "www"
print(n.isalpha()) #Retorna True

n = "www2"
print(n.isalnum()) #Retorna True

n = "WWW"
print(n.isupper()) #Retorna True

n = "www"
print(n.islower()) #Retorna True

n = "ww#$w"
print(n.isascii()) #Retorna True

n = "Olá"
print(n.istitle()) #Retorna True

n = "    "
print(n.isspace()) #Retorna True

n = "115220"
print(n.isdecimal()) #Retorna True

n = "nome"
print(n.isidentifier()) #Retorna True

n = "no#e3me"
print(n.isprintable()) #Retorna True

n = "125"
print(n.isdigit()) #Retorna True