
print("---------------------------------------------------")    
class Usuario:
    def __init__(self, nombre,direccion, telefono, correo):
        self.__nombre=nombre
        self.__direccion=direccion
        self.__telefono=telefono
        self.__correo=correo
    
    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def getDireccion(self):
        return self.__direccion
    def setDireccion(self, direccion):
        self.__direccion = direccion
    
    def getTelefono(self):
        return self.__telefono
    def setTelefono(self, telefono):
        self.__telefono = telefono
    
    def getCorreo(self):
        return self.__correo
    def setTelefono(self, correo):
        self.__correo = correo
    def datos(self):
        print("el nombre del lector es: ",ob.getNombre())
        print("la direccion del lector es: ", ob.getDireccion())
        print("el correo es: ",ob.getCorreo())
        print("el telefono del lector es: ",ob.getTelefono())


class Estudiante(Usuario):
    def __init__(self, codigo_estu,nombre,correo):
        super().__init__(nombre,correo)
        self.__codigo_estu = codigo_estu

    def getCod(self):
        return self.__codigo_estu

    def mostrarDatos(self):
        print("Datos estudiante")
        print("Nombre: ", self.__codigo_estu)
        print("pedidos: ", self.__nombre)
    
class Docente(Usuario):
    def __init__(self, codigo_docen,nombre):
        super().__init__(nombre)
        self.__codigo_docen = codigo_docen

    def getCod(self):
        return self.__codigo_docen

    def mostrarDatos(self):
        print("Datos estudiante")
        print("Nombre: ", self.__codigo_docen)
        print("pedidos: ", self.__nombre)


ob=Usuario('Oscar','craaa','3333333333333','jjjj@mmm.com')
print(ob.datos())
#print('el nombre del lector es: ')
#print(ob.getNombre())
#print('la direccion del lector es:' )
#print(ob.getDireccion())
#print('el telefono del lector es: ')
#print(ob.getTelefono())
#print('el correo es:')
#print(ob.getCorreo())

#print("""""")

print("---------------------------------------------------")    


class pedido:
    def __init__(self,idUsuario,timaterial,coMaterial):
        self.__idUsuario=idUsuario
        self.timaterial=timaterial
        self.coMaterial=coMaterial
    def getidUsuario(self):
        return self.__idUsuario
    def gettimaterial(self):
        return self.timaterial
    def getcoMaterial(self):
        return self.coMaterial
    def setidusuario(self,idUsuario):
        self.__idUsuario=idUsuario
    def settmaterial(self,tmaterial):
        self.timaterial=tmaterial
    def setcmaterial(self,coMaterial):
        self.coMaterial=coMaterial
ped=pedido(2224,"revenge",3465)
print("el id del usuario asignado es  :",ped.getidUsuario())
print("el titulo del material del pedido es :",ped.gettimaterial())
print("el codigo asignado del codigo del material es :",ped.getcoMaterial())

class bibliotecario(pedido):
    def __init__(self, idUsuario, timaterial, coMaterial, nombre):
        super().__init__(idUsuario, timaterial, coMaterial)
        self.__nombre = nombre

    def getnombre(self):
        return self.__nombre

    def setnombre(self, nombre):
        self.__nombre = nombre
        
po=bibliotecario(1777,"libro",2341, "camila")
print("-el nombre del bibliotecario es: ",po.getnombre())



print("---------------------------------------------------")    



class material:
    def __init__(self,titulo_material,codigo_material,ti_revista):
        
        self.ti_revista = ti_revista
        self.titulo_material = titulo_material
        self.codigo_material = codigo_material
        self.reservafin = []
    def getrevista(self):
        return self.ti_revista
    def setrevista(self,ti_revista):
        self.ti_revista = ti_revista
    def settitulomat(self,titulomaterial):
        self.titulo_material = titulomaterial
    def agregar(self,fecha):
        self.reservafin.append(fecha)#agregacion
    def verfechas(self):
        return self.reservafin
    def vertitulotip(self):
        return self.titulo_material
    def ver_codigo_material(self):
        return self.codigo_material
    def todo(self):
        print("el codigo del material es: ",obt.ver_codigo_material())
        print("el tipo de libro es: ",obt.vertitulotip())
        print("el tipo de revista es: ",obt.getrevista())

class fechas:
    def __init__(self,fecha):
        self.fecha=fecha 
    def getfecha(self):
        return self.fecha

obt=material("comedia",2314,"anime")
print(obt.todo())
c1=fechas("13 marzo hasta 27 marzo")
obt.agregar(c1)

print("---------------------------------------------------")    

for fechas in obt.verfechas():
    print("la fecha de la reserva:", fechas.getfecha())

print("---------------------------------------------------")    



class libro(material):
    def __init__(self,nombrelibro,autor,editorial,titulo_materia):
        super().settitulomat(titulo_materia)

        self.nombre=nombrelibro
        self.__autor=autor
        self.__editorial=editorial
        
    def vernombrelibro(self):
        return self.nombre
    def vereditorial(self):
        return self.__editorial
    def verautor(self):
        return self.__autor
    def datostest(self):
        print("El tipo de libro es:",super().vertitulotip())
        print("Autor: ", opp.verautor())
        print("Noombre libro:", opp.vernombrelibro())
        print("Editorial:", opp.vereditorial())
 
opp=libro("100 poesias","Jose","Esspa","Literatura")
print(opp.datostest())

print("---------------------------------------------------")     


class revista(material):
    def __init__(self,revista,tiporevista,autor,edicion):
        super().setrevista(revista)
        self.tiporevista=tiporevista
        self.__autor=autor
        self.__edicion=edicion
    def vertiporevista(self):
        return self.tiporevista
    def verautor(self):
        return self.__autor
    def vereditorial(self):
        return self.__edicion
    def todo(self):
        print("La revista es: ",super().getrevista())
        print("el autor de la revista es: ", t.verautor())
        print("la editorial de la revista es:", t.vereditorial())
        print("el tipo de revista es: ",t.vertiporevista())
        

t=revista("modelos","comercial","maria muñoz","colombia")
print(t.todo())
