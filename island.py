l=[[1,1,0,0,0],
  [1,1,0,0,0],
  [0,0,1,0,0],
  [0,0,0,1,1]]
def change(l,i,j):
    if (i<0 or i >= len(l) or j<0 or j>=len(l[0]) or l[i][j]!=1):
        return
    l[i][j]=2
    change(l,i-1,j)
    change(l,i+1,j)
    change(l,i,j+1)
    change(l,i,j-1)
def count(l):
    count=0
    for i in range(len(l)):
        for j in range(len(l[0])):
            if (l[i][j]==1):
                change(l,i,j)
                count+=1
    return count
print(count(l))
    
