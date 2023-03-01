class Persona:
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getDocumento(self):
        return self.documento

    def setDocumento(self, documento):
        self.documento = documento

class Aprendiz(Persona):
    def __init__(self, nombre, documento, ficha):
        super().__init__(nombre, documento)
        self.ficha = ficha

    def getFicha(self):
        return self.ficha

    def mostrarDatos(self):
        print("Datos Aprendiz")
        print("Nombre: ", self.nombre)
        print("Documento: ", self.documento)
        print("Ficha: ", self.ficha)


print("Datos Persona")
ob = Persona("Maria", "123456")
print(ob.getNombre())
ob.setNombre("Ana")
print(ob.getNombre())
print(ob.getDocumento())
ob.setDocumento("789012")
print(ob.getDocumento())
print("""""")

app = Aprendiz("Pedro", "345678", "12345")
app.mostrarDatos()

