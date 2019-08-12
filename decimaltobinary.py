import math
def dec(n):
    l=""
    while(n>0):
        l+=str(n%2)
        n=n//2
    return l[::-1]

def bina(n):
    ans=0
    n=str(n)
    n=n[::-1]
    for i in range(len(n)):
        if n[i]=='1':
            ans+=math.pow(2,i)
    return int(ans)
            
