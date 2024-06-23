import matplotlib.pyplot as plt
import numpy as np

#Dados
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y) #cria o gráfico
plt.xlabel('Eixo X') #Define o eixo x
plt.ylabel('Eixo Y') #Define o eixo y
plt.title('Gráfico de Linha') #Mostra o titulo
plt.show() #Mostra o gŕafico