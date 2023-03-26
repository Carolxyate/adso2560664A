from Persona import *
import csv
listaTodo=[]
with open('C:\\Users\\SENA\\Desktop\\ejerrrcarol\\todo.csv') as csvDataFile:

    csvReader=csv.reader(csvDataFile)    
    for row in csvReader:
        ob=Persona(row[0],row[1],row[2],row[3],row[4])
        listaTodo.append(ob)
        #print(row)
        # print('index:',row[0])
        # print('year',row[1])
        # print('age:',row[2])
        # print('name:',row[3])
        # print('movie:',row[4])
#print(listaTodo)
for per in listaTodo:
    print(per.pelicula())
    print(per.numbers())
#print(listaPerson[10])
while True:
    print("1-ingresar actor")
    
    ctrl=int(input("ingrese la opcion que desee: ")) #tipo strin

    match ctrl:
        case 1:
            print(listaTodo(Persona))
        case _:
            print("opcion invalida")
            break
    