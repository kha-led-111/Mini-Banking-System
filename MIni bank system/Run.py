from Bank import Bank
from Accounts import Accounts
class main():
    print("have account")
   
    check=int(input("1-have account or 2-don't have"))
    if(check==1):
       card_ID=input("please inter card ID ")
       password=(input("please inter card Password"))

       if(Accounts.check(Accounts,card_ID,password)):
            print("welcom sir") 
            print(" 1-show balance 2-deposit 3-withdraw 4-exchange 5-Exit") 
            operation=int(input("chose one"))
            if(operation==2):
               Accounts.Deposit(Accounts,int(input("add money ")),card_ID)
            elif(operation==3):
                Accounts.withdraw(Accounts,int(input("how much do you want")),card_ID)  
            elif(operation==1):
                Accounts.Show_Balance(Accounts,card_ID)  
            elif(operation==4):
                Accounts.Exchange(Accounts,input("enter person Id"),int(input("enter money")),card_ID)  
            elif(operation==5):
                print("thanks have good day")           


       else:raise KeyError("not found ID")

    else:
        Bank.Create_Account()
        
            