# Display options to the user
print("1. Create account")
print("2. Deposit")
print("3. Withdraw")
print("4. Check balance")
print("5. Exit")

# Get user's choice
choice = int(input("Enter your choice: "))

# Implement functionality based on user choice
if choice == 1:
    name = input("Enter your name: ")
    print("Hello " + name + ", your account has been successfully created.") 

elif choice == 2:
    dep = input("Enter the amount you'd like to deposit: ")
    print("You have deposited " + dep + " successfully.")

elif choice == 3:
    withdraw = input("Enter the amount you'd like to withdraw: ")
    print("You have withdrawn " + withdraw + " successfully.")

elif choice == 4:
    print("Checking balance...")  # Placeholder, assuming balance checking logic will be implemented

elif choice == 5:
    print("Exiting the system...")

else:
    print("Invalid choice. Please try again.")
