class Todo:
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        print("Current Tasks:")
        for i, task in enumerate(self.tasks):
            print(f"{i+1}. {task}")
        print("Completed Tasks:")
        for i, task in enumerate(self.completed_tasks):
            print(f"{i+1}. {task}")

    def complete_task(self, task_num):
        task = self.tasks.pop(task_num-1)
        self.completed_tasks.append(task)

    def delete_task(self, task_num):
        del self.tasks[task_num-1]


def main():
    todo = Todo()

    while True:
        print("\n1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            task = input("Enter task: ")
            todo.add_task(task)
        elif choice == '2':
            todo.view_tasks()
        elif choice == '3':
            task_num = int(input("Enter task number to complete: "))
            todo.complete_task(task_num)
        elif choice == '4':
            task_num = int(input("Enter task number to delete: "))
            todo.delete_task(task_num)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == '__main__':
    main()
