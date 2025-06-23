'''
4)try=>risky code 
1)except
2)finally
3)raise

'''
# fp=open('xyz.txt','r')
# data=fp.read()
# print(data)
#FileNotFoundError: [Errno 2] No such file or directory: 'xyz.txt'

'''
print(10/5)
print(10/0)
print(10/1)
print('goodmorning')
'''
'''
#ZeroDivisionError
print(10/5)
try :
    print(10/0)
    

except ZeroDivisionError as error:
    print(10/1)
print("Good morning")'''

#-------------------------------------------------------
'''
try :#risky code
    fp=open("read.txt","r")
 

except FileNotFoundError as error:
    fp=open('texts.txt','r')  # handle code
data=fp.read()
print(data)
print("good morning")
fp.close()
'''

#------------------------------------------------------------

fp=None
num=None

try:
    a=int(input("Enter No::"))
    b=int(input("Enter No::"))
    print('number is',a,":",a)
    print(a/0)
    print(b/3)
except ValueError as error:
    print("pleace Enter only numbers")
except ZeroDivisionError as error:
    print('wecont devide by zero')
    
except FileExistsError as error:
   print("File no found pleace check")