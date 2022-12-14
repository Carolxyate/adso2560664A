Solicite una fecha al usuario. en formato día, mes y año. Dígale cuanto tiempo
#ha pasado desde esa fecha hasta hoy o cuanto falta para llegar a esa fecha si es posterior
dia_hoy = int(input("Ingrese el dia actual: "))
mes_hoy = int(input("Ingrese el mes actual: "))
año_hoy = int(input("Ingrese el año actual: "))

dia = int(input("Ingrese un dia: "))
mes = int(input("Ingrese un mes: "))
año = int(input("Ingrese un año: "))
#Convertir las fechas a dias
total = (año*365)+(mes*30)+dia
total_hoy = (año_hoy*365)+(mes_hoy*30)+dia_hoy
#Evaluar datos ingresados correcto
if año <= 0:
    print("El valor registrado no es valido")
elif not (mes>0 and mes<=12):
    print("El valor registrado no es valido")
elif not (dia>0 and dia<=30):
    print("El valor registrado no es valido")
elif not año_hoy<=0:
    print("El valor registrado no es valido")
elif not (mes_hoy>0 and mes_hoy<=12):
    print("El valor registrado no es valido")
elif not (dia_hoy>0 and dia_hoy<=30):
    print("El valor registrado no es valido")
else:
    if año < año_hoy:
        total_real = total_hoy-total
        print("Han pasado", total_real, "dias")
    elif año>año_hoy:
        total_real = total-total_hoy
        print("Falta", total_real, "dias")