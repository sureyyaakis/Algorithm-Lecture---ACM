// *** not done!

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

