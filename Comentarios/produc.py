class producto:
    cont=0
    def __init__(self, nombre, precio):
        self.__nombre=nombre
        self.__precio=precio
        producto.cont+=1
        
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre=nombre
        
    def getPrecio(self):
        return self.__precio
    
    def setPrecio(self, precio):
        self.__precio=precio
    
    def getCalculariva(self):
        a=self.__precio*0.19
        i=self.__nombre
        return i,a
            
    
print("Datos Productos")
ob= producto("tarjeta", 123456)
ob2= producto("memoria", 30000)
print(ob.getNombre())
#ob.setNombre("memoria")
print(ob2.getNombre())
print(ob.getPrecio())
#ob.setPrecio(789012)
print(ob2.getPrecio())
print(ob.getCalculariva())
print(ob2.getCalculariva())
print(producto.cont)
print("""""")




    