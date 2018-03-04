"""
Algorithm:
1- Initialise an integer array (till 2700) to 0.
2- Start with 2(say i for general case) and check if var[i]==0, if yes, increment count of all its multiples by 1.
3- Repeat the point 2 for all numbers till 2700.
4- Find and store first 1000 numbers that have number of prime factors >=3. # I didnt get this part/?
"""
primes = []
import math
for num in range(2, 2701):
    if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
       primes.append(num)

print(primes[3:1001])
print("The index: ",len(primes[3:1001])) # There arent 1000 prime numbers between 0 to 2700

