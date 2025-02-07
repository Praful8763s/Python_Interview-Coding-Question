def count_characters(s):
    count_dict = {}
    for char in s:
        if char != ' ':
            if char in count_dict:
                count_dict[char] +=1
            else:
                return s
    return count_dict

string = "AaBb@&#!"
result = count_characters(string)
print(result)

# Count characters with frequency between 0 to 5
filtered_result = {k: v for k, v in result.items() if 0 <= v <= 5}
print(filtered_result)

# Count the number of characters that have a frequency between 0 to 5
count_in_range = len(filtered_result)
print(f"Number of characters with frequency between 0 to 5: {count_in_range}")