# Power Of Large Numbers HackerRank

def pwrlargenum():
    t=(int)(input())
    for i in range(0,t):
        a,b=(input().split())
        print(pow((int)(a),(int)(b),1000000007))
        
pwrlargenum()
