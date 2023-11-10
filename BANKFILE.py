
# Function to create a new account and add it to the data
def create_account():
    f = open("accounts.txt","a")
    accName = input("Enter account holder name : ")
    accNumber = input("Enter account holder number : ")
    accType = input("Enter Type of account : ")
    accBalance = input("Enter initial account balance : ")
    IFSCcode = input("Enter IFSC code : ")
    CreditCard = input("Enter Credit Card number : ")
    CVV = input("Enter CVV : ")
    EXPdate = input("Enter Expire Date : ")
    PIN = input("Enter pin : ")
    f.write("accName : " + accName + " , " + "accNumber : " + accNumber + " , " + "accType : " + accType)
    f.write(" , accBalance : " + accBalance + " , IFSCcode : " + IFSCcode + " , CreditCard : " + CreditCard)
    f.write(" , CVV : " + CVV + " , EXPdate : " + EXPdate + " , Pin : " + PIN + '\n')
    print("Account created successfully.")
    f.close()
def check_account(CreditCard):
    f = open("accounts.txt","r")
    for check in f:
        account_info = check.split(" , ")
        account = {}
        for item in account_info:
            key, value = item.split(" : ")
            account[key.strip()] = value.strip()
        if account["CreditCard"] == CreditCard:
            Pin = input("enter credit card pin :")
            if account["Pin"] == Pin:
                return account
            else:
                print("invalid pin")
    f.close()
def balance_enquiry(got_it):
    print("Account balance :", got_it["accBalance"])



#menu Card
CreditCard = input("enter credit card number :")
got_it =check_account(CreditCard)
if got_it:
    def operation():
        print("1. for balance enquirey :")
        opt = int(input("choose option : "))
        if opt == 1:
            balance_enquiry(got_it)
        else:
            print("Visit again")
        print("Continue : 1\nStop : 2")
        choice = input("choose choice: ")
        if choice == 1:
            operation()
        else:
            print('\nThank you, Visit again...')
            return
    operation()
else:
    print("Account not found")
