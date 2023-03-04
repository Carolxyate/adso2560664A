class Aprendiz:#se crea una clase llamada aprendiz
    def __init__(self,nombre):#se inicializa con el constructor y un atributo
        self.__nombre=nombre#se crea una variabole de instancia
        self.__cursos=[]# se crea una lista vacia
    def agregarCurso(self,nombreCurso):#se crea un metodo con un parametro
        self.__cursos.append(nombreCurso)#agrega los valores del objeto dentro del mismo metodo
    def verCursos(self):# se crea un metodo para ver los cursos agregados
        return self.__cursos#retorna los cursos

class Curso:#se crea otra clase llamada curso
    def __init__(self,nombreCurso):#se innicialiaza con un parametro
        self.__nombreCurso=nombreCurso#se crea una variable de instancia 

    def getNombreCurso(self):#se crea un metodo 
        return self.__nombreCurso#retorna el nombre del curso
    
ob=Aprendiz('Miguel')#se crea un objeto que lleva la clase aprendiz y le pasa el paratametro nombre
c1=Curso('Python Basico')#se crea otro objeto con un curso independiente
c2=Curso('Python Intermedio')#se crea otro objeto con un curso independiente
c3=Curso('Java Basico')#se crea otro objeto con un curso independiente

ob.agregarCurso(c1)#agrega el objeto al metodo para agregar el curso
ob.agregarCurso(c2)#agrega el objeto al metodo para agregar el curso
ob.agregarCurso(c3)#agrega el objeto al metodo para agregar el curso

for curso in ob.verCursos():#se crea un for para recorrer el metodo que conteniene la lista
    print(curso.getNombreCurso())#imprime los cursos

del ob#elimina el objeto 
#print(ob)
print('.....',c1.getNombreCurso())