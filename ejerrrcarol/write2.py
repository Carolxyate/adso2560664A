import csv# se importa el modulo csv
diccio=[
    {'name':'Alice','age':18},
    {'name':'Bob','age':19},
    {'name':'John','age':17}
]#se crea una lista que contiene diccionarios
header=['name','age']#se crea una lista con dos encabezaods

with open('archivos/people.csv','w') as csvfile:
    writer=csv.DictWriter(csvfile,fieldnames=header)
    writer.writeheader()
    writer.writerows(diccio)