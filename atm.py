balance = 1000000
chance = 0
correct_pin = False
print("---------------------------------")
print("Welcome to Gt bank")
print("kindly insert your card")
print("----------------------------------")
print("Enter your 4 digit password")
while chance <= 3:
    pin = input()
    if pin.isdigit() == True and len(str(pin)) == 4:
        print("correct password")
        print("Enjoy your transaction")
        correct_pin = True
    else:
        print("wrong password")
        print("Try again")
        chance += 1
    while correct_pin == True:
        print("What transaction will you like to perform")
        print("1. Balance Enquiry \n 2.Transfer \n 3. Withdraw \n 4. End")
        print("pick any of 1, 2, 3 or 4 😉")
        value = int(input())
        if value == 1:
            print("Your  total balance is",balance)
            input()
        elif value == 2:
            print("how much will you like to transfer")
            transfer_amt = int(input("Enter amount: "))
            if transfer_amt >= balance:
                print("Insufficient Funds")
                input()
            else:
                print("Transaction successful")
                balance += transfer_amt
                print("your balance is now", balance)
                input()
        elif value == 3:
            print("How much will you like to withdraw")
            with_amt = int(input("Enter the amount you wish to withdraw: "))
            if with_amt > balance:
                print("Insufficient funds")
                input()
            else:
                print("Transaction successful")
                balance -= with_amt
                print("your balance is now", balance)
                input()
        elif value == 4:
            print("Thank you for banking with us....")
            quit()
        else:
            print("Invalid syntax")
            print("Try again")
            input()


