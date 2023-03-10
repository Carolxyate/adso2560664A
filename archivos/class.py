from Aprendiz import * #se importa de la clase aprendiz todos los datos o atributos
from Curso import * #se importa de la clase aprendiz todos los datos o atributos


with open('herencia/aprendices.txt','r') as flujo:#se abre el archivo y lo lee
    datos=flujo.read()    #se crea una variable local y la lee
    print(datos)#imprime los datos 
    #flujo.write('2560664,maria,123')
aprendices=[]#se crea una lista local
with open('herencia/aprendices.txt','r') as flujo:#se abre el archivo y lo lee
    for linea in flujo:#intera o recorre los datos guardados
        #print(linea)
        aprendices.append(linea.rsplit())#agrega a la lista que quita los \n de la lista

datosxlinea=[]#se crea una lista local
for aprendiz in aprendices:#recorre los datos de la lista aprendices 
    datosxlinea.append(aprendiz[0].split(','))#se agrega a la lista los aprendiz, y el split parte los datos donde haya la ,

#print(ob.getNombre())

print(datosxlinea)#imprime los datos linea por linea 

listaDeObjetos=[]# se crea una lista local
for apr in datosxlinea:#se crea un for para interar los datos de la lista 
     f=apr[0]#pasa la posicion inicial o la primera
     n=apr[1]#pasa la segunda posicion
     d=apr[2]#pasa la tercera posicion 
     ob=Aprendiz(f,n,d)#se crea el objteo con los parametros
     print(ob)#imprime el objeto
     listaDeObjetos.append(ob)#agrega el objeto a la lista

for xx in listaDeObjetos:#se crea un for para que recorrar la lista 
    print(xx.getNombre())#imprime el nombre
    print(xx.getDocumento())#imptime el documento
    print(xx.getFicha())#imprime la ficha 