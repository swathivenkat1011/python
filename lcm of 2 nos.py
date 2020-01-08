def lcm(x, y):  
   if x > y:  
       greater = x  
   else:  
       greater = y  
   while(True):  
       if((greater % x == 0) and (greater % y == 0)):  
           lcm = greater  
           break  
       greater += 1  
   return lcm  
  
  
a,b=eval(input("enter 2 nos seperated by comma"))
print("The L.C.M. of",a,"and",b,"is", lcm(a,b))
