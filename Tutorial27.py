def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniformity
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Test cases
test_strings = input("enter the sente")
for string in test_strings:
    result = is_palindrome(string)
    print(f"'{string}' is a palindrome: {result}")