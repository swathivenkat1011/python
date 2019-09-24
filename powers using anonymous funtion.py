from functools import reduce
import math
n=int(input("ente the limit to display the powers"))
l=[x for x in range(1,n+1)]
print("list is ",l)

#map()

final_list=list(map(lambda g:pow(2,g),l))
print("final list is map power of 2",final_list)


#filter()

fl=list(filter(lambda h:(h%2==0),l))
print("list with reduce for even no",fl)


#reduce()
#no list gives value

fin_list=reduce((lambda z,a:z*a),l)
print("list with reduce to mul ele",fin_list)


