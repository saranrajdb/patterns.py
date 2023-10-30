a="sarans"
l=len(a)
n=(l//2)-1
for i in range(0,l):
    for j in range(0,l):
        if(j==i and i<=n or i+j==l-1):    
            print(a[i],end=" ")
        else:
            print(" ",end=" ")
    print()