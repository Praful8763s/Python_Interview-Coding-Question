def Reversed_string(n):
    words = n.split()
    reversed_words = str[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence
n = input("Enter the words")
print("Original String are : f{n} is",n )
for i in str(n):
   print("reversed string are : ", Reversed_string(n))