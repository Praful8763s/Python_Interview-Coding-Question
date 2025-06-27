# set = {3,1,4,2,4,6,8}
def sort_set(set):
 s = list(set)
 for i in range(len(set)):
    for j in range(i+1, len(set)):
        if set[i]>set[j]:
            set[i],set[j] = set[j], set[i]
 return set
sets = {3,1,4,2,4,6,8}
print(sort_set(sets))