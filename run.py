import colorama
import math
import inquirer
from tabulate import tabulate
from colorama import Fore, Back, Style
from constants import *


def welcome():
    """
    Welcome message with input request for naming of project
    """
    while True:
        print(Style.BRIGHT + "Welcome to Price Book's Wall calculator \n")
        print('We aim to provide you with order quantities.\n')
        print('Allowing you to spend more time building than ordering\n')
        print('Let us start bying giving your project a name' +
              '(1-50 characters) \n')

        input_name = input('Please enter your project name: \n')
        while (len(input_name) < 1 or len(input_name) > 50):
            print(Fore.RED + Style.BRIGHT + 'Sorry, you need to enter' +
                  ' a project name to proceed with more than 1 and' 
                  ' less than 50 characters.')
            input_name = input(Fore.BLACK +
                               'Please enter your project name: \n')

        project_name = Fore.GREEN + input_name.capitalize()
        print(f'Great you have named your Project {project_name}\n')
        break
    return True


def wall_meter_square_calc():
    """
    Calculates the total area of the wall.
    """
    while True:
        try:
            wall_length = float(input(Fore.BLACK + 'Wall Length:\n'))
            wall_height = float(input(Fore.BLACK + 'Wall height:\n'))
            break
        except ValueError:
            print(Fore.RED + Style.BRIGHT + 'Please only enter numbers')

    area = wall_length * wall_height
    print(Fore.GREEN + Style.BRIGHT + f'Great! you have {area} m2\n')
    return area, wall_length


def get_stud_quantities(wall_length):
    """
    Calculates the amount of frame work required to build a wall.
    """

    print(Fore.BLACK + tabulate(stud_table, stud_headers, tablefmt='github\n'))

    while True:
        try:
            stud = int(input(Fore.BLACK + 'Choose a stud ref from the table above:'
                         + '\n'))
            if stud >= 1 and stud <= 7:
                zero_index_stud = int(stud)-1
                centers_answers = inquirer.prompt(centers)
                cntrs = centers_answers['centers']
                break
            else:
                raise ValueError
        except ValueError:
            print(Fore.RED + Style.BRIGHT + 'Please only enter numbers'+
            ' shown on the list above')

        
    while True:
        """
        Calculates additional studs required in wall per door frame  
        """
        try:
            doors = float(input(Fore.BLACK + 'How many doors are in the wall?'
                                + '\n'))
            break
        except ValueError:
            print(Fore.RED + Style.BRIGHT + 'Please only enter numbers')
    while True:
        """
        Calculates additional studs required in wall per corner  
        """
        try:
            corners = float(input(Fore.BLACK +
                                  'How many corners are there?\n'))
            break
        except ValueError:
            print(Fore.RED + Style.BRIGHT + 'Please only enter numbers')

    studs = math.ceil(wall_length/cntrs)
    number_studs = studs + doors + corners
    print(Fore.GREEN + Style.BRIGHT + f'You need {number_studs} studs' +
                       f' and {wall_length * 2}lm of tracks\n')


def get_insulations_quantites(wall_area):
    """
    Provide the option of insulation and total m2 required
    """

    insulated_answers = inquirer.prompt(insulation)
    insulated = insulated_answers['insulation']
    print(Fore.GREEN + f'You have chosen {insulated}!')

    if insulated == "Yes":
        print(Fore.GREEN + Style.BRIGHT + f'You need {wall_area} m2 of insulation\n')
    if insulated == "No":
        print(Fore.GREEN + Style.BRIGHT + 'No insulation')


def get_wall_linings_quantities(wall_area, wall_length):
    """
    Provide the m2 and number of boards required to be ordered.
    """

    linings_answer = inquirer.prompt(linings)
    lngs_answr = linings_answer['linings']
    if lngs_answr == 'Yes':
        lining_quants = lining_options()
        total_linings_wall = lining_quants * wall_area
        print(Fore.GREEN + Style.BRIGHT + f' You need {total_linings_wall}m2' +
                           f' or {math.ceil(total_linings_wall/2.88)}' +
                           ' total number of boards' +
                           f' in total and {wall_area}m2 per layer' +
                           f' or {math.ceil(wall_area/2.88)} number of boards per layer')
        print(Fore.BLACK +
          tabulate(lining_table, lining_headers, tablefmt='github\n'))

   
    if lngs_answr == 'No':
        print(Fore.GREEN + Style.BRIGHT + + 'No wall linings needed')


def lining_options():
    """
    Show the common differing types of wall linings and record the choice
    """
    while True:
        try:
            lining_choices = input(Fore.BLACK +
                                   'How many linings would you like?' +
                                   '(Please choose upto 6 linings):\n')
            numberoflinings = int(lining_choices)
            if numberoflinings >= 1 and numberoflinings <= 6:
                print(numberoflinings)
                return numberoflinings
            else:
                raise ValueError
        except ValueError:
            print(Fore.RED + Style.BRIGHT + 'Sorry, please choose a number between 1 and 6')


def main():
    """
    Run all program functions
    """
    welcome()
    
    print(Fore.BLACK + 'Now let us enter your wall dimensions\n')
    wall_area, wall_length = wall_meter_square_calc()

    get_stud_quantities(wall_length)

    get_insulations_quantites(wall_area)

    get_wall_linings_quantities(wall_area, wall_length)

main()