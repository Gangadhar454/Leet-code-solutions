l=[6,5,4,3,1,8,10,20,21,29]
l.sort(reverse=True)
for i in range(0,len(l)-2):
    p1=i+1
    p2=len(l)-1
    while(p1<p2):
        if (l[i]**2 == (l[p1]**2 +l[p2]**2)):
            print(l[p2],l[p1],l[i])
            p1+=1
            p2-=1
        elif l[i]**2 < (l[p1]**2 +l[p2]**2):
            p1+=1
        else:
            p2-=1

            
