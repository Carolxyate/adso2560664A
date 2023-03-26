from Persona import *
import csv
listaPersonas=[]
with open('C:\\Users\\SENA\\Desktop\\ejerrrcarol\\femalee.csv') as csvDataFile:

    csvReader=csv.reader(csvDataFile)    
    for row in csvReader:
        ob=Persona(row[0],row[1],row[2],row[3],row[4])
        listaPersonas.append(ob)
        #print(row)
        # print('index:',row[0])
        # print('year',row[1])
        # print('age:',row[2])
        # print('name:',row[3])
        # print('movie:',row[4])
#print(listaPersonas)
for per in listaPersonas:
    print(per.pelicula())
    print(per.numbers())
#print(listaPersonas[10])