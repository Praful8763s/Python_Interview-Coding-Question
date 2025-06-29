from collections import Counter
def unique_elements(data):
    freq = Counter(data)
    for item in data:
        if freq[item]==1:
            return item
    return None
s = "programming"
print(unique_elements(s))  # Output: 'r'