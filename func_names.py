"""

This script create a new name for the step function
For this enter a discription of the step from file.feature

"""

while True:

    step_name = input('(press q for quit) \n' + 'Input step name for create new name function: ')

    new_name_func = step_name.strip().lower().replace(' ', '_')

    print('\n \n \n' + new_name_func + '\n \n \n')

    if new_name_func == 'q' or new_name_func == 'quit':
        break
