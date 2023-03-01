"""class Persona:# se crea la clase persona
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