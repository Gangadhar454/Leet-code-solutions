def gcd(num1,num2):
    i = 1
    while(i <= num1 and i <= num2):
        if(num1 % i == 0 and num2 % i == 0):
            gcd = i
        i = i + 1
    return gcd
def rotation(arr,k):
    n=len(arr)
    sets=gcd(len(arr),k)
    for i in range(sets):
        j=i
        temp=arr[i]
        d=(j+k)%n
        while(d!=i):
            arr[j]=arr[d]
            j=d
            d=(j+k)%n
        arr[j]=temp
    return arr
print(rotation([1,2,3,4,5,6],4))

    
