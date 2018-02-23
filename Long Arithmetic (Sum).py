# Long Arithmetic (Summation)

def sum_digits(n):
  s = 0
  while n:
    s += n % 10
    n //= 10
  print (s)
sum_digits(10003)
