def merged_list(list):
    merged_list = list[0]+list[1]
    for i in range(len(merged_list)):
        for j in range(i+1 , len(merged_list)):
            if merged_list[i] > merged_list[j]:
                merged_list[i], merged_list[j] = merged_list[j] , merged_list[i]
    return merged_list
list = [[1, 2, 3], [4, 5, 6]]
print(merged_list(list))