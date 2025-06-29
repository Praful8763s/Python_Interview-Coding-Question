from collections import Counter



def print_unique_elements(data):
    freq = Counter(data)
    print("Unique elements:")
    for item, count in freq.items():
        if count == 1:
            print(f"{item}")

# ---------- For Array ----------
arr = [1, 2, 2, 3, 4, 4, 5, 6, 6]
print("Array:")

print_unique_elements(arr)

