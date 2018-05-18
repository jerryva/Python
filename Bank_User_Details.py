   	
 #!/usr/bin/env python
#creating dictionary
bankAccount=dict()
#class student mad here
class account:
	noOfAccount=0
	def setAccount(self,holderName,holderAddress,holderAccountType):
		self.name=holderName
		self.address=holderAddress
		self.accountType=holderAccountType
		self.balance=0
		account.noOfAccount+=1
		print "Your account number is : ",account.noOfAccount
	def getAccount(self):
		print "---------------------------"
		print "	  HOLDERS DATA  "
		print "---------------------------"
		print "Holders name : ",self.name
		print "Holders address : ",self.address
		print "Holders account type : ",self.accountType
		print "Balance : ",self.balance," RS"
	def deposit(self,amount):
		self.balance+=amount
	def withDraw(self,amount):
		self.balance-=amount

flag=0
inc=0
print "------------------"
print "1 --- Set your account"
print "2 --- Set yout account details"
print "3 --- Deposit money to your account"
print "4 --- Withdraw money from your account"
ch=input("Enter choice : ")
print "------------------"
while ch!=0:
	if ch==1:
		name=raw_input("Enter Holders name : ")
		address=raw_input("Enter Holders address : ")
		accountType=raw_input("Enter account type : ")
		name1=name
		name=account()
		name.setAccount(name1,address,accountType)
		inc=inc+1
		bankAccount[str(inc)]=name
		flag=1
	elif ch==2 and flag==1:
		acc=raw_input("Enter account number : ")
		if acc in bankAccount:
			bankAccount[acc].getAccount()
		else:
			print "This account does not exist !!"

	elif ch==3 and flag==1:
                acc=raw_input("Enter account number : ")
		if acc in bankAccount:
			amount=input("Enter amount : ")
			bankAccount[acc].deposit(amount)
                else:
                        print "This account does not exist !!"

	elif ch==4 and flag==1:
               	acc=raw_input("Enter account number : ")
		if acc in bankAccount:
			amount=input("Enter amount : ")
			bankAccount[acc].withDraw(amount)
		else:
                	print "This account does not exist !!"

        else:
                print "atleast one account must be created"

	print "------------------"
	print "1 --- Set your account"
	print "2 --- Set yout account details"
	print "3 --- Deposit money to your account"
	print "4 --- Withdraw money from your account"
	ch=input("Enter choice : ")
	print "------------------"
else:
	print "Bye come again!!"

