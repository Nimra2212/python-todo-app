from todos.wrongValueHandling import enter_wrong_values
from todos.allTasks import task_list, display_task
from todos.createTodo import task


def remove_task():
    while True:
        if not len(task):
            return display_task()
        elif len(task) > 0:
            task_list()
            task_remove_number = input('''
Enter the task number which you want to delete OR any key to perform other task operation: 
''')
            if not task_remove_number.isdigit():
                return enter_wrong_values("Do you want to continue choosing task (y/n)? ")
            elif 0 < int(task_remove_number) <= len(task):
                task.pop(int(task_remove_number) - 1)
                print("Task Removed Successfully!")
            elif 0 >= int(task_remove_number) or int(task_remove_number) > len(task):
                print("You entered a wrong value, Kindly choose a given task number to delete Task! \n ")
