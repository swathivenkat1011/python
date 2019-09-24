n=int(input("enter the input"))
for i in range(n,0,-1):
    for j in range(0,i):
        print(" ",end="")
    print('/',end="")
    for z in range(0,n-1):
        for y in range(0,8):
            print(" ",end="")
        print('/',end="")
    print('')

