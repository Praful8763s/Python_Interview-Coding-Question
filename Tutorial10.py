def check_even_odd(num):
    # num = int(input("Enter a number: "))
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"            

if  __name__ == "__main__":
    num = int(input("Enter a number: "))
    check_even_odd(num)