def count(str1, str2):
    str1= set(str1)
    str2 = set(str2)
    s = str1 & str2
    return s(count)
    
str1 = input("enter the first string")
str2 = input("enter the second string")
print(count(str1,str2))