# Filename: list_tuple_set_interview.py

# ------------------ LIST QUESTIONS ------------------

def remove_duplicates_list(nums):
    """Remove duplicates from list while preserving order"""
    print("\n1. Remove Duplicates from List")
    seen = set()
    result = []
    for n in nums:
        if n not in seen:
            seen.add(n)
            result.append(n)
    print(result)

def find_second_largest(nums):
    """Find second largest number in a list"""
    print("\n2. Find Second Largest Number")
    unique = list(set(nums))
    unique.sort()
    print(unique[-2] if len(unique) >= 2 else "Not enough unique numbers")

def reverse_list(nums):
    """Reverse a list"""
    print("\n3. Reverse List")
    print(nums[::-1])

def common_elements_lists(l1, l2):
    """Find common elements in two lists"""
    print("\n4. Common Elements Between Two Lists")
    common = list(set(l1) & set(l2))
    print(common)

def rotate_list(nums, k):
    """Rotate list to the right by k steps"""
    print("\n5. Rotate List by K")
    k = k % len(nums)
    rotated = nums[-k:] + nums[:-k]
    print(rotated)


# ------------------ TUPLE QUESTIONS ------------------

def tuple_unpacking(t):
    """Unpack tuple into variables"""
    print("\n6. Tuple Unpacking")
    a, b, c = t
    print(f"a={a}, b={b}, c={c}")

def swap_with_tuples(a, b):
    """Swap values using tuple unpacking"""
    print("\n7. Swap Two Values Using Tuple")
    a, b = b, a
    print("After swap:", a, b)

def count_elements_tuple(t, elem):
    """Count occurrences of element in tuple"""
    print("\n8. Count Element in Tuple")
    print(f"{elem} occurs {t.count(elem)} times")


# ------------------ SET QUESTIONS ------------------

def set_operations(s1, s2):
    """Basic set operations: union, intersection, difference"""
    print("\n9. Set Operations")
    print("Union:", s1 | s2)
    print("Intersection:", s1 & s2)
    print("Difference:", s1 - s2)

def unique_chars_in_string(s):
    """Check if a string has all unique characters using set"""
    print("\n10. Unique Characters in String")
    print(len(set(s)) == len(s))

def remove_duplicates_with_set(lst):
    """Remove duplicates using set"""
    print("\n11. Remove Duplicates Using Set")
    print(list(set(lst)))


# ------------------ MAIN DRIVER ------------------

if __name__ == "__main__":
    # List functions
    remove_duplicates_list([1, 2, 2, 3, 4, 4, 5])
    find_second_largest([4, 1, 7, 7, 2, 9])
    reverse_list([1, 2, 3, 4, 5])
    common_elements_lists([1, 2, 3, 4], [3, 4, 5, 6])
    rotate_list([10, 20, 30, 40, 50], 2)

    # Tuple functions
    tuple_unpacking((10, 20, 30))
    swap_with_tuples(5, 10)
    count_elements_tuple((1, 2, 2, 3, 2, 4), 2)

    # Set functions
    set_operations({1, 2, 3}, {2, 3, 4})
    unique_chars_in_string("abcdefg")
    unique_chars_in_string("hello")
    remove_duplicates_with_set([1, 2, 2, 3, 4, 4, 5])
