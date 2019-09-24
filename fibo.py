print("fibonacci series")
n=int(input('enter the range'))
a=0
b=1
print(0,1,end=" ")
for i in range(1,n-1):
    fib=a+b
    a=b
    b=fib
    print(fib,end=" ")
