def sorted_array(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
    return arr
       



arr = [3,4,2,1,5,6]
print(sorted_array(arr))
# Arrays.sort(a)
