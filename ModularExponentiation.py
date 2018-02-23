# Modular Exponentiation in Python 
# pow(x, y, z,)  = x ** y % z


def modexp(x, y, z):
  x = (x**y)%z
  print(x)
  #print(pow(x, y, z))

modexp(5, 4, 7)



