# Long Arithmetic (Subtraction)

def sum_digits(n):
  s = 0
  while n:
    s -= n % 10 # sub
    n //= 10
  print (s)
sum_digits(10005)
