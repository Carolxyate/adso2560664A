import csv #se importa el modulo csv
header=['Fruit','Price']#se crea una lista con dos valores
rows=[['Apple',1200],#se crea una lista que contiene sublistas
      ['Berry',2000],#se crea una lista que contiene sublistas
      ['Lemon',1000],#se crea una lista que contiene sublistas
      ['Melon',3000],#se crea una lista que contiene sublistas
      ['Grapes',4000],#se crea una lista que contiene sublistas
      ['Pear',2000]]#se crea una lista que contiene sublistas

with open ('archivos/example.csv','w') as csvfile:#se abre el archivo para escribir y si no esta se genera automaticamente
    csvwriter=csv.writer(csvfile)#se crea el objeto con el csv para que escriba por linea
    csvwriter.writerow(header)#escribe el encabezado
    csvwriter.writerows(rows)#escribe los rows despues del encabezado