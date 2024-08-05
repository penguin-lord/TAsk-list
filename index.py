import os

class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def complete_task(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"{self.description} - {status}"

class TaskList:
    def __init__(self, filename="tasks.txt"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{description}' added.")

    def complete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number].complete_task()
            self.save_tasks()
            print(f"Task '{self.tasks[task_number].description}' marked as completed.")
        else:
            print("Invalid task number.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task.description}|{task.completed}\n")

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                for line in file:
                    description, completed = line.strip().split('|')
                    self.tasks.append(Task(description, completed == 'True'))

def main():
    task_list = TaskList()
    while True:
        print("\nTask List Menu:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. View Tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter the task description: ")
            task_list.add_task(description)
        elif choice == '2':
            task_number = int(input("Enter the task number to complete: ")) - 1
            task_list.complete_task(task_number)
        elif choice == '3':
            task_list.view_tasks()
        elif choice == '4':
            print("Exiting the Task List program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
