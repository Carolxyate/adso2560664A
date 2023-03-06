"""class Pedido:
    def __init__(self,id_usu,titulo_mate,codigo_mate):
        self.__id_usu=id_usu
        self.titulo_mate=titulo_mate
        self.codigo_mate=codigo_mate
        self.__pedidos=[]
        
    def agregarPedido(self,nombrePedido):
        self.__cursos.append(nombrePedido)
    def verPedidos(self):
        return self.__pedidos
    def getUsu(self):
        return self.__id_usu
    def setUsu(self,id_usu):
        self.__id_usu=id_usu
    
    def getTitulo(self):
        return self.titulo_mate
    def getCodi(self):
        return self.codigo_mate"""
         

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


ob=Usuario('Oscar','1234','jjjj@mmm.com','cra 18 #4-a')
print(ob.getNombre())
ob.setNombre("Ana")
print(ob.getDireccion())

print(ob.getTelefono())

print(ob.getCorreo())
print(ob.getDireccion())
print("""""")

app= Estudiante('2345','maria',)
app.mostrarDatos()


