def pascal(n):
    p=[]
    for i in range(1,n+1):
        c=[]
        c.append(1)
        for j in range(1,len(p)+1):
            if j>=len(p):
                c.append(1)
            else:
                c.append(p[j-1]+p[j])
        p=c
        print(c)


