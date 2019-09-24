print('GREATEST OF 3 NOS')
x,y,z=eval(input("enter 3 nos separated by comma"))
if x>y and x>z:
    print(x,"is the greatest")
elif y>x and y>z:
     print(y,"is the greatest")
elif z>x and z>y:
     print(z,"is the greatest")
else:
     print("some of the nos are equal")
