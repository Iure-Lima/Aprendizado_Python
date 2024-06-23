import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br') #Abre a url
    print(site.read())
except urllib.error.URLError:
    print("Não podemos abrir o site no momento")
else:
    print("Site funcionando perfeitamente")
