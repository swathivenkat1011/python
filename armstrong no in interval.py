print("Armstrong no within a interval")
limit=int(input("enter the interval"))
print("The armstrong nos are")
for n in range(1,limit+1):
    sum=0
    temp=n
    while n>0:
        x=n%10
        y=x*x*x
        sum=sum+y
        n=n//10
    if sum==temp:
        print(sum,end=" ")
    
    

