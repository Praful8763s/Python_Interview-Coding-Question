
# ------------------ 1. Create and Access Dictionary ------------------

print("\n1. Create and Access Dictionary")
person = {'name': 'Praful', 'age': 23, 'city': 'Indore'}
print("Name:", person['name'])  # Access value by key

# ------------------ 2. Add and Update Key-Value Pairs ------------------

print("\n2. Add and Update Key-Value")
person['profession'] = 'Engineer'
person['age'] = 24  # Update
print(person)

# ------------------ 3. Delete Key from Dictionary ------------------

print("\n3. Delete Key")
del person['city']
print(person)

# ------------------ 4. Loop Through Dictionary ------------------

print("\n4. Loop Through Dictionary")
for key, value in person.items():
    print(f"{key}: {value}")

# ------------------ 5. Check If Key Exists ------------------

print("\n5. Check Key Existence")
print("age" in person)
print("salary" in person)

# ------------------ 6. Count Frequency of Elements ------------------

print("\n6. Count Frequency of Elements")
data = ['a', 'b', 'a', 'c', 'b', 'a']
freq = {}
for char in data:
    freq[char] = freq.get(char, 0) + 1
print(freq)

# ------------------ 7. Merge Two Dictionaries ------------------

print("\n7. Merge Two Dictionaries")
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
merged = {**d1, **d2}
print(merged)

# ------------------ 8. Sort Dictionary by Keys and Values ------------------

print("\n8. Sort by Keys and Values")
d = {'banana': 3, 'apple': 4, 'cherry': 1}
print("Sorted by keys:", dict(sorted(d.items())))
print("Sorted by values:", dict(sorted(d.items(), key=lambda item: item[1])))

# ------------------ 9. Find Max and Min Key/Value ------------------

print("\n9. Max/Min Key and Value")
print("Max key:", max(d))
print("Min value:", min(d.values()))

# ------------------ 10. Convert Two Lists into Dictionary ------------------

print("\n10. Lists to Dictionary")
keys = ['id', 'name', 'age']
values = [101, 'Praful', 23]
converted = dict(zip(keys, values))
print(converted)

# ------------------ 11. Invert a Dictionary ------------------

print("\n11. Invert Dictionary")
original = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in original.items()}
print(inverted)

# ------------------ 12. Remove Duplicates from Dictionary Values ------------------

print("\n12. Remove Duplicate Values")
d_with_dupes = {'a': 1, 'b': 2, 'c': 1, 'd': 2}
unique_values = set()
unique_dict = {}
for k, v in d_with_dupes.items():
    if v not in unique_values:
        unique_values.add(v)
        unique_dict[k] = v
print(unique_dict)

# ------------------ 13. Nested Dictionary Access ------------------

print("\n13. Nested Dictionary Access")
student = {
    'name': 'Praful',
    'marks': {'math': 90, 'science': 95}
}
print("Math Marks:", student['marks']['math'])

# ------------------ 14. Dictionary Comprehension ------------------

print("\n14. Dictionary Comprehension")
squares = {x: x**2 for x in range(1, 6)}
print(squares)

# ------------------ 15. Find Common Keys in Two Dicts ------------------

print("\n15. Common Keys")
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 5, 'c': 6, 'd': 7}
common = dict1.keys() & dict2.keys()
print("Common keys:", common)

# ------------------ END OF FILE ------------------




### 📌 What You Learn from This File

# | Question Type                         | Covered |
# | ------------------------------------- | ------- |
# | Basic creation and access             | ✅       |
# | Update and deletion                   | ✅       |
# | Looping, key existence check          | ✅       |
# | Frequency count                       | ✅       |
# | Merge, sort, max/min                  | ✅       |
# | List to dict, invert dict             | ✅       |
# | Remove duplicates, nested dict access | ✅       |
# | Dict comprehension and common keys    | ✅       |

# ---

# Would you like this code in **Java or C++**, or as an **interactive quiz** format?
