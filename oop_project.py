from bank_accounts import *

Ray = BankAccount(1000, "Ray")
Sara = BankAccount(2000, "Sara")

Ray.getBalance()
Sara.getBalance()

Sara.deposit(500)

Ray.withdraw(10000)
Ray.withdraw(10)

Ray.transfer(200, Sara)
Ray.transfer(900, Sara)

Samey = InterestRewardsAcct(1000, 'Samey')
Samey.getBalance()
Samey.deposit(1000)
Samey.transfer(100, Ray)

Tracy = SavingsAcct(7000, "Tracy")
Tracy.transfer(2000, Ray)
Tracy.getBalance()
Tracy.transfer(20000, Ray)
