def roman_to_integer(roman_str):
    # Dictionary of Roman numerals
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    # Initialize result
    result = 0
    
    # Convert to uppercase to handle both cases
    roman_str = roman_str.upper()
    
    # Iterate through the string
    for i in range(len(roman_str)):
        # If current value is greater than or equal to next value
        if i + 1 < len(roman_str) and roman_values[roman_str[i]] < roman_values[roman_str[i + 1]]:
            result -= roman_values[roman_str[i]]
        else:
            result += roman_values[roman_str[i]]
            
    return result

def main():
    try:
        roman_num = input("Enter a Roman numeral: ")
        integer_value = roman_to_integer(roman_num)
        print(f"Roman numeral {roman_num} = {integer_value}")
    except KeyError:
        print("Invalid Roman numeral! Please use valid Roman numerals (I, V, X, L, C, D, M)")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()