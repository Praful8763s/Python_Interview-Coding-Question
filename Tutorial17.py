def is_amstrong(n):
    return sum(int(digit)**len(str(n)))
n = int(input("Enter the number"))
for digit in str(n):
    if is_amstrong(n):
        print("n is amstrong", is_amstrong(n))
    else:
        print("n is not amstrong")