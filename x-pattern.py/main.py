a="saran"
l=len(a)
for i in range(0,l):
    for j in range(0,l):
        if(j==i or i+j==l-1):    
            print(a[i],end=" ")
        else:
            print(" ",end=" ")
    print()
