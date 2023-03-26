import csv
with open('C:\\Users\\SENA\\Desktop\\ejerrrcarol\\femalee.csv') as csvDataFile:
#with open('files/people.csv') as csvDataFile:
    csvReader=csv.reader(csvDataFile)
    #print(csvReader)
    for row in csvReader:
        #print(row)
        print('index',row[0])
        print('year',row[1])
        print('age',row[2])
        print('name:',row[3])
        print('movie:',row[4])
        
