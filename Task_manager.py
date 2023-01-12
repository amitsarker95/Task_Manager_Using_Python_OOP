from datetime import datetime
import uuid 
class Task:
    task_list = []
    def __init__(self,taskname):
        self.task_name = taskname
        self.created_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.update_time = "NA"
        self.completed_time = "NA"
        self.task_done = False
        self.id = uuid.uuid4()
        Task.task_list.append(self) 
    def __repr__(self):
        return f"ID : {self.id}\nTask Name : {self.task_name}\nCreated time : {self.created_time}\nUpdated time : {self.update_time}\nCompleted : {self.task_done}\nCompleted Time: {self.completed_time}"

    def update_task(self, new_task):
        for task in Task.task_list:
            if new_task == task.task_name:
                new_name = input("Enter new task name :")
                task.task_name = new_name
                task.update_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print("\nTask Updated Successfully.")

    def complete_task(self, new_task):
        for task in Task.task_list:
            if new_task == task.task_name:
                task.task_done = True
                task.completed_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print("\nTask Completed Successfully.\n")

    def show_incomplete_task(self):
        isValid = 0
        for task in Task.task_list:
            if task.task_done == False:
                print(task)
                print()
                isValid = 1
        if isValid == 0:
            print("There is no incomplete task.")

    def show_complete_task(self):
        isValid = 0
        for task in Task.task_list:
            if task.task_done == True:
                print(task)
                print()
                isValid = 1
        if isValid == 0:
            print("There is no task completed yet.")

    def show_task(self):
        if len(Task.task_list):
            for task in self.task_list:
                print(task)
                print()
        else:
            print("There is no task found.")



while True:
    print(f"1. Add New Task\n2. Show All Task\n3. Show Incomplete Task\n4. Show Completed Task\n5. Update Task\n6. Mark A Task Completed")
    option = int(input("Enter Option : "))
    if option == 1:
        task_name = input("Enter Task Name : ")
        task_obj = Task(task_name)
        print("Task Added Successfully.\n")
    elif option == 2:
        print()
        task_obj.show_task()
        print()
    elif option == 3:
        print()
        task_obj.show_incomplete_task()
        print()
    elif option == 4:
        print()
        task_obj.show_complete_task()
        print()
    elif option == 5:
        incomplete_task = []
        counter = 1
        for task in task_obj.task_list:
            if task.task_done == False:
                print(f"Task No : {counter}")
                counter = counter + 1
                print(task)
                print()
                incomplete_task.append(task.task_name)
        task_option = int(input("Enter task number : "))
        task_obj.update_task(incomplete_task[task_option-1])
        print()
    elif option == 6:
        is_left = False
        make_complete_task = []
        idx = 1
        for task in task_obj.task_list:
            if task.task_done == False:
                print(f"Task No : {idx}")
                idx = idx + 1
                print(task)
                make_complete_task.append(task.task_name)
                is_left = True
                print()
        if is_left == True:
            option1 = int(input("Enter task number : "))
            task_obj.complete_task(make_complete_task[option1-1])
            print()
        else:
            print("No Task to complete")
    elif option > 6:
        break
