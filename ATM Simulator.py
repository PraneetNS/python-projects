balance = 5000
pin = "1234"

entered_pin = input("Enter PIN: ")

if entered_pin != pin:
    print("Wrong PIN")
else:
    while True:
        print("\n1.Check Balance\n2.Deposit\n3.Withdraw\n4.Exit")
        choice = input("Choose: ")

        if choice == '1':
            print("Balance:", balance)

        elif choice == '2':
            amt = int(input("Amount: "))
            if amt > 0:
                balance += amt

        elif choice == '3':
            amt = int(input("Amount: "))
            if amt > balance:
                print("Insufficient funds")
            else:
                balance -= amt

        elif choice == '4':
            break

        else:
            print("Invalid choice")
