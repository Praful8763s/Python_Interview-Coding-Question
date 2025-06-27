
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str  # Prepend each character
    return reversed_str
#reverse_string
# Example usage:
text = "Hello, World!"
print(reverse_string(text))  # Output: !dlroW ,olleH