def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Encuentra el punto medio de la lista
        left_half = arr[:mid]  # Divide la lista en dos mitades
        right_half = arr[mid:]

        merge_sort(left_half)  # Llamada recursiva para ordenar la mitad izquierda
        merge_sort(right_half)  # Llamada recursiva para ordenar la mitad derecha

        i = j = k = 0

        # Combina las dos mitades ordenadas en una lista ordenada
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copia los elementos restantes de left_half (si los hay)
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copia los elementos restantes de right_half (si los hay)
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Ejemplo
arr = [64, 34, 25, 12, 22, 11, 90, 5, 73]
merge_sort(arr)
print("Lista ordenada mediante Merge Sort:", arr)