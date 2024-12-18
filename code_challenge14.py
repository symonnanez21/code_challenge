has_account = False
running = True
import os

bal = 0

def deposit_money():
    global bal
    os.system('cls')
    amount = eval(input("How much would you like to deposit?"))

    tsun = amount // 1000
    tsun2 = amount % 1000
    fhun = tsun2 // 500
    fhun2 = tsun2 % 500
    thun = fhun2 // 200
    thun2 = fhun2 % 200
    ohun = thun2 // 100
    ohun2 = thun2 % 100
    fifty = ohun2 // 50
    fifty2 = ohun2 % 50
    bente = fifty2 // 20
    bente2 = fifty2 % 20
    ten = bente2 // 10
    ten2 = bente2 % 10
    payb = ten2 // 5
    payb2 = ten2 % 5
    wan = payb2 // 1
    wan2 = payb2 % 1

    os.system('cls')
    print("Filipino denominations of the amount you would like to deposit is as follows:")
    print(f"1000 = {tsun}")
    print(f"500 = {fhun}")
    print(f"200 = {thun}")
    print(f"100 = {ohun}")
    print(f"50 = {fifty}")
    print(f"20 = {bente}")
    print(f"10 = {ten}")
    print(f"5 = {payb}")
    print(f"1 = {wan}")
    print(f"Amount entered: {amount}")

    choice1 = input("Would you like to deposit the amount? (YES or NO)")
    if choice1.lower() == "yes":
        os.system('cls')
        bal += amount
        print(f"You have successfully deposited {amount} pesos.")
        bla = input("Plese enter 'OK' to continue.")
        return bal
    elif choice1.lower() == "no":
        os.system('cls')
        print("Deposit session has ended.")
        print()
        return bal

def check_balance():
    os.system('cls')
    print(f"Your total balance is {bal} pesos.")
    bla = input("Plese enter 'OK' to continue.")

def withdraw_money():
    global bal
    os.system('cls')
    amount = eval(input("How much would you like to withdraw? "))
    if amount >= bal:
        print(f"Withdraw amount must not be greater than the available balance {bal}.")
        print(f"Amount entered: {amount}")
        bla = input("Plese enter 'OK' to continue.")
    elif amount == bal or amount <= bal:
        bal -= amount
        os.system('cls')
        print(f"{amount} has been successfully withdrawn, your current balance is now {bal}.")
        bla = input("Plese enter 'OK' to continue.")
        return bal
    else:
        print("Invalid input.")
        print()

while running == True:
    os.system('cls')
    print("Welcome to JERB Bank Services")
    if has_account == False:
        os.system('cls')
        sign_in = input("You will need to create an account in order use our services.\nWould you like to create an account? (YES or NO)")
        if sign_in.lower() == "yes":
            os.system('cls')
            print("Account Sign Up")
            print()
            name = input("Please enter your name. ")
            password = input("Create your own password. ")
            pass_confirm = input("Re-enter your password. ")
            if pass_confirm == password :
                os.system('cls')
                print("Account successfully created")
                has_account = True
                bla = input("Plese enter 'OK' to continue.")
        elif sign_in.lower() == "no":
            print("Thank you for using our system.")
            running = False
            break

    elif has_account == True:
        while running == True:
            os.system('cls')
            print("Please login your account to access our services.")
            whatname = input("Name: ")
            if whatname == name:
                whatpass = input("Password: ")
                if whatpass == password:
                    while running == True:
                        os.system('cls')
                        print(f"Hi {name}! What would you like to do for today?")
                        print("1. Check balance")
                        print("2. Deposit money")
                        print("3. Withdraw money")
                        print("4. End program")
                        choice = input("")
                        if choice == "1":
                            check_balance()
                        elif choice == "2":
                            deposit_money()
                        elif choice == "3":
                            withdraw_money()
                        elif choice == "4":
                            os.system('cls')
                            print("Thank you for using our services.")
                            running = False
                            break
                elif whatpass != password:
                    os.system('cls')
                    print("Incorrect password.")
                    bla = input("Plese enter 'OK' to continue.")
            elif whatname != name:
                os.system('cls')
                print("Account name does not exist.")
                bla = input("Plese enter 'OK' to continue.")