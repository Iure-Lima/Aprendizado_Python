import matplotlib.pyplot as plt

#Dados da sessões
dados = [83, 51, 66, 61 ,82 ,65 ,54 ,56 ,92 ,60,
        65 ,87, 68 ,64 ,51 ,70 ,75 ,66 ,74 ,68,
        44, 55 ,78 ,69 ,98 ,67, 82, 77 ,79, 62,
        38 ,88 ,76 ,99 ,84 ,47 ,60, 42, 66, 74,
        91, 71 ,83, 80, 68, 65, 51, 56 ,73 ,55]

#Cria o histograma
plt.hist(dados, bins=10,color= "skyblue", edgecolor="black")

#Personalização (opcional)
plt.title("Histograma das sessões") #Define o titulo
plt.xlabel("Quantidade de sessões") #Define o label no eixo x
plt.ylabel("Frequência") #Define o label no eixo y
plt.grid(axis="y",linestyle="--", alpha=0.7) #Define as linhas do histograma

#Mostra o gráfico
plt.show()
