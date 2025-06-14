# map is inbult function it Expection two arguments
# map(function,sequence)
# sequence maight be tuple,set,dict,sting,numer etc
'''
1) map is a inbult function
2)Executing provided function for every element of sequence
'''

product_prices=[98,198,298,398,498,598]
# def addone(price):
#     return price+1

# map_obj=map[addone,product_prices]
# print(list(map(lambda product_prices=product_prices+1,98,198,298,398,498,598)))


# to change lowercase to uupper case 
ename=['balaji','reddy','orange']

def changecase(ename):
    return ename.upper()

new_names=list(map(changecase,ename))

print(new_names)
#------------------------------------------
#lambda functions
enames=['balaji','reddy','orange']


odd=list(map(lambda ename:ename.upper(),enames))
print(odd)
#----------------------------------------------

#for loop iteration 
'''
uname=['balaji','reddy','orange']

new_unams=[]
for unames in uname:
   new_unams= unames.upper()

print(new_unams)    
'''

#----------------------------------------------------------
 # 1)Example =2
 # print even numbers in sequencec by using labbda function
num=[10,9,12,11,13,14,155,16,]

Even_num=list(filter(lambda num: num %2==0 ,num))

print(Even_num)






