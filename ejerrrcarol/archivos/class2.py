from Aprendiz import * #se importa de la clase aprendiz todos los datos o atributos
from Curso import * #se importa de la clase curso todos los datos o atributos

nombre=input('ingrese nombre del aprendiz')#se crea la variable con datos solicitados por teclado
documento=int(input('ingrese documento del aprendiz'))#se crea la variable con datos solicitados por teclado y como entero
ficha=input('ingrese ficha del aprendiz')#se crea la variable con datos solicitados por teclado

ap=Aprendiz(ficha,nombre,documento)#se crea un objeto que instancia las variables 

nombreCurso=input('ingrese nombre del curso')#se crea otra variable que ingrese el nombre del curso por teclado
horas=int(input('ingrese intensidad horaria del curso'))#se crea una variable que ingrse las horas por teclado
c1=Curso(nombreCurso,horas)#se crea un objjeto que instancia las variables
ap.agregarCurso(c1)#se agrega el objeto con el metodo para que agregue el curso

with open('herencia/aprendices.txt','a') as flujo:   #se abre el archivo con dos parametros y lo actualiza
    flujo.write(ap.getFicha()+','+ap.getNombre()+','+str(ap.getDocumento())+'\n')#escribe los datos, se concatenan con el + y los sepra con una , para verse mas ordenado
    