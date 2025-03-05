class BankAccount:
  def __init__(self,name: str,account: str,balance: int):
    self.__name=name
    self.__account=account
    self.__balance=balance
  
  def deposit(self,amount: int):
    self.__balance+=amount
  
  def withdraw(self,amount: int):
    self.__balance-=amount
    self.__service_charge()

  @property
  def balance(self):
    return self.__balance
  
  def __service_charge(self):
    self.__balance-=self.__balance*0.01

if __name__ =="__main__":
  account = BankAccount("Randy Riches", "12345-6789", 1000)
  account.withdraw(100)
  print(account.balance)  
  account.deposit(100)
  print(account.balance)
