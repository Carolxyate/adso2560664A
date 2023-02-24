def try_syntax(numerator, denominator):#se crea una funcion con dos parametros
    try:#se pone a evaluar
        print(f'In the try block: {numerator}/{denominator}')#imprime la mezcla de las varibales y cadena de texto 
        result = numerator / denominator#se crea una varibale con la operacion a realizar
        print(f'In the try block: {result}')#se imprime el resultado de la operacion
        #print('In the try block:', result)#se imprime el resultado de la operacion
        #quiero ver el resultado de la operacion en el print
    except ZeroDivisionError as zde:#se crea un except que se ejecuta sise trata de hacer una divison por cero y se renombra
        print(zde)#imprime el error incorporado en python 
    else:#si de lo contrario, es decir si no hay ningun error se va por el else
        print('The result is:', result)#imprime el resultado de la operacion
        return result #retorna el resultado
    finally:#finaliza el proceso
        print('Exiting')#imprime al finalizar 
        #return "Fallo por zero"
#print(try_syntax(12, 4))
print(try_syntax(12, 10))#llama la funcion dentro del print y le pasa los datos