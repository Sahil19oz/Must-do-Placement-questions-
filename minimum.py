file=open("input.txt","r")
t=file.readline()
for _ in range(int(t)):
    n=file.readline()
    print(n)
    l=list(map(int,file.readline().split()))
    print(l)
    #l=[10,20,30,40,50,5,7]
    #l=[4 ,5 ,1 ,2 ,3]
    left=0
    right=len(l)-1
    while(left<right):
         mid=(left+(right))//2
         if l[mid]<l[mid+1]:
              left=mid+1
         else:
              right=mid
    print(l[l[mid]])
