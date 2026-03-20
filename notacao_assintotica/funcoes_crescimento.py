import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(1, 300, 400)

# Funções de crescimento
o_1 = np.ones_like(n)*5
o_log_n = np.log(n)*10
o_n = n
o_n_log_n = n * 0.55 * np.log(n)
o_n_squared = n ** 1.3
o_2_pow_n = 1.85 ** (n / 5)  # Ajustando para melhor visualização

plt.figure(figsize=(12, 7))  # Largura de 12 polegadas e altura de 6 polegadas

# Plotando as funções com ajustes para melhor visualização
plt.plot(n, o_1, label=r"$O(1)$", linewidth=2)
plt.plot(n, o_log_n, label=r"$O(\log n)$", linewidth=2)
plt.plot(n, o_n, label=r"$O(n)$", linewidth=2)
plt.plot(n, o_n_log_n, label=r"$O(n \log n)$", linewidth=2)
plt.plot(n, o_n_squared, label=r"$O(n^2)$", linewidth=2)
plt.plot(n, o_2_pow_n, label=r"$O(2^n)$", linewidth=2)

# Ajustando os limites do eixo Y
plt.ylim(0, 500)
plt.xlim(0, 300)

# Adicionando título e rótulos
plt.xlabel("Tamanho da Entrada (n)")
plt.ylabel("Crescimento")
plt.title("Comparação das Funções de Crescimento")

# Colocando a legenda no lado direito, dentro do gráfico
plt.legend(loc='upper left', bbox_to_anchor=(1.02, 1), frameon=True, edgecolor='black', fontsize='small', borderpad=1,
           handlelength=2)
plt.grid(True)

# Ajuste para evitar corte da legenda
plt.subplots_adjust(right=0.85)

plt.show()
