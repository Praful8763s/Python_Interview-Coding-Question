from collections import Counter

def first_unique_element(data):
    # Count frequencies using Counter
    freq = Counter(data)
    
    # Loop through original order to find first unique
    for item in data:
        if freq[item] == 1:
            return item
    return None  # Return None if no unique element found
lst = [1, 2, 2, 3, 4, 3, 5]
print("First unique in list:", first_unique_element(lst))  
