# A continuación vamos a realizar un ejercicio para aprender a utilizar todas las funciones que acabamos de explicar.
#  El ejercicio consiste en utilizar todas las funciones sobre un objeto lista que crearemos al principio. 
# El código fuente es el siguiente:

lista = [45,32,3,78]
print("Lista original: ", lista)
lista.append(995)
lista.append(7)
print("Lista después de usar append: ", lista)
lista.sort()
print("Lista ordenada: ", lista)
lista.reverse()
print("Lista al revés: ",lista)
listaextend = [1,5,87,45]
lista.extend(listaextend)
print("Lista después de extend: ",lista)
lista.sort(reverse=True)
print("Lista ordenada al revés: ", lista)
print("Número de elementos 45: ",lista.count(45))
lista.insert(4,111)
print("Lista después de insert: ",lista)
lista.remove(45)
print("Lista después de remove: ", lista)
print("Posición del elemento 111: ",lista.index(111))
lista.pop()
print("Lista después de pop: ", lista)
lista.clear()
print("Lista después de clear: ", lista)

