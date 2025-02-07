
n = int(input("enter the number"))
def pyramid(n):
   for i in range(1,n+1):
     for j in range(n-1):
         print(" ",end = " ")
     for k in range(1,i):
        print("*",end =" ")
     print()
    #   
pyramid(n)