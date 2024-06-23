import matplotlib.pyplot as plt
import numpy as np

#Dadps
data = [np.random.randn(50) for _ in range(5)]

plt.boxplot(data) #Define o gráfico
plt.xlabel('Grupos') #Define o eixo x
plt.ylabel('Valores') #Define o eixo x
plt.title('Box Plot') #Define o titulo
plt.show() #Mostra o gráfico
