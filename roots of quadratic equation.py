import math
print('ROOTS OF A QUADRATIC EQUATION')
a,b,c=eval(input("enter the values of a b c"))
q=(b*b)-(4*a*c)
x=-b/(2*a)
y=(math.sqrt((b*b)-(4*a*c)))/(2*a)
if q==0:
    print("the roots are equal","r1 = ",-b/(2*a),"r2 =",-b/(2*a))
if q>0:
    print("the roots are real","r1 =",x+y,"r2 =",x-y)
else:
    print("the roots are imaginary","r1 =",x,"+i",y,"r2 =",x,"-i",y)
