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
        print('We aim to provide you with market rates (Average rates)' +
              'order quantities.\n')
        print('Allowing you to spend more time building than quoting\n')
        print('Let us start bying giving your project a name' +
              '(1-50 characters) \n')

        input_name = input('Please enter your project name: \n')
        while (len(input_name) < 1 or len(input_name) > 50):
            print(Fore.RED + Style.BRIGHT + 'Sorry, you need to enter' +
                  'a project name to proceed.')
            input_name = input(Fore.BLACK +
                               'Please enter your project name: \n')

        project_name = Fore.GREEN + input_name.capitalize()
        print(f'Great you have named your Project {project_name}\n')
        break
    return True


def wall_build_up():

    print(Fore.BLACK + 'Now let us enter your wall dimensions\n')
    wall_area, wall_length = wall_meter_square_calc()

    print(Fore.GREEN + f'Great! you have {wall_area} m2\n')

    get_stud_quantities(wall_length)

    get_insulations_quantites(wall_area)

    get_wall_linings_quantities(wall_area, wall_length)


def wall_meter_square_calc():
    while True:
        try:
            wall_length = float(input(Fore.BLACK + 'Wall Length:\n'))
            wall_height = float(input(Fore.BLACK + 'Wall height:\n'))
            break
        except ValueError:
            print(Fore.RED + Style.BRIGHT + 'Please only enter numbers')

    area = wall_length * wall_height
    return area, wall_length


def get_stud_quantities(wall_length):

    print(Fore.BLACK + tabulate(stud_table, stud_headers, tablefmt='github\n'))

    while True:
        try:
            stud = input(Fore.BLACK + 'Choose a stud ref from the table above:'
                         + '\n')
            zero_index_stud = int(stud)-1
            centers_answers = inquirer.prompt(centers)
            cntrs = centers_answers['centers']
            break
        except ValueError:
            print(Fore.RED + Style.BRIGHT + 'Please only enter numbers')
    while True:
        try:
            doors = float(input(Fore.BLACK + 'How many doors are in the wall?'
                                + '\n'))
            break
        except ValueError:
            print(Fore.RED + Style.BRIGHT + 'Please only enter numbers')
    while True:
        try:
            corners = float(input(Fore.BLACK +
                                  'How many corners are there?\n'))
            break
        except ValueError:
            print(Fore.RED + Style.BRIGHT + 'Please only enter numbers')

    studs = math.ceil(wall_length/cntrs)
    number_studs = studs + doors + corners
    print(Fore.GREEN + f'You need {number_studs} studs' +
                       'and {wall_length * 2}lm of tracks\n')


def get_insulations_quantites(wall_area):

    insulated_answers = inquirer.prompt(insulation)
    insulated = insulated_answers['insulation']
    print(Fore.GREEN + f'You have chosen {insulated}!')

    if insulated == "Yes":
        print(Fore.GREEN + f'You need {wall_area} m2 of insulation\n')
    if insulated == "No":
        print('no insulation')


def get_wall_linings_quantities(wall_area, wall_length):

    linings_answer = inquirer.prompt(linings)
    lngs_answr = linings_answer['linings']
    if lngs_answr == 'Yes':
        lining_quants = lining_options()
        total_linings_wall = lining_quants * wall_area
        print(Fore.GREEN + f' You need {total_linings_wall}m2' +
                           f' or {total_linings_wall/2.88}' +
                           'total number of boards' +
                           f' in total and {wall_area}m2 per layer' +
                           ' or {wall_area/2.88} number of boards per layer')

    print(Fore.BLACK +
          tabulate(lining_table, lining_headers, tablefmt='github\n'))
    if lngs_answr == 'No':
        print(Fore.GREEN + 'No wall linings needed')


def lining_options():
    while True:
        try:
            lining_choices = input(Fore.BLACK +
                                   'How many linings would you like?' +
                                   '(Please choose upto 6 linings):')
            numberoflinings = int(lining_choices)
            if numberoflinings > 1 and numberoflinings < 6:
                print(numberoflinings)
                return numberoflinings
            else:
                raise ValueError
        except ValueError:
            print(Fore.RED + 'Sorry, please choose a number between 1 and 6')


def main():
    """
    Run all program functions
    """
    welcome()
    wall_build_up()


main()
