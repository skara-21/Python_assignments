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
        initial_balance = int(input("Enter your initial balance (<= 100 GEL): "))
        if initial_balance > 100:
            print("Your initial balance should not be more than 100 GEL. Try again!")
        else:
            break

    account_number = generate_account_number(used_account_numbers)
    account = {"name": name, "balance": initial_balance, "account_number": account_number}
    data.append(account)
    print("Account created successfully!")
    print(f"Account Number: {account['account_number']}")
    return account

def menu():
    data = []
    used_account_numbers = set()
    
    while True:
        print("\nMenu:")
        print("1. Create bank account")
        print("2. Balance")
        print("3. Transfer money")
        print("4. Other options (placeholder)")
        print("5. Other options (placeholder)")
        print("6. Other options (placeholder)")
        print("7. Exit")
      
        choice = input("Enter your choice: ")

        if choice == "1":
            create_account(data, used_account_numbers)
        elif choice == "2":
            pass  
        elif choice == "3":
            pass  
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

print("Welcome to TBC!")
menu()
