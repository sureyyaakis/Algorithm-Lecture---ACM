# Greatest Common Division (GCD)
# With subtract 

def gcd(a,b):
  
  while(a != b):
    if (a>b):
      a = a-b
    else:
      b = b-a
  return a
  
print(gcd(252, 105))
