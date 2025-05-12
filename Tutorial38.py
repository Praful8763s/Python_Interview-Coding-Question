def print_pyramid(n):
    # Upper pyramid
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end="")
        for j in range(2*i+1):
            if j == 0 or j == 2*i or i == n-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    
    # Lower reverse pyramid
    for i in range(n-2, -1, -1):
        for j in range(n-i-1):
            print(" ", end="")
        for j in range(2*i+1):
            if j == 0 or j == 2*i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Test the pattern with height 5
n = int(input("Enter the rows"))
print_pyramid(n)