def Palindron(n):
    return str(n)==str(n)[::-1]
n = int(input("enter the number"))
if Palindron(n):
    print("this is palindrone", Palindron(n))
else:
    print("not palindorne")