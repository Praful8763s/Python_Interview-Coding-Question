n = 5
alph = 65
for i in range(0,n):
    print(" "*(n-i),end ="")
    """pattern in this location to change the position to enter the next line of alphabet print using f
    using then print the star and alphabet in A in a B in b C in c D in d E in e to Z in z """
    for j in range(0,i+1):
        print(chr(alph),end=" ")
        alph+=1
    alph = 65
    print()