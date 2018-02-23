
"""
n = 8765
power = 101
mod = 9691573

x = 0
while x < mod:
    if (x ** power) % mod == n:
        break
    x += 1

print x
"""
# Power of large numbers HackerRank
# The code has issue

def power(a,b,mod):
    ans = 1
    while b>0:
        if b%2==1:
            ans = (ans*a)%mod
        a = (a*a)%mod
        b/=2
    return ans
t = int(input())
while t>0:
    t-=1
    a,b = input().strip().split()
    A = 0
    mod = 10**9+7
    B = 0
    for i in range(len(a)):
        A = (A*10 + int(a[i]))%mod
    p = mod-1
    for i in range(len(b)):
        B = (B*10 + int(b[i]))%p
    if B == 0:
        print(1)
    else:
        print(power(A,B,mod))
