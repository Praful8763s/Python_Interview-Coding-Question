def is_palindrome(number):
    # Convert number to string for easy comparison
    num_str = str(number)
    
    # Compare the string with its reverse
    return num_str == num_str[::-1]

def check_palindrome():
    try:
        # Get input from user
        num = int(input("Enter a number to check if it's palindrome: "))
        
        # Check if it's palindrome
        if is_palindrome(num):
            print(f"{num} is a palindrome number!")
        else:
            print(f"{num} is not a palindrome number!")
            
        # Show the reverse number for reference
        reverse_num = int(str(num)[::-1])
        print(f"Original number: {num}")
        print(f"Reverse number: {reverse_num}")
        
    except ValueError:
        print("Please enter a valid integer number!")

if __name__ == "__main__":
    check_palindrome()