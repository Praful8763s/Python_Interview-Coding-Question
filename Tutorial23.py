def binary_patter_0_1(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end=" ")
            for k in range(i+1):
                if i==n//2 and k==i//2:
                    print("0",end ="")
                else:
                    print("1",end="")
        # print()
    print()
n = int(input("enter the rows"))
binary_patter_0_1(n)