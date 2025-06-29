from collections import Counter

def print_repeated_elements(data):
    freq = Counter(data)
    print("Repeated elements:")
    for item, count in freq.items():
        if count > 1:
            print(f"{item}: {count} times")


# ---------- For String ----------
text = "programming"
print("\nString:")
print_repeated_elements(text)
