try:#se crea otro bloque para evaluar
    #print(1/1))
    raise SyntaxError #el raise lanza un error apropisto para que se genere el except
except SyntaxError as e:#se genera un except y el as lo renombra como e.
    print(e)#imprime el error
    print('Cierra el parentesis')#imprime el mensaje al ejecutar el error
    
try:#se crea otro bloque para evaluar
    #raise ZeroDivisionError
    print(5/2)#imprime la operacion dentro del try y la resuelve
#except (ZeroDivisionError) as e:
except ZeroDivisionError as zde:#se ejecuta el except si se trata de hacer una division por cero y se renombra
    print(zde)#imprime el error incorporado en python
    print('prueba error')#imprime el mensaje al ejecutar el error 