def addpoly(p1,p2):
    c=[]
    m=len(p1)
    n=len(p2)
    i=j=k=0
    while i<m and j<n:
        if p1[i][0]==p2[j][0]:
            c[k][0].append(p1[i][0]+p2[j][0])
            c[k][1].append(p1[i][1])
            i+=1
            j+=1
            k+=1
        elif p1[i][0]>p2[j][0]:
                c[k][0].append(p1[i][0])
                c[k][1].append(p1[i][1])
                i+=1
                k+=1
        else:
                c[k][0].append(p2[j][0])
                c[k][1].append(p2[j][1])
                j+=1
                k+=1
    while i<m:
        c[k][0].append(p1[i][0])
        c[k][1].append(p1[i][1])
        i+=1
        k+=1
    while j<n:
         c[k][0].append(p2[j][0])
         c[k][1].append(p2[j][1])
         j+=1
         k+=1
    return c
