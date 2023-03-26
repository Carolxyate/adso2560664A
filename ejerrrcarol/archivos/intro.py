flujo=open('archivos/basico.txt','a')#es un objeto para el intercambio de datos y contiene 2 parametros, el open es un metodo
#datos=flujo.read()#una variable que contiene el objeto para leer
#print(datos)
flujo.write('\nCuando estudian con juicio')#pasa el objeto para poder escribir y le muestra la cadena de texto con un salto de linea
datos=flujo.read()#lee los datos del objeto
print(datos)#imprime los datos leidos



#Rutas:ubicacion de un archivo o documento
#relativa:comparten o tienen la misma carpeta-parte mas corta 
#adsoluta: ubicacion desde la raiz del disco-parte mas larga
#stream o flujo es un tuvo para poder hacer intercambio de datos
#puede leer, escribir y actualizar(read,write,a)
