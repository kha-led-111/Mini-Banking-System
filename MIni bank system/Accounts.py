import json
import os
import uuid
class Accounts:
    data_file="Acounts.jason"
    def __init__(self,Id,Name,Password,balance):
        self.id=Id
        self.name=Name
        self.password=Password
        self.balance=balance
    def create(cls,name,password,balannce):
        #generate uniqe id
        Id=str(uuid.uuid4())
        #create new account
        new_account=cls(Id,name,password,balannce)

        data=[]
        if os.path.exists(cls.data_file):
            with open(cls.data_file,"r") as f:
                try:
                    data=json.load(f)
                except json.JSONDecodeError:
                    data=[]
        data.append({
            "Id":Id,
            "Name":name,
            "Password":password,
            "Balance":balannce

        })            
        #to save data
        with open(cls.data_file,"w") as f:
            json.dump(data,f,indent=4)
    #ايداع        
    def Deposit(self,D_Mony,card_Id):
       with open(self.data_file,"r") as f:
            data=json.load(f)
            for acc in data:
                if acc["Id"]==card_Id:
                     acc["Balance"] += D_Mony 
                     print("the money has deposited ")  
                     break 
            else:
                print("not founded")
                return
       with open(self.data_file,"w") as f:
            json.dump(data,f,indent=4) 
       print("the money has deposited correctly ")       
  #سحب    
    def withdraw(self,W_Mony,card_id):
        with open(self.data_file,"r") as f:
            data=json.load(f)
            for acc in data:
                if acc["Id"]==card_id:
                     acc["Balance"] -= W_Mony 
                     print("the money has withdrawed ")  
                     break 
            else:
                print("not founded")
                return
        with open(self.data_file,"w") as f:
            json.dump(data,f,indent=4) 
        print("the money has withdrawed correctly ")  
        
  #check pass and Id
    def check(self,id,password):
        with open(self.data_file,"r") as f:
            data=json.load(f)

            for Acc in data:
                if Acc["Id"]==id  and Acc["Password"]==password:
                  
                    return True
            print("not found")
            return False  
        #show balance
    def Show_Balance(self,card_id):
        with open(self.data_file,"r") as f:
            data=json.load(f)
            for acc in data:
                if acc["Id"]==card_id:
                    print("the balance is ",{acc["Balance"]})
                    break
                else:
                    print("not founded")
                return
        with open(self.data_file,"w") as f:
            json.dump(data,f,indent=4)    
    def Exchange(self,E_Id,E_money,Card_Id) :
       self.withdraw(self,E_money,Card_Id)
       self.Deposit(self,E_money,E_Id)
        
       






          






    