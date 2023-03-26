class Persona:
    def __init__(self,index,year,age,name,movie):
        self.__index=index
        self.__year=year
        self.__age=age
        self.__name=name
        self.__movie=movie
    def pelicula(self):
        return self.__index+' '+self.__name+' '+self.__movie
    def numbers(self):
        return self.__index+' '+self.__age+' '+self.__year