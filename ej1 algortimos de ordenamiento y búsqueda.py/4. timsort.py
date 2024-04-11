#Timsort es un algoritmo de ordenamiento híbrido que combina el algoritmo de ordenamiento por inserción y el algoritmo de ordenamiento por mezcla. Fue diseñado para aprovechar las ventajas de ambos algoritmos y mejorar el rendimiento en una amplia gama de situaciones. 
#El funcionamiento de Timsort se basa en dividir la lista en pequeños bloques llamados "runs" y luego combinarlos en orden. Primero, se identifican los runs ascendentes y descendentes en la lista. Luego, estos runs se fusionan utilizando el algoritmo de ordenamiento por mezcla, asegurando que los elementos se coloquen en el orden correcto. Finalmente, se realiza una fase de inserción para garantizar que la lista esté completamente ordenada.
#La principal ventaja de Timsort es su capacidad para manejar eficientemente diferentes tipos de datos y casos de entrada, como listas parcialmente ordenadas o listas con elementos repetidos. Además, Timsort tiene un buen rendimiento en el peor de los casos, lo que lo hace adecuado para aplicaciones en tiempo real.
#En cuanto a su orden de complejidad, Timsort tiene una complejidad promedio y peor caso de O(n log n), donde "n" es el tamaño de la lista a ordenar. Sin embargo, en el mejor caso, cuando la lista ya está ordenada, Timsort tiene una complejidad lineal de O(n). Esto lo convierte en uno de los algoritmos de ordenamiento más eficientes en la mayoría de los casos.

def timsort(arr):
    # Divide the array into small runs
    min_run = 32
    n = len(arr)
    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run - 1), n - 1))
    
    # Merge the runs using merge sort
    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            mid = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))
            merge(arr, start, mid, end)
        size *= 2
    
    return arr

def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, start, mid, end):
    left = arr[start:mid + 1]
    right = arr[mid + 1:end + 1]
    i = j = 0
    k = start
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

# Example usage
arr = [5, 2, 8, 1, 9, 3]
sorted_arr = timsort(arr)
print(sorted_arr)
