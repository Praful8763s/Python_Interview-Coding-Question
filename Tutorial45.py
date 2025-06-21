def quick_sort_loop(arr):
    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()
        if low < high:
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            i += 1
            arr[i], arr[high] = arr[high], arr[i]  # pivot at right place

            # Push subarrays to sort
            stack.append((low, i - 1))
            stack.append((i + 1, high))


# === Test Quick Sort with Loop ===
arr = [10, 7, 8, 9, 1, 5]
quick_sort_loop(arr)
print("Sorted array:", arr)
