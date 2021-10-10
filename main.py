from todos.createTodo import add_todo
from todos.updateTodo import update_task
from todos.removeTodo import remove_task
from todos.allTasks import display_task


while True:
    try:
        user_task_selection = int(input(f'''
1: Add New Tasks 
2: List All Current Tasks 
3: Update Tasks 
4: Delete tasks 
Enter option number you want to perform:     
'''))
        if 1 > user_task_selection or user_task_selection > 4:
            print("You entered a wrong number, Kindly select from the above numbers!")
        else:
            if user_task_selection == 1:
                if add_todo() != 'y':
                    break
            elif user_task_selection == 2:
                if display_task() != 'y':
                    break
            elif user_task_selection == 3:
                if update_task() != 'y':
                    break
            elif user_task_selection == 4:
                if remove_task() != 'y':
                    break
    except ValueError:
        print("\n You entered a wrong value, Kindly select from the above numbers!")