arr=[3,4,7,2,-3,1,4,2]
k=7
count=0
cumu={}
x=0
for i in range(len(arr)):
    x=x+arr[i]
    if(x==k):
        count+=1
    else:
        if x-k in cumu.keys():
            count+=cumu[x-k]
    if x not in cumu.keys():
            cumu[x]=1
    else:
        cumu[x]+=1
print(count)
