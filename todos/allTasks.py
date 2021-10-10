from todos.wrongValueHandling import enter_wrong_values
from todos.createTodo import task, add_task_again


def task_list():
    index = 1
    for item in task:
        print(f"{index}: {item.get('Task')} ({item.get('Status')}) Created on: {item.get('Date')}")
        index += 1


def display_task():
    if not task:
        return add_task_again('''
Task list is empty! Type 'T' to enter a new task OR any key to perform other task operations: ''')
    elif len(task) > 0:
        task_list()
        return enter_wrong_values('\n Do you want to continue selecting task (y/n)? ')
