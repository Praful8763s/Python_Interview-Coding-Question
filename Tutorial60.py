from collections import Counter
def check_frequency(list):
    freg = Counter(list)
    for item in freg:
        if freg[item]==1:
            return item
    return None
s = "programming"
print(check_frequency(s))