def Triangle_Pattern(n):
    for i in range(n):
       print(" " * (n-i-1) + "*" *(2*i+1))
n = int(input("enter the number"))
Triangle_Pattern(n) 


