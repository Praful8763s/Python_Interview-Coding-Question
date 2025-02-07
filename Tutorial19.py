def fibnoacii_series(n):
    if n<=0:
        return "Input value should be positive"
    elif n==1:
        return 1
    elif n==2:
        return 2
    else:
        return fibnoacii_series(n-2)+fibnoacii_series(n-1)
n = int(input("Enter the number whose fibonacci"))
for i in range(1,n+1):
    print(fibnoacii_series(i))