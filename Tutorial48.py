list = [2,4,1,2,3,0,9]
def reverse_sort(list):
 for i in range(len(list)):
    for j in range(i+1, len(list)):
        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]


 return list
list = [2,4,1,2,3,0,9]
reverse_sorted_list = reverse_sort(list)
print("Reversed sorted list:", reverse_sorted_list) 
