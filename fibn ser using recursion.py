
def fib(n):
    if n<=1:
        return 1
    else:
        return (fib(n-1)+fib(n-2))
n=int(input("enter the range for series\n"))
if n<=0:
    print("enter avalid no")
else:
    print("Fibonacci series is ")
    for i in range(n):
        print(fib(n))
'''def fib(n):
    if n<=1:
        return 1
    else:
        return (fib(n-1)+fib(n-2))'''
      

      
