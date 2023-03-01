#intento documento
"""class Persona:
    def __init__(self,nombre,docu):#se define la funcion con el construrtor y un parametro
        self.__nombre=nombre#atributo partuckar oar saber  
        #print('Constructor Activado')        

    def getNombre(self):
        return self.__nombre

    def setNombre(self,nombre):
        self.__nombre=nombre
    def getdouc(self):
        return self.__docu
    def setdocu(self,docu):
        self.__nombre=docu

ob=Persona('Maria')
ob=Persona('13452')
ob=persona('13452')
print(ob.getNombre())
ob.setNombre('Ana')
print(ob.getNombre())
#print(type(ob))

def setNombre(self,nombre):
    ob.setNombre('Ana')
print(ob.getNombre())
#print(type(ob))

class Aprendiz(Persona):
    def __init__(self,nombre,ficha):
        Persona.__init__(self,nombre)
        self.__ficha=ficha

    def getFicha(self):
        return self.__ficha

app=Aprendiz('Pedro',12345)
print(app.getFicha())
print(app.getNombre())
print(app.getdocu())"""


class Persona:# se crea la clase persona
    def __init__(self,nombre):#se define la funcion con el construrtor y un parametro
        self.__nombre=nombre #se une con el atributo nombre 
        #print('Constructor Activado')        

    def getNombre(self): #se define la funcion con el metodo get para acceder al valor del atributo.
        return self.__nombre

    def setNombre(self,nombre):#se define la funcion con el metodo set para acceder al atributo
        self.__nombre=nombre

ob=Persona('Maria')
print(ob.getNombre())
ob.setNombre('Ana')
print(ob.getNombre())
#print(type(ob))

class Aprendiz(Persona):#se crea una subclase con la clase padre que es persona
    def __init__(self,nombre,ficha):#se define la funcion con el constructor y un parametro, el init es para inicializar los atributos del objeto que creamos.
        Persona.__init__(self,nombre)
        self.__ficha=ficha #se une con el atributo nombre

    def getFicha(self):
        return self.__ficha

app=Aprendiz('Pedro',12345)
print(app.getFicha())
print(app.getNombre())
