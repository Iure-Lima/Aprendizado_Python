import matplotlib.pyplot as plt

#Dados
horas_de_estudo = [2,3,5,1,6,4,7,8,9,10]
notas_finais = [60,65,75,50,80,70,85,90,95,100]


#Criação dos grafico de dispersao
plt.scatter(horas_de_estudo,notas_finais,color="blue", label="Estudantes") #Cria o grafico

#Personalização do grafico (Opcional)
plt.title("Gráfico de dispersão: Horas de Estudo vs Notas Finais") #Define o titulo
plt.xlabel("Horas de Estudos") #Define o label no eixo x
plt.ylabel("Notas Finais") #Define o label no eixo y
plt.legend() #Define que teremos uma legenda
plt.grid(True) #Define as linhas de grid

#Mostra o gráfico
plt.show()
