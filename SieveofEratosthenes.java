// Prime Numbers - Sieve of Eratosthenes
// Prime number is any number greater than 1 and only divisible by itself.
// 1 is not prime number because it is not greater than 1


public class PrimeNum {
    
	public static void main(String[] args){
        
        for (int i=2;i<=100;i++) 
        {		
            for (int j=2;j<=i;j++)
            {			
                if(j==i) 
                {				
                    System.out.println(i);
				} 
                
				if(i%j==0)
                {
					break;
				}
			}
		}
	}

}

