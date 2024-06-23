import matplotlib.pyplot as plt

#Dados
categorias = ["Amarelo", "Verde","Roxo","Azul"] #Define as categorias
frequencia = [12, 8, 22, 16] #Define a frequencia das categorias

#Define as cores da barra (Tem que ser em inglês)
cores = ["yellow", "green", "purple","blue"]

#Criação dos grafico de pizza
plt.pie(frequencia, labels=categorias,autopct="%1.1f%%",startangle=90,colors=cores) #Cria o grafico

#Personalização do grafico (Opcional)
plt.title("Gráfico de pizza para as vendas de lenço") #Define o titulo

#Mostra o gráfico
plt.show()
