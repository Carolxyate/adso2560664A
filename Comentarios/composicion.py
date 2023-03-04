class Curso:#se crea una clase llamda curso
    def __init__(self,titulo):#se inicializa con su constructor y un atributo o parametro
        self.__titulo=titulo#se crea una variable de instancia

    def getTitulo(self):#se crea un metodo
        return self.__titulo#retorna el titulo

class Aprendiz:#se crea otra clase llamada aprendiz
    def __init__(self,nombre):#se inicializa con su constructor y un atrubito o parametro en este caso nombre
        self.__nombre=nombre#se crea una variable de instancia
        self.__cursos=[]#se crea una lista vacia

    def agregarCurso(self,nombreCursito):#se crea un metodo con un parametro
        cursito=Curso(nombreCursito)#se crea una variable que instancia la clase Curso
        self.__cursos.append(cursito) #se hace uso de un metodo .append para agregar a la lista los datos 

    def getCursos(self):#se crea un metodo get para obtener los cursos
        return self.__cursos#retorna los cursos 
    
ap=Aprendiz('Sofia')#se crea un objeto con la clase aprendiz
ap.agregarCurso('Python Basico')#se intancia con el objeto
ap.agregarCurso('Python Intermedio')#se agrega otro curso

for c in ap.getCursos():#se crea un for para que recorra los valores de la lista
    print(c.getTitulo())#se imprime la lista que recorrio

del ap#elimina el objeto