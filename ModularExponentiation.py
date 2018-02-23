# Modular Exponentiation in Python 

""" 
n = 8765
power = 101
mod = 9691573

x = 0
while x < mod:
    if (x ** power) % mod == n:
        break
    x += 1

print (x)

"""
x = 7
y = 2
z = 5

print(pow(x, y, z))
