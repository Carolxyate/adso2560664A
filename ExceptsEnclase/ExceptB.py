values = (12, 2) #se crea una tupla
#x,y=10,12
#print(divmod(10,3))
try:#bloque a evaluar
    q, r = divmod(*values)#divmod es una funcion que hace una division y el * separa los elementos de la tupla
    #print('valor de q=',q)
    print(f'q={q}')#imprime el cociente de la division, la f mezcla cadenas  
    print(f'r={r}')#imprime el residuo de la divission, la f mezcla las cadenas 
except (ZeroDivisionError, TypeError) as e:#except se ejecuta si es una divison por cero o ingresa una letra y se ronombra
    print(type(e), e)#imprime el tipo de error e imprime el error incorporado en python