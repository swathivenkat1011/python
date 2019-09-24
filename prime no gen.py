print("prime no generation")
n=int(input("enter the range"))
count=0
for i in range(2,n+1):
    for j in range(1,i+1):
        if(i%j==0):
            count=count+1
    if(count==2):
        print(i,end="")
    count=0    
        
            
