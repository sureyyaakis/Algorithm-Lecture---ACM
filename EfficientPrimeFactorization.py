//Efficient Prime Factorization

n=int(input("Enter the number: "))
if n==1 : 
    print([n])
for i in range(2 , n+1):
    if n%i==0 :
        n1=i  
        for b in range(2,n+1): 
            if ((n1%b)==0) & (n1==b):
                print([n1])
            elif (n1%b)==0 or n1<b:  
                break



