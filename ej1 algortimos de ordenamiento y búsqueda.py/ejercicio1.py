import random
import time

def bucket_sort(arr):
    # Implementación del algoritmo bucket sort
    pass

def shell_sort(arr):
    # Implementación del algoritmo shell sort
    pass

def radix_sort(arr):
    # Implementación del algoritmo radix sort
    pass

# Generar listas aleatorias de diferentes tamaños
sizes = [100000, 1000000, 10000000]
lists = []

for size in sizes:
    random_list = [random.randint(0, 1000000) for _ in range(size)]
    lists.append(random_list)

# Aplicar los algoritmos de ordenamiento y medir el tiempo de ejecución
for i, lst in enumerate(lists):
    print(f"Lista de tamaño {sizes[i]}:")
    
    start_time = time.time()
    bucket_sort(lst)
    end_time = time.time()
    print(f"Tiempo de ejecución de bucket sort: {end_time - start_time} segundos")
    
    start_time = time.time()
    shell_sort(lst)
    end_time = time.time()
    print(f"Tiempo de ejecución de shell sort: {end_time - start_time} segundos")
    
    start_time = time.time()
    radix_sort(lst)
    end_time = time.time()
    print(f"Tiempo de ejecución de radix sort: {end_time - start_time} segundos")

