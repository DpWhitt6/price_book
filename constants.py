import inquirer

centers = [
    inquirer.List('centers', message='What centers do you require (m)?',
                  choices=[0.3, 0.45, 0.6]),

]
insulation = [
    inquirer.List('insulation', message='Do you want insulation?',
                  choices=['Yes', 'No']),
]
linings = [
    inquirer.List('linings', message='Add a lining?',
                  choices=['Yes', 'No']),
]

lining_headers = ['Ref', 'Linings', 'Thickness', 'm2']
lining_table = [[1, 'Plasterboard - Std', '12.5mm', 2.88],
                [2, 'Plasterboard - Std', '15mm', 2.88],
                [3, 'Plasterboard - Fire', '12.5mm', 2.88],
                [4, 'Plasterboard - Fire', '15mm', 2.88],
                [5, 'Plywood', '8mm', 2.88],
                [6, 'Plywood', '12mm', 2.88],
                [7, 'Plywood', '18mm', 2.88]]

stud_headers = ['Ref', 'Material', 'Thickness']
stud_table = [[1, 'Timber', '50mm'], [2, 'Timber', '70mm'],
              [3, 'Timber', '90mm'], [4, 'Timber', '150mm'],
              [5, 'Steel', '70mm'], [6, 'Steel', '90mm'],
              [7, 'Steel', '146mm']]
