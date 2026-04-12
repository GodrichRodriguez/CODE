def withdrawal_system():
    balance = 1000  # starting balance

    while True:
        print("\n withdrawal money system")
        print("1. Withdraw Money")
        print("2. Check Balance")
        print("3. Exit")

        try:
            choice = input("Enter your choice (1-3): ")

            if choice == "1":
                try:
                    amount = float(input("Enter amount to withdraw: "))

                    if amount <= 0:
                        print("Invalid amount. Please enter a positive number.")
                    elif amount > balance:
                        print("\n❌ Insufficient funds!")

                        # Error options
                        while True:
                            print("\nWhat do you want to do?")
                            print("1. Exit")
                            print("2. Check Balance")
                            print("3. Re-enter withdrawal")

                            option = input("Choose option (1-3): ")

                            if option == "1":
                                print("Exiting program...")
                                return

                            elif option == "2":
                                print(f"Your current balance is: {balance}")

                            elif option == "3":
                                break

                            else:
                                print("Invalid option. Try again.")

                    else:
                        balance -= amount
                        print(f"✅ Withdrawal successful! New balance: {balance}")

                except ValueError:
                    print("❌ Invalid input! Please enter a numeric value.")

            elif choice == "2":
                print(f"💰 Your current balance is: {balance}")

            elif choice == "3":
                print("thank yu soo much for withdrawing ur money")
                break

            else:
                print("Invalid choice. Please select 1-3 only.")

        except Exception as e:
            print("Something went wrong:", e)


# Run the program
withdrawal_system()