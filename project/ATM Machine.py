import random


class Account:
    # Construct an Account object
    def __init__(self, id, balance=0, annualInterestRate=3.4):
        self.userid = id
        self.balance = balance
        self.annualInterestRate = annualInterestRate

    def getId(self):
        return self.userid

    def getBalance(self):
        return self.balance

    def getAnnualInterestRate(self):
        return self.annualInterestRate

    def getMonthlyInterestRate(self):
        return self.annualInterestRate / 12

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def getMonthlyInterest(self):
        return self.balance * self.getMonthlyInterestRate()


def main():
    print("****************************************************************************")
    print("*                                                                          *")
    print("*                   Welcome to IT SOURCECODE ATM SYSTEM                    *")
    print("*                                                                          *")
    print("****************************************************************************")
    # Creating accounts
    accounts = []
    for i in range(1000, 9999):
        account = Account(i, 0)
        accounts.append(account)

    # ATM Processes
    while True:

        # Reading id from user
        id = int(input("\nEnter account pin: "))

        # Loop till id is valid
        while id < 1000 or id > 9999:
            print('----------------')
            print('****************')
            print('  INVALID  PIN  ')
            print('****************')
            print('----------------')
            id = int(input("\nRe-enter: "))

        # Iterating over account session
        while True:

            # Printing menu
            print("\n1 - View Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Exit ")

            accountobj = account

            # Reading selection
            selection = int(input("\nEnter your selection: "))

            # Getting account object
            for acc in accounts:
                # Comparing account id
                if acc.getId() == id:
                    accountobj = acc
                    break

            # View Balance
            if selection == 1:
                # Printing balance
                print(accountobj.getBalance())

            # Withdraw
            elif selection == 2:
                # Reading amount
                amt = float(input("\nEnter amount to withdraw: "))
                ver_withdraw = input("Is this the correct amount, Yes or No ? " + str(amt) + " ")

                if ver_withdraw == "yes":
                    print("Verify withdraw")
                else:
                    break

                if amt < accountobj.getBalance():
                    # Calling withdraw method
                    accountobj.withdraw(amt)
                    # Printing updated balance
                    print("\nUpdated Balance: " + str(accountobj.getBalance()) + " n")
                else:
                    print("\nYou're balance is less than withdrawl amount: " + str(accountobj.getBalance()) + " n")
                    print("\nPlease make a deposit.")

            # Deposit
            elif selection == 3:
                # Reading amount
                amt = float(input("\nEnter amount to deposit: "))
                ver_deposit = input("Is this the correct amount, Yes, or No ? " + str(amt) + " ")

                if ver_deposit == "yes":
                    # Calling deposit method
                    accountobj.deposit(amt)
                    # Printing updated balance
                    print("\nUpdated Balance: " + str(accountobj.getBalance()) + " n")
                else:
                    break

            elif selection == 4:
                print("nTransaction is now complete.")
                print("Transaction number: ", random.randint(10000, 1000000))
                print("Current Interest Rate: ", accountobj.annualInterestRate)
                print("Monthly Interest Rate: ", accountobj.annualInterestRate / 12)
                print("Thanks for choosing us as your bank")
                exit()

            # Any other choice
            else:
                print("nThat's an invalid choice.")


# Main function
main()
