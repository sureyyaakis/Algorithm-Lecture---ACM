#Efficient Prime Factorization

n=int(input("Enter the number: "))
if n==1 :  #because the below logic doesn't work on 1
    print([n])
for i in range(2 , n+1):
    if n%i==0 :
        n1=i  #get factor
        for b in range(2,n+1): #check if it is prime
            if ((n1%b)==0) & (n1==b):
                print([n1])
            elif (n1%b)==0 or n1<b:  #if not then pass
                break



