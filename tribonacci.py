def tri(n):
    dp=[0]*(n+2)
    if n==0:
        return dp[0]
    elif n==1:
        dp[1]=1
        return dp[1]
    else:
        dp[2]=1
        for i in range(3,n+2):
            dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
    return dp[n+1]

n=int(input())
print(tri(n))
