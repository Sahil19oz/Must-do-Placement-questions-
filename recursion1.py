#Print a sequence of numbers starting with N, without using loop, in which  A[i+1] = A[i] - 5,  if  A[i]>0,
#else A[i+1]=A[i] + 5  repeat it until A[i]=N.

def fun(temp,n,flag):
    if temp==n:
        print(n)
        return
    print(temp,end=" ")
    if temp>0 and flag ==0:
        fun(temp-5,n,flag)
    else:
        flag=-1
        fun(temp+5,n,flag)
    
for _ in range(int(input())):
    n=int(input())
    temp=n
    flag=0
    print(n,end=" ")
    fun(temp-5,n,flag)
    
