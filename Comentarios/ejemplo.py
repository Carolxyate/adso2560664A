#La herencia es un proceso mediante el cual se puede crear una clase hija que hereda de una clase padre, compartiendo sus métodos y atributos. 
# Además de ello, una clase hija puede sobreescribir los métodos o atributos, o incluso definir unos nuevos.

# Polimorfismo: habla de la habilidad que tienen los objetos para responder a diferentes clases utilizando el mismo nombre.
#herencia multiple: una clase hereda de varias clases padre en vez de una sola

class Clase1:
    pass
class Clase2:
    pass
class Clase3:
    pass
class Clase4(Clase1, Clase3, Clase2):
    pass
print(Clase4.__mro__)

# mro: Esta función nos devuelve una tupla con el orden de búsqueda de los métodos.


#####################################################################################################################

#la función super() nos permite acceder a los métodos de la clase padre desde una de sus hijas. 

class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    def hablar(self):
        print("guaff")
        pass
    def moverse(self):
        print("4 pasos")
        pass
    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)
    def getedad(self,_edad):
        self._edad=_edad
        print(_edad)
    def getEspecie(self, especie):
        self.especie=especie
        print("su especie es:",self.especie)

class Perro(Animal):
    def __init__(self, especie, dueño, _edad):
        super().__init__(especie,_edad)
        self.dueño = dueño
    def getdueño(self,dueño):
        self.dueño = dueño
        print("dueño: ",self.dueño)
mi_perro = Perro('mamífero', 'Luis', 7)
#print(mi_perro.__str__())
mi_perro.hablar()
mi_perro.describeme()
mi_perro.getdueño("andrey")
mi_perro.getedad("5 años")
mi_perro.getEspecie('mamifero')




#############################################################################

#La sobreescritura de Métodos en Python se refiere a la posibilidad de que una subclase cuente con métodos
#con el mismo nombre que los de una clase superior pero que definen comportamientos diferentes.
class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def mostrarNombre(self):
        print("El nombre de la PERSONA es",self.nombre)
class Encargado:
    def __init__(self,codigoEncargado,departamento):
        self.codigoEncargado=codigoEncargado
        self.departamento=departamento
class EstudianteEncargado(Persona,Encargado):
    def __init__(self,nombre,edad,clave,calificacion,codigoEncargado,departamento):
        Persona.__init__(self,nombre,edad)
        Encargado.__init__(self,codigoEncargado,departamento)
        self.clave=clave
        self.calificacion=calificacion
        self.codigoEncargado=codigoEncargado
        self.departamento=departamento
    
    def mostrarNombre(self):
        print("El nombre del ESTUDIANTE-ENCARGADO es",self.nombre)
    
class Estudiante(Persona):
    def __init__(self,nombre,edad,clave,calificacion):
        Persona.__init__(self,nombre,edad)
        self.clave=clave
        self.calificacion=calificacion
estudianteEncargado1=EstudianteEncargado("Juan",22,"0232",10,"0233","cundinamarca")
estudianteEncargado1.mostrarNombre()

persona1=Persona("Juan",22)
persona1.mostrarNombre()

print("Nombre: ",estudianteEncargado1.nombre,"  Departamento : ",estudianteEncargado1.departamento)

juan=Persona("Juan",22)
print("juan edad",juan.edad)
maria=Estudiante("Maria",23,"2222",10)
print("maria la clave es: ",maria.clave)
