#random funs
import random
print(random.random())
print("randint b/w 0to2 includes the last value 2 also",random.randint(0,2))




#random.randrange(start,stop,step)


#random.randrange() with only one argument
print("Random number between 0 and 50 : ", random.randrange(50))
#random.randrange() with two arguments
print("Random number between 20 and 40 : ", random.randrange(20,40))
#random.randrange() with three argument
print("Random number between 0 and 60 with step value 5: ", random.randrange(0,60,5))
