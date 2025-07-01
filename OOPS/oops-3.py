class Account :

    def open_account(self):
        print("Account opened")

    def deposit_Amount(self,amount):
        print( amount,' :Amount deposited')
        
f1=Account()
f1.open_account()
f1.deposit_Amount(50000)
#/////////////////////////////////////////////////////////////////
class Test:
#instance method 
    def __init__(self):
        print("Specal Jilebi")

    def m1(self):
        pass 
#class method 
    @classmethod
    def m2(cls):
        pass 
 #static method
    @staticmethod
    def m3():
        pass 

Test()