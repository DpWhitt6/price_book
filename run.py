from colorama import just_fix_windows_console
just_fix_windows_console()

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

print(tabulate(lining_table,lining_headers,tablefmt="github"))
print(tabulate(stud_table,stud_headers,tablefmt='github'))
print(tabulate(centers_table,centers_headers,tablefmt='github'))