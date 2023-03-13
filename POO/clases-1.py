class Usuario:
    def __init__(self, nombre, direccion, telefono, correo):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__correo = correo

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

    def setCorreo(self, correo):
        self.__correo = correo

    def datos(self):
        print("Nombre: ", self.getNombre())
        print("Dirección: ", self.getDireccion())
        print("Correo: ", self.getCorreo())
        print("Teléfono: ", self.getTelefono())


class Estudiante(Usuario):
    def __init__(self, codigo_estu, nombre, direccion, telefono, correo):
        super().__init__(nombre, direccion, telefono, correo)
        self.__codigo_estu = codigo_estu

    def getCod(self):
        return self.__codigo_estu

    def mostrarDatos(self):
        print("Datos estudiante")
        print("Nombre: ", self.getNombre())
        print("Código: ", self.__codigo_estu)


class Docente(Usuario):
    def __init__(self, codigo_docen, nombre, direccion, telefono, correo):
        super().__init__(nombre, direccion, telefono, correo)
        self.__codigo_docen = codigo_docen

    def getCod(self):
        return self.__codigo_docen

    def mostrarDatos(self):
        print("Datos docente")
        print("Nombre: ", self.getNombre())
        print("Código: ", self.__codigo_docen)

while True:
    print("------ Menú ------")
    print("1. Mostrar datos de Usuario")
    print("2. Mostrar datos de Estudiante")
    print("3. Mostrar datos de Docente")
    print("4. Salir")

    opcion = int(input("Ingrese la opción que desee: "))

    if opcion == 1:
        usuario = Usuario("Juan", "Calle 123", "1234567", "juan@mail.com")
        usuario.datos()
    elif opcion == 2:
        estudiante = Estudiante("E123", "Pedro", "Calle 456", "2345678", "pedro@mail.com")
        estudiante.mostrarDatos()
    elif opcion == 3:
        docente = Docente("D456", "Maria", "Calle 789", "3456789", "maria@mail.com")
        docente.mostrarDatos()
    elif opcion == 4:
        break
    else:
        print("Opción inválida")






class pedido:
    def __init__(self, idusuario, tmaterial, cmaterial):
        self.__idusuario = idusuario
        self.__tmaterial = tmaterial
        self.__cmaterial = cmaterial

    def getidusuario(self):
        return self.__idusuario

    def gettmaterial(self):
        return self.__tmaterial

    def getcmaterial(self):
        return self.__cmaterial

    def setidusuario(self, idusuario):
        self.__idusuario = idusuario

    def settmaterial(self, tmaterial):
        self.__tmaterial = tmaterial

    def setcmaterial(self, cmaterial):
        self.__cmaterial = cmaterial


class bibliotecario(pedido):
    def __init__(self, idusuario, tmaterial, cmaterial, nombre):
        super().__init__(idusuario, tmaterial, cmaterial)
        self.__nombre = nombre

    def getnombre(self):
        return self.__nombre

    def setnombre(self, nombre):
        self.__nombre = nombre

while True:
    print("Menú:")
    print("1. Mostrar id de usuario de pedido")
    print("2. Mostrar tipo de material de pedido")
    print("3. Mostrar código de material de pedido")
    print("4. Mostrar nombre del bibliotecario")
    print("5. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        p = pedido("123", "libro", "9788478291195")
        print("El id de usuario del pedido es:", p.getidusuario())
    elif opcion == "2":
        p = pedido("123", "libro", "9788478291195")
        print("El tipo de material del pedido es:", p.gettmaterial())
    elif opcion == "3":
        p = pedido("123", "libro", "9788478291195")
        print("El código de material del pedido es:", p.getcmaterial())
    elif opcion == "4":
        b = bibliotecario("123", "libro", "9788478291195", "Juan")
        print("El nombre del bibliotecario es:", b.getnombre())
    elif opcion == "5":
        break
    else:
        print("Opción inválida. Intente de nuevo.")






class Material:
    def __init__(self, id_usuario, titulo_materia, codigo_material, revista):
        self.id_usuario = id_usuario
        self.revista = revista
        self.titulo_materia = titulo_materia
        self.codigo_material = codigo_material
        self.reservafin = []

    def get_revista(self):
        return self.revista

    def set_revista(self, revista):
        self.revista = revista

    def set_titulo_materia(self, titulo_materia):
        self.titulo_materia = titulo_materia

    def agregar(self, fechaini):
        self.reservafin.append(fechaini)

    def ver_fechas(self):
        return self.reservafin

    def ver_usuarios(self):
        return self.id_usuario

    def ver_titulos_materia(self):
        return self.titulo_materia

    def ver_codigo_material(self):
        return self.codigo_material

    def todo(self):
        print("El código del material es:", self.ver_codigo_material())
        print("El usuario es:", self.ver_usuarios())
        print("El tipo de libro es:", self.ver_titulos_materia())
        print("El tipo de revista es:", self.get_revista())


class Fechas:
    def __init__(self, fechainiyfin):
        self.fechainiyfin = fechainiyfin

    def get_fechainiyfin(self):
        return self.fechainiyfin


class Usuario:
    def __init__(self, id_usuario, nombre_usuario, direccion):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.direccion = direccion

    def ver_id_usuario(self):
        return self.id_usuario

    def ver_nombre_usuario(self):
        return self.nombre_usuario

    def ver_direccion(self):
        return self.direccion


class Libro(Material):
    def __init__(self, nombre_libro, autor, editorial, titulo_materia):
        super().__init__(None, titulo_materia, None, None)
        self.__nombre = nombre_libro
        self.__autor = autor
        self.__editorial = editorial

    def ver_nombre_libro(self):
        return self.__nombre

    def ver_editorial(self):
        return self.__editorial

    def ver_autor(self):
        return self.__autor

    def datos_test(self):
        print("El tipo de libro es:", super().ver_titulos_materia())
        print("Autor:", self.ver_autor())
        print("Nombre del libro:", self.ver_nombre_libro())
        print("Editorial:", self.ver_editorial())

    def todo(self):
        super().todo()
        print("Autor:", self.ver_autor())
        print("Nombre del libro:", self.ver_nombre_libro())
        print("Editorial:", self.ver_editorial())


class Revista(Material):
    def __init__(self, revista, tipo_revista, autor, editorial):
        super().__init__(None, None, None, revista)
        self.tipo_revista = tipo_revista
        self.autor = autor
        self.editorial = editorial

    def ver_tipo_revista(self):
        return self.tipo_revista

    def ver_autor(self):
        return self.autor

    def ver_editorial(self):
        return self.editorial

while True:
    print("\n--- MENÚ ---")
    print("1. Libro")
    print("2. Revista")
    print("3. Usuario")
    print("0. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        # Libro
        nombre_libro = input("Ingrese el nombre del libro: ")
        autor = input("Ingrese el autor: ")
        editorial = input("Ingrese la editorial: ")
        titulo_materia = input("Ingrese el título de la materia: ")

        try:
            libro = Libro(nombre_libro, autor, editorial, titulo_materia)
            libro.datos_test()
        except:
            print("Error al crear el objeto")

    elif opcion == "2":
        # Revista
        revista = input("Ingrese el nombre de la revista: ")
        tipo_revista = input("Ingrese el tipo de revista: ")
        autor = input("Ingrese el autor: ")
        editorial = input("Ingrese la editorial: ")

        try:
            revista = Revista(revista, tipo_revista, autor, editorial)
            revista.todo()
        except:
            print("Error al crear el objeto")

    elif opcion == "3":
        # Usuario
        id_usuario = input("Ingrese el ID de usuario: ")
        nombre_usuario = input("Ingrese el nombre de usuario: ")
        direccion = input("Ingrese la dirección: ")

        try:
            usuario = Usuario(id_usuario, nombre_usuario, direccion)
            print("ID de usuario:", usuario.ver_id_usuario())
            print("Nombre de usuario:", usuario.ver_nombre_usuario())
            print("Dirección:", usuario.ver_direccion())
        except:
            print("Error al crear el objeto")

    elif opcion == "0":
        # Salir
        break

    else:
        print("Opción no válida")