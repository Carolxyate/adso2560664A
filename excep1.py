def divisores(num):
    try:        
        for i in range(num+1):
            if num%i==0:
                print(i,' es divisor')
    except ZeroDivisionError:
        print('indeterminacion')
    except TypeError:
        print(type(num),'Tipo de dato no soportado')
    except:
        print("error")


while True:
    try:
        var=int(input('ingrese numero'))
        divisores(var)
        if var==0:
            break
    except ValueError:
        print("dato no soportado")

var=int(input('ingrese numero'))
divisores(var)
print('El programa continua en esta linea')