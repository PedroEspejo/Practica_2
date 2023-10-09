def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # Elegir el pivote (generalmente se elige el elemento medio)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Ejemplo

arr = [64, 34, 25, 12, 22, 11, 90, 5, 73]
sorted_arr = quick_sort(arr)
print("Lista ordenada mediante Quick Sort:", sorted_arr)