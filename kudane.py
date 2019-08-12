def maxarray(ar,size):
    maxx=0
    summ=0
    for i in ar:
        summ+=i
        if summ<0:
            summ=0
        elif summ>maxx:
            maxx=summ
    return maxx
a = [-2, -3, 4, -1, -2, 1, 5, -3] 
print("Maximum contiguous sum is" , maxarray(a,len(a)))
            
    
