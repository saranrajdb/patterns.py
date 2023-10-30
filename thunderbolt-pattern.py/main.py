s="input"
l=len(s)
for i in range(0,l*2):
    for j in range(0,l):
        if i+j==l-1 or i==l-1 or i+j==l*2-2:
            print(s[j],end=" ")
        else:
            print(" ",end=" ")
    print()