def print_square_pattern(binary_string):
    # Get the length of the binary string
    n = len(binary_string)

    # Define the size of the square pattern
    size = int(n**0.5)  # Assuming the square pattern should have sides equal to √n

    # C    heck if the binary string length can form a perfect square
    if size * size != n:
        print("The binary string cannot form a perfect square.")
    else:
        # Print the square pattern
        index = 0
        for i in range(size):
            for j in range(size):
                print(binary_string[index], end=" ")
                index += 1
            print()  # Newline after each row

if __name__ == "__main__":
    binary_string = "1111011100110001"
    print_square_pattern(binary_string)
