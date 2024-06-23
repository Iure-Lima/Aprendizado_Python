import matplotlib.pyplot as plt

#Dados
categorias = ["Amarelo", "Verde","Roxo","Azul"] #Define as categorias
frequencia = [12, 8, 22, 16] #Define a frequencia das categorias

#Define as cores da barra (Tem que ser em inglês)
cores = ["yellow", "green", "purple","blue"]

#Criação dos grafico de barras
plt.bar(categorias,frequencia,color=cores) #Cria o grafico

#Personalização do grafico (Opcional)
plt.title("Gráfico de barras para as vendas de lenço") #Define o titulo
plt.xlabel("Cor") #Define o label no eixo x
plt.ylabel("Quantidade") #Define o label no eixo y
plt.grid(axis="y",linestyle="--", alpha=0.7) #Define as linhas do gráfico

#Mostra o gráfico
plt.show()
