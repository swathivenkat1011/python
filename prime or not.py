print("no is prime or not")
n=int(input("enter a no"))
count=0
for i in range(1,n+1):
    if(n%i==0):
        count=count+1
if(count>2):
    print(n,"is not a prime no")
else:
    print(n,"is a prime no")
