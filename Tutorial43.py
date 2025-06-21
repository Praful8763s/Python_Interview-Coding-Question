
# write a function to check if a string is a palindrome

# def check_palindrome(s):
#     s = ' '.join(c for c in s if c.isalnum()).lower()
#     return s == s[::-1]
# strings =["rader", "madam", "hello", "level"]
# for s in strings:
#     if check_palindrome(s):
#         print(f"{s} is a palindrome")
#     else:
#         print(f"{s} is not a palindrome")



#write a function to check if a number fibnoacci series
import math
def is_perfect_square(x):
  s = int(math.sqrt(x))
  return s *s == x
def check_fibonacci(n):
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in a:
   if check_fibonacci(n):
       print(f"{n} is a Fibonacci number")
   else:
        print(f"{n} is not a Fibonacci number")