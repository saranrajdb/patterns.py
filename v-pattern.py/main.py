a="name"
l=len(a)
for i in range(0,l):
    for j in range(0,l*2-1):
        if(j==i or i+j==l*2-2):    
            print(a[i],end="")
        else:
            print("",end=" ")
    print()