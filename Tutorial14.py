# Define the list of tuples
x = [("x1", 1), ("x2", 2), ("x3", 3)]

# Use lambda to extract the second element from each tuple and print them
output = list(map(lambda item: item[1], x))

# Print the output
print(" ".join(map(str, output)))