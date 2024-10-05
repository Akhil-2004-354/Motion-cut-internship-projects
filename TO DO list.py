# TO DO LIST
import json
import os

class TaskManager:
    def __init__(self, file_name='tasks.json'):
        self.file_name = file_name
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                return json.load(file)
        else:
            return []

    def save_tasks(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.tasks, file)

    def add_task(self, description):
        task = {'description': description, 'complete': False}
        self.tasks.append(task)
        self.save_tasks()

    def edit_task(self, index, description):
        if index < len(self.tasks):
            self.tasks[index]['description'] = description
            self.save_tasks()

    def delete_task(self, index):
        if index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()

    def mark_complete(self, index):
        if index < len(self.tasks):
            self.tasks[index]['complete'] = True
            self.save_tasks()

    def display_tasks(self):
        for index, task in enumerate(self.tasks):
            status = 'Complete' if task['complete'] else 'Incomplete'
            print(f"{index+1}. {task['description']} ({status})")


def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. Mark Complete")
        print("5. Display Tasks")
        print("6. Quit")

        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            task_manager.add_task(description)
        elif choice == '2':
            index = int(input("Enter task number: ")) - 1
            description = input("Enter new description: ")
            task_manager.edit_task(index, description)
        elif choice == '3':
            index = int(input("Enter task number: ")) - 1
            task_manager.delete_task(index)
        elif choice == '4':
            index = int(input("Enter task number: ")) - 1
            task_manager.mark_complete(index)
        elif choice == '5':
            task_manager.display_tasks()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
