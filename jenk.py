# 📝 Simple To-Do List App
# Author: Danish Saifi
# Level: Beginner | Looks Classy 😉

def show_menu():
    print("\n====== TO-DO LIST ======")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    print("========================")

tasks = []

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f"✅ '{task}' added to your list.")
        
    elif choice == "2":
        if not tasks:
            print("🕊 No tasks yet. Relax!")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")

    elif choice == "3":
        if not tasks:
            print("⚠ No tasks to remove!")
        else:
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")
            try:
                num = int(input("Enter task number to remove: "))
                removed = tasks.pop(num - 1)
                print(f"❌ '{removed}' removed.")
            except (ValueError, IndexError):
                print("⚠ Invalid choice! Try again.")

    elif choice == "4":
        print("👋 Goodbye! Stay productive.")
        break

    else:
        print("❗ Invalid option. Please try again.")
