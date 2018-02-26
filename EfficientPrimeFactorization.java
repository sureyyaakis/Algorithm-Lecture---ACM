#Efficient Prime Factorization
int num = 24;
int num1 = num;

for (int i=2; i<num1; i++) {
      while (num%i == 0) {
        System.out.println(i);
        num /=i;
      }
}




