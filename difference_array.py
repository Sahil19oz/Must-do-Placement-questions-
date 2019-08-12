def dig(x):
    while x>9:
        a=x%10
        x//=10
        b=x%10
        p=abs(a-b)
        if p!=1:
            return 0
    return 1
for _ in range(int(input())):
    n,k=map(int,input().split())
    ar=list(map(int,input().split()))
    ans=[]
    for i in ar:
        if i<k and i>9:
            nn=dig(i)
            if nn==1:
                ans.append(i)
    if len(ans)>0:
        print(*ans)
    else:
        print(-1)
    
