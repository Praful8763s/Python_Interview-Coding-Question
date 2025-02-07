def fact_num(n):
    if(n==0):
        return 1;
    else: 
        ## using recursion use to developed the code of factorial program
        ## put input o that output 1 and put input 5 the
                return n*(fact_num(n-1))
num = int(input("Enter the number"))
print(fact_num(num))