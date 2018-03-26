// not done 
// (a*b)%M = ((a%M)*(b%M))%M
/**
 * Recursive (Not recommended)
 * if b = 0                   1
 * if b is even and b > 0    (a^2)^(b/2)
 * if b is odd                a^b = a*((a^2)^(b-1)/2)) 
*/ 

  public static int modExpon(int a = 5, int b = 3, int M = 7 )
  {
  
    if (a == 0)
        return 1;
    else if (b%2 == 0) 
        return modExpon(a*a, b/2, M) % M;
    else 
        return ((a%M) * modExpon (a*a, (b-1)/2,  M)) % m;
 }
// Iterative Version
