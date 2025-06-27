def dict():
 dict ={1:Rohan,2: Sohan}
 dict1 = list(dict)
 for i in range(len(dict1)):
    for j in range(i+1, len(dict1)):
        if dict1[i] > dict1[j]:
         dict1[i], dict1[j] = dict1[j],dict1[i]
 return dict1
print(dict)