a,b=eval(input("enter 2 nos"))
print("enter\n1 to add\n2 to sub\n3 to mul\n4 to div\n5 to mod")
n=int(input())
if n==1:
    print("The sum of",a,"and",b,"is",a+b)
elif n==2:
    print("The sub of",a,"and",b,"is",a-b)
elif n==3:
    print("The mul of",a,"and",b,"is",a*b)
elif n==4:
    if((type(a)==int)and(type(b)==int)):
       print("The div of",a,"and",b,"is",a//b)
    else:
       print("The div of",a,"and",b,"is",a/b)
elif n==5:
    print("The mod of",a,"and",b,"is",a%b)
      
        
