def create_and_access_dict():
    print("\n1. Create and Access Dictionary")
    person = {'name': 'Praful', 'age': 23, 'city': 'Indore'}
    print("Name:", person['name'])
    return person

def add_and_update(person):
    print("\n2. Add and Update Key-Value")
    person['profession'] = 'Engineer'
    person['age'] = 24
    print(person)
    return person

def delete_key(person):
    print("\n3. Delete Key")
    if 'city' in person:
        del person['city']
    print(person)
    return person

def loop_through_dict(person):
    print("\n4. Loop Through Dictionary")
    for key, value in person.items():
        print(f"{key}: {value}")

def check_key_existence(person):
    print("\n5. Check Key Existence")
    print("age" in person)
    print("salary" in person)

def count_frequency(data):
    print("\n6. Count Frequency of Elements")
    freq = {}
    for char in data:
        freq[char] = freq.get(char, 0) + 1
    print(freq)
    return freq

def merge_dicts(d1, d2):
    print("\n7. Merge Two Dictionaries")
    merged = {**d1, **d2}
    print(merged)
    return merged

def sort_dict(d):
    print("\n8. Sort by Keys and Values")
    print("Sorted by keys:", dict(sorted(d.items())))
    print("Sorted by values:", dict(sorted(d.items(), key=lambda item: item[1])))

def find_max_min(d):
    print("\n9. Max/Min Key and Value")
    print("Max key:", max(d))
    print("Min value:", min(d.values()))

def lists_to_dict(keys, values):
    print("\n10. Lists to Dictionary")
    converted = dict(zip(keys, values))
    print(converted)
    return converted

def invert_dict(d):
    print("\n11. Invert Dictionary")
    inverted = {v: k for k, v in d.items()}
    print(inverted)
    return inverted

def remove_duplicate_values(d):
    print("\n12. Remove Duplicate Values")
    unique_values = set()
    unique_dict = {}
    for k, v in d.items():
        if v not in unique_values:
            unique_values.add(v)
            unique_dict[k] = v
    print(unique_dict)
    return unique_dict

def nested_dict_access(student):
    print("\n13. Nested Dictionary Access")
    print("Math Marks:", student['marks']['math'])

def dict_comprehension():
    print("\n14. Dictionary Comprehension")
    squares = {x: x**2 for x in range(1, 6)}
    print(squares)

def find_common_keys(dict1, dict2):
    print("\n15. Common Keys")
    common = dict1.keys() & dict2.keys()
    print("Common keys:", common)


# ------------------ MAIN PROGRAM ------------------

if __name__ == "__main__":
    person = create_and_access_dict()
    person = add_and_update(person)
    person = delete_key(person)
    loop_through_dict(person)
    check_key_existence(person)
    count_frequency(['a', 'b', 'a', 'c', 'b', 'a'])
    merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
    sort_dict({'banana': 3, 'apple': 4, 'cherry': 1})
    find_max_min({'banana': 3, 'apple': 4, 'cherry': 1})
    lists_to_dict(['id', 'name', 'age'], [101, 'Praful', 23])
    invert_dict({'a': 1, 'b': 2, 'c': 3})
    remove_duplicate_values({'a': 1, 'b': 2, 'c': 1, 'd': 2})
    nested_dict_access({'name': 'Praful', 'marks': {'math': 90, 'science': 95}})
    dict_comprehension()
    find_common_keys({'a': 1, 'b': 2, 'c': 3}, {'b': 5, 'c': 6, 'd': 7})
