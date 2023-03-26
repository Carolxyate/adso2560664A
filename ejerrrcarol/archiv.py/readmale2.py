from Persona import *
import csv
listaPerson=[]
with open('C:\\Users\\SENA\\Desktop\\ejerrrcarol\\malee.csv') as csvDataFile:

    csvReader=csv.reader(csvDataFile)    
    for row in csvReader:
        ob=Persona(row[0],row[1],row[2],row[3],row[4])
        listaPerson.append(ob)
        #print(row)
        # print('index:',row[0])
        # print('year',row[1])
        # print('age:',row[2])
        # print('name:',row[3])
        # print('movie:',row[4])
print(listaPerson)
for per in listaPerson:
    print(per.pelicula())
#print(listaPerson[10])