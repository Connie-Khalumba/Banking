from cardHolder import CardHolder

def print_menu():
    print("\nWelcome to the Credit Card Processing System! Please choose one of the following options...")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")

def deposit(cardHolder):
    try:
        deposit_amount = float(input("How much money would you like to deposit: "))
        cardHolder.set_balance(cardHolder.get_balance() + deposit_amount)
        print(f"Thank you for your deposit. Your new balance is: {cardHolder.get_balance()}")
    except ValueError:       
        print("Invalid amount")

def withdraw(cardHolder):
    try:
        withdraw_amount = float(input("How much money would you like to withdraw: "))
        ### Check if user has money
        if cardHolder.get_balance() < withdraw_amount:
            print("Insufficient balance :(")
        else:
            cardHolder.set_balance(cardHolder.get_balance() - withdraw_amount)
            print("You're good to go! Thank you :)")
    except ValueError:
        print("Invalid amount")

def check_balance(cardHolder):
    print("Your current balance is: ", cardHolder.get_balance())

if __name__ == "__main__":
    current_user = CardHolder("", "", "", "", 0.0)

    #### Create a repository of cardholders
    list_of_cardHolders = []
    list_of_cardHolders.append(CardHolder("124589012316", 1234, "John", "Doe", 160.31))
    list_of_cardHolders.append(CardHolder("124589012317", 1234, "Jane", "Doe", 160.31))
    list_of_cardHolders.append(CardHolder("562314908271", 5678, "Jane", "Smith", 210.45))
    list_of_cardHolders.append(CardHolder("983746512890", 9876, "Alice", "Johnson", 530.89))
    list_of_cardHolders.append(CardHolder("673451928374", 4321, "Bob", "Williams", 345.22))
    list_of_cardHolders.append(CardHolder("098765432198", 8765, "Charlie", "Brown", 100.00))

    ### Prompt user for debit card number
    while True:
        try:
            debitCardNum = input("Please insert your debit card number: ")
            ### Check against repository
            debitMatch = [holder for holder in list_of_cardHolders if holder.get_cardNum() == debitCardNum]
            if len(debitMatch) > 0:
                current_user = debitMatch[0]
                break
            else:
                print("Invalid card number. Please try again")
        except:
            print("Invalid card number. Please try again")

    ### Prompt for PIN
    while True:
        try:
            # Prompt the user to input their PIN
            userPin = int(input("Please enter your PIN: ").strip())

            ### Check against the cardholder's PIN
            if current_user.get_pin() == userPin:
                print("PIN accepted.")
                break  # Exit the loop if the PIN is correct
            else:
                print("Invalid PIN. Please try again.")
        except ValueError:
            # Handle non-integer inputs
            print("Invalid PIN format. Please enter a numerical PIN.")

    ### Print options
    print("Welcome ", current_user.get_firstname(), "  :)")
    option = 0
    while True:
        print_menu()
        try:
            option = int(input())
        except ValueError:
            print("Invalid input. Please try again")
            continue  # Skip the rest of the loop iteration

        if option == 1: 
            deposit(current_user)
        elif option == 2:
            withdraw(current_user)
        elif option == 3:
            check_balance(current_user)
        elif option == 4:  # Adjusted to match the menu option
            break
        else:
            print("Invalid option. Please try again.")

    print("Thank you, Have a nice day :)")
