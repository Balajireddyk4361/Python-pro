# def add():
#     print('Addition')

# id(add)

# print(type(add()))



#
# innerfunction

def outer():
    print('outer function')

    def inner():
        print('inner function ')
    inner()
    inner()

    def login():
        print('login functon ')

    login()
    login()

outer()

#---------------------------------------------------------
# 2)
#how to invoke inner function into outer function

def out():
    print('print outer logo')

    def inn():
        print('print inner logo')
    return inn
reload=out()
reload()


#-----------------------------------------------------
# lamda function or name less function  

# lambda x=False
# How to Execute lambda function == > using 
'''
def sum(a,b):
    return a+b

r1=sum(10,20)
print(r1)
'''

# lamda function 

sum=lambda x,y:x+y

r1=sum(10,20)
print(r1)