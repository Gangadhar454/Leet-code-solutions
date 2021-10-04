string="pwwkew"
j=0
i=0
Set=set()
MAX=0
while i < len(string):
    if(string[i] not in Set):
        Set.add(string[i])
        i+=1
        MAX=max(MAX,len(Set))
    else:
        Set.remove(string[j])
        j+=1
print(MAX)
print(''.join(Set))

        
