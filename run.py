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

centers_headers = ['Ref','Stud Centers','M']
centers_table = [[1,'300mm',0.3],[1,'450mm',0.45],[1,'600mm',0.6]]


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
        print('Let us start bying giving your project a name (Atleast 1 character) \n')
        
        input_name = input('Please enter your project name: \n') 
        while (input_name) < str(1):
            print('Sorry, you need to enter a project name to proceed.')
            input_name = input('Please enter your project name: \n')
            
        project_name = Fore.GREEN + input_name.capitalize()
        print(f'Great you have named your Project {project_name}\n')
        break
    return True 

def calc_wall(welcome):
    """
    User to input two measurements Length and Height (Max height: 10m)
    output to be L X H = M2 
    """
    while True:
        print(Fore.BLACK + 'Now let us enter your wall dimensions\n')

        wall_length = input('Wall Length: \n')
        wall_height = input('Wall height: \n')

        x=float(wall_length)
        y=float(wall_height)

        sqrd_m = x * y

        #class wall_dimensions:
         #   def m() = sqrd_m:


        print(f'Great! you have {sqrd_m} m2\n')
        
        print(tabulate(stud_table,stud_headers,tablefmt='github\n'))
        stud = input('Choose a stud ref from the table above: \n')
        #for s in range(len(stud_table.column(1))):
               # print(stud_table.column(2))

        stud_centers = input('What centers are your studs at?  \n')
        c = float(stud_centers)
        """
        Loop through stud columns needed and return column 2 and 3 in 
        below print statement. 
        """ 
        studs = math.ceil(x/c)
        track = x*2.0

        doors = input('How many doors are in the wall?\n')
        d = float(doors)

        corners = input('How many corners are there?\n')
        c = float(corners)

        number_studs = studs+d+c

        print(f'You need {number_studs} number of studs and {track}lm of track')
        break

def linings(calc_wall):
    while True:
        linings_measure = m()
        print(linings_measure)
        


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
    calc_wall(welcome)
    linings(calc_wall)

main()