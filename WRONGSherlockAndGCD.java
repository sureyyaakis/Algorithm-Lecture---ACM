//Sherlock and GCD

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.util.Scanner;

public class Solution {

      public static int gcd(int a, int b) {
        while (b != 0) {
            int t = b;
            b = a % b;
            a = t;
        }
        return a;
    }

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner reader = new Scanner(System.in);
        
        int T = reader.nextInt();
        for (int t=0; t<T; t++) {
            int N = reader.nextInt();
            int[] a = new int[N];
            for (int i=0; i<N; i++)
                a[i] = reader.nextInt();
            
            boolean result = true;
            for (int i=0; i<N; i++) {
                for (int j=i+1; j<N; j++) {
                    if (gcd(a[i],a[j]) != 1) {
                        result = false;
                        break;
                    }
                }
                if (result == false) 
                    break;
            }
            if (result == false)
                System.out.println("NO");
            else 
                System.out.println("YES");
            
           
        }
    }
}
