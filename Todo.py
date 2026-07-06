tasks = []
while True:
    print("\n---TO-D0-LIST ---")
    print("1. Add task")
    print("2. View tasks you have added")
    print("3. Remove task")
    print("4. Exit")
    choice= input("Enter what you have decided:")

    if choice =="1":
        task = input("Enter a very new task:")
        tasks.append(task)
        print("Task successfully added")

    elif choice == "2":
        print("\n your tasks:")
        if len(tasks)==0:
            print("No tasks yet")
        else:
            for i in range(len(tasks)):
                print(i+1, "-", tasks[i])
    elif choice =="3":
        # show tasks first
        print("\n your tasks:")
        if len(tasks) == 0:
            print("No tasks yet")
        else:
            for i in range(len(tasks)):
                print(i+1, "-", tasks[i])
        try:
            task_number = int(input("Enter the number of the task you want to remove:"))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' has been removed.")
        else:
            print("Invalid task number. Please try again.")

    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
        continue