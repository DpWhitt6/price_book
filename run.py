import colorama
from colorama import Fore, Back, Style

import math

from tabulate import tabulate
lining_headers = ['Ref','Linings','Thickness','m2','Cost']
lining_table = [[1,'Plasterboard - Std','12.5mm',2.88,25],[2,'Plasterboard - Std','15mm',2.88,35],\
    [3,'Plasterboard - Fire','12.5mm',2.88,40],[4,'Plasterboard - Fire','15mm',2.88,45],\
        [5,'Plywood','8mm',2.88,55],[6,'Plywood','12mm',2.88,65],[7,'Plywood','18mm',2.88,75]]

stud_headers= ['Ref', 'Material', 'Thickness', 'Cost m2']
stud_table = [[1,'Timber','50mm',7],[2,'Timber','70mm',8.5],[3,'Timber','90mm',10],\
    [4,'Timber','150mm',12.5],[5,'Steel','70mm',7],[6,'Steel','90mm',8.5],[7,'Steel','146mm',12.5]]

import inquirer
centers = [
    inquirer.List('centers', message='What centers do you require (m)?',\
        choices=[0.3,0.45,0.6]),
]
insulation = [
    inquirer.List('insulation',message='Do you want insulation?',\
        choices=['Yes','No']),
]
linings = [
    inquirer.List('linings',message='Add a lining?',\
        choices=['Yes','No']),
]

#print(tabulate(lining_table,lining_headers,tablefmt="github"))

#print(tabulate(centers_table,centers_headers,tablefmt='github'))

def welcome():
    """
    Welcome message with input request for naming of project
    """
    while True:
        print(Style.BRIGHT + "Welcome to Price Book's Wall calculator \n")
        print('We aim to provide you with market rates (Average rates) and order quantities.\n')
        print('Allowing you to spend more time building than quoting\n')  
        print('Let us start bying giving your project a name (1-50 characters) \n')
        
        input_name = input('Please enter your project name: \n') 
        while (len(input_name)<1 or len(input_name) >50):
            print(Fore.RED + Style.BRIGHT + 'Sorry, you need to enter a project name to proceed.')
            input_name = input(Fore.BLACK + 'Please enter your project name: \n')
            
        project_name = Fore.GREEN + input_name.capitalize()
        print(f'Great you have named your Project {project_name}\n')
        break
    return True 

def wall_build_up():
 
    while True:
        cost=[]

        print(Fore.BLACK + 'Now let us enter your wall dimensions\n')
        wall_area, wall_length = meter_square_calc()

            
        print(Fore.GREEN +f'Great! you have {wall_area} m2\n')
        
        stud_calc,cost_of_studs = stud_selector()
        
        centers_answers = inquirer.prompt(centers)
        cntrs= centers_answers['centers']
        while True:
            try:
                doors = float(input(Fore.BLACK +'How many doors are in the wall?\n'))
                corners = float(input(Fore.BLACK +'How many corners are there?\n'))
                break
            except ValueError:
                print(Fore.RED + Style.BRIGHT +'Please enter numbers only')

        studs = math.ceil(wall_length/cntrs)
        number_studs = studs+doors+corners
        print(Fore.GREEN + f'You need {number_studs} studs and {wall_length * 2}lm of tracks\n')
        cost.insert(1,f'Studs estimate = £{float(cost_of_studs*wall_area)}')

        insulated_wall,cost_of_insulation = insulations()
        if insulated_wall == "Yes":
            print(Fore.GREEN + f'You need {wall_area} m2 of insulation\n')
            cost.insert(1,f'Insulation estimate = £{float(cost_of_insulation*wall_area)}')
        if insulated_wall == "No":
            print('no insulation')

        lining_quants =  wall_linings()
        total_linings_wall = lining_quants * wall_area
        print(Fore.GREEN + f' You need {total_linings_wall}m2 or {total_linings_wall/2.88} total number of boards in total and {wall_area}m2 per layer or {wall_area/2.88} number of boards per layer')
        break
            

def meter_square_calc():
    while True:
        try:
            wall_length = float(input(Fore.BLACK + 'Wall Length: \n'))
            wall_height = float(input(Fore.BLACK +'Wall height: \n'))
            break
        except ValueError:
            print(Fore.RED + Style.BRIGHT +'Please only enter numbers')

    area = wall_length * wall_height
    return area,wall_length

def stud_selector():
    
    print(Fore.BLACK + tabulate(stud_table,stud_headers,tablefmt='github\n'))
    
    while True:
        try:
            stud = input(Fore.BLACK + 'Choose a stud ref from the table above: \n')
            zero_index_stud = int(stud)-1
            cost_of_stud = float(stud_table[zero_index_stud][3])
            return stud,cost_of_stud
        except ValueError:
            print(Fore.RED + Style.BRIGHT +'Please only enter numbers')
        

def insulations():
    insulated_answers = inquirer.prompt(insulation)
    insulated = insulated_answers['insulation']
    cost_of_insulation = 5.5

    print(Fore.GREEN + f'You have chosen {insulated}!')
    return insulated,cost_of_insulation

def wall_linings():
    
    linings_answer = inquirer.prompt(linings)
    lngs_answr = linings_answer['linings']
    if lngs_answr == 'Yes':
        lining_quants = lining_options()
    
    print(Fore.BLACK + tabulate(lining_table,lining_headers,tablefmt='github\n'))
    if lngs_answr == 'No':
        print(Fore.GREEN + 'No wall linings needed')
    return lining_quants
   

    
def lining_options():
 # to be reviewed 
    while True: 
        try:
            lining_choices = input(Fore.BLACK +'How many linings would you like? (Please choose upto 6 linings):' )
            numberoflinings = int(lining_choices)
            numberoflinings <1 and numberoflinings >6
            print(numberoflinings)
            return numberoflinings
        except ValueError:
            print(Fore.RED + 'Sorry, please choose a number between 1 and 6')

    

"""
TO DO:
Add invalid input for naming purposes - Limit the number of characters
Add invalid input for numbers only 
Add function to loop through tabulate to return columns related to 
    reference 
Use above function to cycle through Stud, Linnings and centers table.
Add input options for number of doors and corners in the wall 
Create a table that takes the users inputs to be displayed at the end 
    i.e. Stud type|Amount needed|Anticpated Cost
          Linings |Amount needed|Anticpated Cost
"""



        
def main():
    """
    Run all program functions
    """
    welcome()
    wall_build_up()

main()