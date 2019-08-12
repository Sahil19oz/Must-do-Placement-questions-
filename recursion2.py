#Write a program to reverse digits of a number N

def rev(temp,ans):
    if temp==0:
        print(ans)
        return
    ans=(ans*10)+(temp%10)
    rev(temp//10,ans)
    
for _ in range(int(input())):
    temp=int(input())
    ans=0
    rev(temp,ans)
