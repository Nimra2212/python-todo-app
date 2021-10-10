from todos.allTasks import task_list, display_task
from todos.createTodo import task
from todos.wrongValueHandling import enter_wrong_values


def update_task():
    try:
        while True:
            if not len(task):
                return display_task()
            elif len(task) > 0:
                task_list()
                update_task_number = input('''
Enter the task number you want to update OR type any key to select other task operations: ''')
                if update_task_number == '':
                    print("Selection can't be Empty!!! \n")
                elif not update_task_number.isdigit():
                    return enter_wrong_values("Do you want to continue choosing task (y/n)? ")
                elif update_task_number.isdigit():
                    if 0 < int(update_task_number) <= len(task):
                        update_task_or_status = input(
                            "Type 'T' to update the Task OR Type 'S' to update the Status: ").upper()
                        if update_task_or_status == 'T':
                            task_value_update = input("Enter the task to be updated! ")
                            task[int(update_task_number) - 1]['Task'] = task_value_update
                            print("Task Updated Successfully!")
                        elif update_task_or_status == 'S':
                            update_task_or_status = int(input('''
 1: To Do 
 2: In Progress 
 3: Completed 

 Choose above option to set your task status! 
''').upper())
                            if 0 < update_task_or_status <= 3:
                                if update_task_or_status == 1:
                                    task[int(update_task_number) - 1]['Status'] = 'To Do'
                                    print("Task Updated Successfully!")
                                elif update_task_or_status == 2:
                                    task[int(update_task_number) - 1]['Status'] = 'In Progress'
                                    print("Task Updated Successfully!")
                                elif update_task_or_status == 3:
                                    task[int(update_task_number) - 1]['Status'] = 'Completed'
                                    print("Task Updated Successfully!")
                            elif 0 >= update_task_or_status or update_task_or_status > 3:
                                print("You entered a wrong value, Kindly choose given status number! \n")
                        elif update_task_or_status != 'T' or update_task_or_status != 'S':
                            print("You entered a wrong value, Try again!!!\n")
                        elif update_task_or_status == '':
                            print("Selection can't be Empty!!!")
                    elif 0 >= int(update_task_number) or int(update_task_number) > len(task):
                        print("You entered a wrong value, Try again!")
    except ValueError:
        print("You entered a wrong value, Try again!")
        return update_task()
