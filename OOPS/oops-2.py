  
class Employee:
    branch_code=11
    



e1=Employee()
e2=Employee()
e3=Employee()


print(e1.__dict__)
print(e2.__dict__)
print(e3.__dict__)

#----------------------------------------------------

# self is a pointer pointing to current object
#


class Account:
    def open_Account(self):
        print('Account opened')

    def deposit_Amount(self):
        print('Amount depposited successfully')

    def Withdrawal_Amount(self):
        print('Amount is Withdrawald success')

    def get_Bal(self):
        return 199999
    
    def Close_Acount(self):
        print('your Account is closed')

# invoking 
a1=Account()
a1.open_Account()
a1.deposit_Amount()
a1.Withdrawal_Amount()
a1.get_Bal()
a1.Close_Acount( )

a2=Account()
a2.open_Account()
a2.deposit_Amount()
a2.Withdrawal_Amount()
a2.get_Bal()
a2.Close_Acount( )

#---------------------------------------------------------------------------------

