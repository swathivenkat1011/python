list1=[]
x=int(input("enter a no"))
n=int(input("enter the no of numbers"))
for i in range(0,n):
    list1.append(int(input()))
print("The nos divisible by",x,"in",list1,"are",end="\n")    
for z in list1:
    if(z%x==0):
        print(z)
    
    
