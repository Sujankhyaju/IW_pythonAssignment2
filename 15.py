# 15. Imagine you are designing a banking application. What would a
# customer look like? What attributes would she have? What methods
# would she have?

def saving(customer):
    deposite_amt = int(input("Enter deposite amount:: "))
    total_balance = customer['Balance']
    total_balance += deposite_amt
    customer.update({'Balance':total_balance})
    print(f"your total balance is :{customer['Balance']}")
    
def withdraw(customer):
    withdraw_amt = int(input("Enter amount to withdraw:: "))
    if customer['Balance'] > 0 and customer['Balance']>=withdraw_amt:
        
        customer['Balance'] -= withdraw_amt
        
        print(f"Your remaining balance is ::{customer['Balance']}")
    
    else:
        print("Insufficient Balance")

def authentication(accountNo):
    if accountNo in customer.values():
        return True
    else:
        return False


def intakeAccountNo():
    accountNo = input("Enter account No.::")
    authen = authentication(accountNo)
    return authen


customer = {'Name':'Suchit','Address':'Bhaktapur','A/c_no.':'13100XXXXX001','Gender':'Male','Balance':1000}
actions =['Saving','Withdraw']

print(customer['Balance'])

for _ , row in enumerate(actions,start=1):
    print(f"{_}. {row}")
    
option = int(input("Choose Your Options::"))

if option == 1:
    print("----------You have selected 'SAVING' Mode-------")
    if intakeAccountNo() == True:
        saving(customer)
    else:
        print(">>>>Enter Valid account number<<<<")

elif option==2:
    print("----------You have selected 'WITHDRAW' Mode-------")
    if intakeAccountNo() == True:
        withdraw(customer)
    else:
        print(">>>>>Enter Valid account number<<<<")
    
else:
    print(">>>>>Invalid Option!!!!<<<<<")