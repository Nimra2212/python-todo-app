

def enter_wrong_values(value):
    while True:
        user_entered_value = input(f"{value}").lower()
        if user_entered_value == 'n':
            return 'n'
        elif user_entered_value == 'y':
            return 'y'
        elif user_entered_value != 'n' and user_entered_value != 'y':
            print("You entered a wrong value! \n")
