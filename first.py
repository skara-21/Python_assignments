import random

def generate_account_number(used_account_numbers):
    prefix = "TB"
    while True:
        account_number = random.randint(0, 9999)
        new_account_number = f"{prefix}{account_number:04d}"
        if new_account_number not in used_account_numbers:
            used_account_numbers.add(new_account_number)
            return new_account_number

def create_account(data, used_account_numbers):
    name = input("Enter your name: ")
    while True:
        initial_balance_input = input("Enter your initial balance (<= 100 GEL): ")
        if initial_balance_input.isdigit():
            initial_balance = int(initial_balance_input)
            if initial_balance <= 100:
                break
            else:
                print("Your initial balance should not be more than 100 GEL. Try again!")
        else:
            print("Invalid input. Please enter a valid number for the initial balance.")

    account_number = generate_account_number(used_account_numbers)
    transfers=[] #for transfers only
    deposits=[initial_balance] #for deposits only
    transactions=['+'.join(initial_balance)] #for evrything
    account = {"name": name, "balance": initial_balance, "account_number": account_number,"transfers":transfers,"deposits":deposits,"transactions":transactions}
    data.append(account)
    print("Account created successfully!")
    print(f"Account Number: {account['account_number']}")
    return account

def deposit_money(data):
    while True:
        account_number = input("Enter your account number: ")
        account_found = False
        for account in data:
            if account['account_number'] == account_number:
                account_found = True
                break
        if not account_found:
            print("Account not found. Please enter a valid account number.")
            return
        
        while True:
            amount_input = input("Enter the amount you want to deposit: ")
            if not amount_input.isdigit():
                print("Invalid input. Please enter a valid number.")
            else:
                amount = int(amount_input)
                if amount < 0:
                    print("Please enter a positive amount.")
                else:
                    break
        for account in data:
            if account['account_number'] == account_number:
                account['balance'] += amount
                print(f"Deposited {amount} GEL successfully!")
                print(f"New Balance: {account['balance']} GEL")
                account["deposits"].append(amount)
                account["transactions"].append('+'.join(amount))
                return

def check_balance(data):
    account_number = input("Enter your account number:")
    account_found = False
    for account in data:
        if account['account_number'] == account_number:
            account_found = True
            print(f"Account Balance: {account['balance']} GEL")
            return
    if not account_found:
        print("Account not found. Please enter a valid account number.")


def transfer_money(data):
    while True:
        from_account_number = input("Enter your account number: ")
        from_account = None
        for account in data:
            if account['account_number'] == from_account_number:
                from_account = account
                break
        if from_account is None:
            print("Sender's account number not found. Please enter a valid account number.")
        else:
            break

    while True:
        to_account_number = input("Enter the recipient's account number: ")
        to_account = None
        for account in data:
            if account['account_number'] == to_account_number:
                to_account = account
                break
        if to_account is None:
            print("Recipient's account number not found. Please enter a valid account number.")
        else:
            break
    
    while True:
        amount_input = input("Enter the amount you want to transfer: ")
        if not amount_input.isdigit():
            print("Invalid input. Please enter a valid number for the amount.")
        else:
            amount = int(amount_input)
            break

    if from_account['balance'] < amount:
        print("Insufficient funds for transfer.")
        return
        
    from_account['balance'] -= amount
    to_account['balance'] += amount
    
    print(f"Transfer of {amount} GEL from {from_account_number} to {to_account_number} successful.")
    print(f"Your new balance: {from_account['balance']} GEL")
    from_account["transfers"].append(amount)
    from_account["transactions"].append('-'.join(amount))
    to_account["deposits"].append(amount)
    to_account["transactions"].append('+'.join(amount))

def get_account_details(data):
    while True:
        display_account = input("Enter account number to display details: ")
        display_account_det = None
        for account in data:
            if account["account_number"] == display_account:
                display_account_det = account
                break
        if display_account_det is None:
            print("Account number not found. Please enter a valid account number.")
        else:
            break
    print("Here are your details:")
    print("Name:",display_account_det["name"])
    print("Current balance:",display_account_det["balance"])
    print("Account number:",display_account_det["account_number"])


def print_history(data):
    while True:
        account_history = input("Enter account number to display details: ")
        account_history_det = None
        for account in data:
            if account["account_number"] == account_history:
                account_history_det = account
                break
        if account_history_det is None:
            print("Account number not found. Please enter a valid account number.")
        else:
            break
    print("What type of history do you want to see?")
    print("1.Every transaction")
    print("2.Tranfers only")
    print("3.Deposits only")
    while True:
        choice=input("Enter your choice: ")
        if choice.isdigit():
            choice=int(choice)
            break
    if choice==1:
        for transaction in account_history_det["transactions"]:
            print(transaction,'\n')
    elif choice==2:
         for tranfer in account_history_det["transfers"]:
            print(tranfer,'\n')
    elif choice==3:
         for deposit in account_history_det["deposits"]:
            print(deposit,'\n')
    
        
        
def menu():
    data = []
    used_account_numbers = set()
    
    while True:
        print("\nMenu:")
        print("1. Create bank account")
        print("2. Deposit money")
        print("3. Balance")
        print("4. Transfer money")
        print("5. Get account details")
        print("6. Get account history")
        print("7. Compute loan")
        print("8. Exit")
      
        choice = input("Enter your choice: ")

        if choice == "1":
            create_account(data, used_account_numbers)
        elif choice == "2":
            deposit_money(data)
        elif choice == "3":
            check_balance(data)
        elif choice == "4":
            transfer_money(data)
        elif choice == "5":
            get_account_details(data)
        elif choice == "6":
            print_history(data)
        elif choice=="7":
            pass
        elif choice == "8":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

print("Welcome to TBC!")
menu()
