def fibonacci_series(n):
    # Initialize first two numbers
    a, b = 0, 1
    
    # Check if n is valid
    if n <= 0:
        return "Please enter a positive number"
    elif n == 1:
        return [0]
    
    # Create fibonacci series
    fib_series = [a, b]
    
    # Generate series
    for _ in range(2, n):
        c = a + b
        fib_series.append(c)
        a, b = b, c
    
    return fib_series

def main():
    try:
        n = int(input("Enter the number of terms for Fibonacci series: "))
        result = fibonacci_series(n)
        
        if isinstance(result, list):
            print(f"\nFibonacci series with {n} terms:")
            print(" ".join(map(str, result)))
        else:
            print(result)
            
    except ValueError:
        print("Please enter a valid integer!")

if __name__ == "__main__":
    main()