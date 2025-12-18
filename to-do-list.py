tasks = []

while True:
    print("\n1.Add  2.View  3.Delete  4.Exit")
    choice = input("Choose: ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == '2':
        if not tasks:
            print("No tasks")
        else:
            for i, task in enumerate(tasks, 1):
                print(i, task)

    elif choice == '3':
        num = input("Task number to delete: ")
        if num.isdigit() and 1 <= int(num) <= len(tasks):
            tasks.pop(int(num) - 1)
        else:
            print("Invalid number")

    elif choice == '4':
        break

    else:
        print("Invalid option")
