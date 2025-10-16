from Accounts import Accounts
class Bank():
    def __init__(self,file=""):
        pass
    def Create_Account():
        #account(input("enter name"),int(input("inter balance")),input("inter password"))
        name=input("enter name")
        balance=int(input("inter balance"))
        password=input("inter password")
        Accounts.create(Accounts,name,password,balance)

     
