pin="1234"
balance=10000

entered_pin=input("enter the pin")

if entered_pin!=pin:
    print("Wrong Pin")
else:
    while True:
        print("\n1.Check Balance\n2.Deposit\n3.Withdraw\n4.Exit")
        choice=input("input a choice")

        if choice=='1':
            print("Balance",balance)

        elif choice=='2':
            amt=int(input("enter amt"))
            if amt > 0:
                balance+=amt

        elif choice=='3':
            amt=int(input("enter amount"))
            if amt>balance:
                print("insufficient funds")
            else:
                balance-=amt

        elif choice=='4':
            break
        else:
            print("invalid choice")
