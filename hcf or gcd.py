def gcd(a,b):
    if a>b:
        l=b
    else:
        l=a
    for i in range(1,l+1):
        if((a%i==0)and(b%i==0)):
            ans=i
    return ans
x,y=eval(input("enter 2 nos separated by comma"))
print("The hcf is",gcd(x,y))
