times = ("Athletico-PR","Cruzeiro","Flamengo","Fortaleza","Vasco","Internacional","Palmeiras","Bahia",
         "Bragantino","Criciúma","Juventude","Atlético-MG","Corinthians","Fluminense","Botafogo","Grêmio",
         "São Paulo", "Atlético-GO","Vitória","Cuiabá")
print("-="*15)
print("Lista de times do Brasileirão: ", times)
print("-="*15)
print("Os cincos primeiros são: ", times[0:5])
print("-="*15)
print("Os 4 últimos são: ", times[-4:])
print("-="*15)
print("Time em ordem alfabetica: ", sorted(times))
print("-="*15)
print(f"O Fluminense está na {times.index('Fluminense') + 1} posição")


