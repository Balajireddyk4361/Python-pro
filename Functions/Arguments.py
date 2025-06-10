''' Arguments are 4 types

->positional argument
->keyword argument
->default argument
->variable argument
'''
#------------------------------------------------------------------
#-> positional argument
def some(a,b):
    print(a-b)

some(100,200)
# changing position of the argument
some(200,100)


#-------------------------------------------------------------------
# ->keyword argument
def average(a,b):
    print(a+b)

average(a=100,b=200)
# changing keyword but not changing any value
average(b=100,a=200)

#-----------------------------------------------------------

# ->default argument

def arrange(a,b,c=10):
    print(a+b+c)

arrange(1,2,3)
# default vaile is 10
arrange(10,20)
arrange(30,40)

#-----------------------------------------------------------------



