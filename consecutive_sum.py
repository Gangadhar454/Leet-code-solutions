def consecutive(n):
    count=0
    for i in range(1,n):
        j=i
        s=0
        while(j<n or s<n):
            s+=j
            if(s==n):
                count=count+1
            j=j+1
    return count
print(consecutive(15))
            
