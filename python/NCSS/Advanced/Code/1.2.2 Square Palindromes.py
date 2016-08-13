#Square Palindromes
def is_square(x):
  return int(x**0.5)*x**0.5 == x
def is_palindrome(x):
  return int(str(x)[::-1]) == x
def is_square_palindrome(x):
    return is_square(x) and is_palindrome(x)

for i in range(1,1000):
    if is_square_palindrome(i):
      print(i)
input()
