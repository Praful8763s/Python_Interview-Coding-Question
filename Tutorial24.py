def int_into_roman(num):
    val =[
        1000,900,500,400,100,90,50,40,10,9,5,4,1,0]
    syb=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I","B"]
    roman_num =' '
    i=0
    while num>0:
      for i in range(num//val[i]):
         roman_num+=syb[i]
         num-=val[i]
      i+=1
    return roman_num
num = int(input("enter the Integer Number :"))
print("Roman number are : ",int_into_roman(num))