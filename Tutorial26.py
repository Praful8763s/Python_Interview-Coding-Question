def string_array_to_dict(string_array):
    result = {string: len(string) for string in string_array}
    return result

# Example usage
string_array = ["apple", "banana", "cherry"]
length_dict = string_array_to_dict(string_array)
print(length_dict)