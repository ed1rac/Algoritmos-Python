import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(1, 100, 500)
O_1 = np.ones_like(n)
O_n = n
O_n2 = n**2

plt.plot(n, O_1, label="O(1)")
plt.plot(n, O_n, label="O(n)")
plt.plot(n, O_n2, label="O(n^2)")

plt.title('Comparando Complexidade de Algoritmos')
plt.xlabel('Tamanho da Entrada (n)')
plt.ylabel('Custo Computacional')
plt.legend()
plt.show()