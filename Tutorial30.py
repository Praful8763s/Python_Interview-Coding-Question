input_list = [1, 2, 1, 3, 4, 5, 1]
element_to_check = 1
occurrence_count = 0

for item in input_list:
    if item == element_to_check:
        occurrence_count += 1

print(f"The element {element_to_check} occurs {occurrence_count} times in the list.")