def spiral(l):
    top=0
    bottom=len(l)-1
    left=0
    right=len(l[0])-1
    di=0
    while(top<=bottom and left <=right):
        if di==0:
            for i in range(left,right+1):
                print(l[top][i],end=" ")
            top+=1
        elif di==1:
            for i in range(top,bottom+1):
                print(l[i][right],end=" ")
            right-=1
        elif di==2:
            for i in range(right,left-1,-1):
                print(l[bottom][i],end=" ")
            bottom-=1
        elif di==3:
            for i in range(bottom,top-1,-1):
                print(l[i][left],end=" ")
            left+=1
        di=(di+1)%4
l=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]
#l=[[1,2,3,4,5],[6,7,8,9,10]]
spiral(l)
