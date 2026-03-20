import numpy as np
import matplotlib.pyplot as plt
import time

# Funções de ordenação

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Função para medir o tempo de execução
def time_sorting_algorithm(algorithm, array):
    start_time = time.time()
    algorithm(array)
    return time.time() - start_time

# Geração de dados e medição de tempos
sizes = [100, 500, 1000, 2000, 5000]
selection_times = []
quicksort_times = []
insertion_times = []
bubble_times = []

for size in sizes:
    data = np.random.randint(0, 10000, size)
    selection_times.append(time_sorting_algorithm(lambda arr: selection_sort(arr), data.copy()))
    quicksort_times.append(time_sorting_algorithm(lambda arr: quicksort(arr, 0, len(arr) - 1), data.copy()))
    insertion_times.append(time_sorting_algorithm(lambda arr: insertion_sort(arr), data.copy()))
    bubble_times.append(time_sorting_algorithm(lambda arr: bubble_sort(arr), data.copy()))

# Plotagem dos resultados
plt.figure(figsize=(12, 8))

plt.plot(sizes, selection_times, label='Selection Sort', marker='o')
plt.plot(sizes, quicksort_times, label='Quicksort', marker='o')
plt.plot(sizes, insertion_times, label='Insertion Sort', marker='o')
plt.plot(sizes, bubble_times, label='Bubble Sort', marker='o')

plt.yscale('log')
plt.xscale('log')

plt.xlabel('Tamanho do Array (log escala)')
plt.ylabel('Tempo de Execução (log escala)')
plt.title('Comparação de Algoritmos de Ordenação')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), borderpad=1)
plt.grid(True, which="both", ls="--", linewidth=0.5)
plt.tight_layout()
plt.show()
