class Vehiculo: # se crea una clase padre
    def __init__(self,tipo):#se inicializa con su constructor y un atributo o parametro
        self.tipo=tipo#se crea una variable de instancia
    def descripcion(self):# se crea un metodo
        print('Soy generico no tengo descripcion',self.tipo)#imprime el texto y el tipo de vehiculo
#v=Vehiculo('Cualquier tipo')

    def getTipo(self):#se crea un getter con el tipo de vehiculo
        return self.tipo#retorna el tipo
        #return Vehiculo.tipo
    def __str__(self):# se hace un metodo para saber que clase es
        return 'Soy objeto de la clase Vehiculo'#retorna la clase que corresponde

class Herramienta:#se crea otra clase padre
    def __init__(self,proposito):#se inicializa con su constructor y con un atributo o parametro
        self.__proposito=proposito
    def getProposito(self):#
        return self.__proposito
    def __str__(self):#busca el tipo dependiendo la clase en la que este
        return 'Soy objeto de la clase Herramienta'#depende la clase en el q este se imprime esto
class Terrestre(Vehiculo,Herramienta):#se crea una subclase, con las dos clases padres
    def __init__(self,tipo,proposito):#hacemos un constructor
        Herramienta.__init__(self,proposito)#se llama la clase padre con sus atributos inicializandolos
        Vehiculo.__init__(self,tipo)#se llama la clase padre con sus atributos inicializandolos        
    def datos(self):#
        print('Tipo: ',super().getTipo())#imprime el tipo llamando la clase padre y diciendo cual metodo llamar
        print('Tipo: ',super().getProposito())#imprime el proposito llamando la clase padre y diciendo cual metodo llamar
    # def __str__(self):
    #     return 'Soy objeto de la clase Terrestre'
               
t=Terrestre("terrestre","carga")#se crea una variable 
t.datos()#llama el metodo con la clase terrestre
print(t.__str__())#imprime la clase 