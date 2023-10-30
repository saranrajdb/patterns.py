a="abcde"
l=len(a)
for i in range(0,l):
    for j in range(0,l):
        if i==0 or i==l-1 or i+j==l-1:
            print(a[j],end=" ")
        else:
            print(" ",end=" ")
    print()