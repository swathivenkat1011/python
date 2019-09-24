print("armstrong no or not")
n=int(input("enter a no"))
sum=0
temp=n
while n>0:
    x=n%10
    y=x*x*x
    sum=sum+y
    n=n//10
    print(sum)
if sum==temp:
    print(temp,"is a armstrong no")
    
    
