def print_pyramid(rows):
    for i in range(rows):
        # Print spaces
        for j in range(rows - i - 1):
            print(" ", end="")
        
        # Print stars
        for k in range(2 * i + 1):
            print("*", end="")
            
        print()  # Move to next line

# Get number of rows from user
rows = int(input("Enter number of rows: "))
print_pyramid(rows)