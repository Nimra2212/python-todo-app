
from todos.wrongValueHandling import enter_wrong_values
from datetime import datetime

task = []


def add_todo():
    while True:
        todo = input("Enter Your Task: ")
        if not todo:
            print('Task Cant be Empty!')
        else:
            new_todo = {'Task': todo, 'Status': 'To Do', 'Date': datetime.today().strftime('%Y-%m-%d')}
            task.append(new_todo)
            print('Tasked Saved Successfully!')
            return add_task_again("Type 'T' to enter a new task OR any key to perform other task: ")


def add_task_again(value):
    enter_new_task = input(value).upper()
    if enter_new_task == 'T':
        return add_todo()
    elif enter_new_task == '':
        print("Selection can't be Empty!!!")
        return add_task_again("Type 'T' to enter a new task OR any key to perform other task: ")
    elif enter_new_task != 'T':
        return enter_wrong_values("Do you want to continue choosing task (y/n)? ")
