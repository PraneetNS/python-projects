def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):
    if b==0:
        return "invalid division"
    return a/b

def mod(a,b):
    return a%b

while True:
        print("\n--- SIMPLE PYTHON CALCULATOR ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("enter your choice (1-5)")

        if choice == '5':
             print("Exiting Calculator")
             break
        
        if choice not in ['1','2','3','4']:
             print("Invalid Choice")
             continue
        
        try:
             num1=float(input("enter the first number"))
             num2=float(input("enter the second number"))
        except ValueError:
             print("Invalid .. Numbers Only")
             continue

        if choice == '1':
             result=add(num1,num2)
        elif choice == '2':
             result=sub(num1,num2)
        elif choice == '3':
             result=multi(num1,num2)
        elif choice == '4':
             result=div(num1,num2)

        print("Result",result)
        
             