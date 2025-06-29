from collections import Counter
def functional_prog(str):
    strinter = Counter(str)
    for items in strinter:
     if strinter[items] > 1:
        return items
    return None
str = [2,1,4,3,2,4,9]
print(functional_prog(str))
