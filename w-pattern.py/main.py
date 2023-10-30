a=input()
l=len(a)
s=(l*2)-2
s1=s*2
k=((l-1)+(l-2))*2+3
for i in range(0,l):
    for j in range(0,k):
        if(j==i or i+j==s or j-i==l*2-2 or j+i==s1):    
            print(a[i],end="")
        else:
            print("",end=" ")
    print()

