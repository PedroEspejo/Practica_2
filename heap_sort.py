def heapify(arr, n, i):
    largest = i  # Inicializa el nodo más grande como la raíz
    left = 2 * i + 1  # Índice del hijo izquierdo
    right = 2 * i + 2  # Índice del hijo derecho

    # Si el hijo izquierdo es más grande que la raíz
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Si el hijo derecho es más grande que el más grande hasta ahora
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Si el nodo más grande no es la raíz
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Intercambia el nodo raíz con el más grande
        heapify(arr, n, largest)  # Llama recursivamente a heapify en el subárbol afectado

def heap_sort(arr):
    n = len(arr)

    # Construye un montón máximo (heap) a partir de los elementos no ordenados
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extrae elementos uno por uno del montón
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Intercambia el primer elemento (raíz) con el último
        heapify(arr, i, 0)  # Llama a heapify en el montón reducido

# Ejemplo
arr = [64, 34, 25, 12, 22, 11, 90, 5, 73]
heap_sort(arr)
print("Lista ordenada mediante Heap Sort:", arr)