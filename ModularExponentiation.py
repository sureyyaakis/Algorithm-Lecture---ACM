# Modular Exponentiation in Python 
# then applies % operator

a = 2
b = 100
c = (int)(1e9+7)

# Using direct fast method to compute 
# (a ^ b) % c.
d = pow(a, b, c)
print (d)
