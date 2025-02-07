
# First Techniques to used to create program
def sort_even_odd(arr):
    # Separate even and odd numbers
    evens = sorted([x for x in arr if x % 2 == 0])
    odds = sorted([x for x in arr if x % 2 != 0])
    
    # Combine even numbers first, then odd numbers
    sorted_arr = evens + odds
    return sorted_arr

# Example usage
#Second technqiues to use the program using lambda functions
arr = [3, 2, 1, 4, 8, 5, 6, 7]
sorted_arr = sort_even_odd(arr)
print(sorted_arr)  # Output: [2, 4, 6, 8, 1, 3, 5, 7]
arr = [3, 2, 1, 4, 8, 5, 6, 7]

# Sort even numbers first, then odd numbers, both in ascending order
sorted_arr = sorted(arr, key=lambda x: (x % 2, x))

print(sorted_arr)