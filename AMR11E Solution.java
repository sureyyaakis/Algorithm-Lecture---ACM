/**
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

*/

// not done!

// make a prime list
// n = input [1,1001]
// T = test case how many n [1,21]
// find at least three distinct prime factors[ex: 1, 30(2,3,5)]

 
class AMR11E {
  public static void main(String[] args) {
 
  List<Integer> primes = new ArrayList<Integer>();
  
  
  for(int i=2; i<=100; i++){
    
      for(int j=2; j<=i; j++){
        if(j==i) 
        {
          System.out.println(i);
          primes.add(i);
        }
        if(i%j == 0)
        break;
      }
    
  }        
 
  System.out.println(primes);
  
  }
}

