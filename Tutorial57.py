from collections import Counter
def print_unique_elements(data):
    freq = Counter(data)
    print("Unique elements:")
    for item, count in freq.items():
        if count == 1:
            print(f"{item}")
text = "programming"
print("\nString:")

print_unique_elements(text)