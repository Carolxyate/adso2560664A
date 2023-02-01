def rango(a):
    if a>=0:
        print(a,"es numero positivo")
    else:
        print(a," es numero negativo")

def nota(num):
    if num > 11:
        print("valor erroneo")
    elif num <=2:
        print("mal")
    elif num <= 4:
        print("insuficiente")
    elif num <= 7:
        print("suficiente")
    elif num <= 9:
        print("muy bien")
    elif num == 10:
        print("excelente")

def trabajo(n):
    A = int(input("ingrese horas trabajadas:" ))
    B = float(A)
    C = B - 40
    D = (40 * 2600) + (C * 5000)
    E = B * 2600
    if B > 40:
        print("El salario es: ", D)
    elif B < 40:
        print("El salario es: ", E)

def num(n1,n2,n3):
    p1 = (n1==n2==n3)
    p2 = (n1==n2!=n3)or(n1!=n2==n3)or(n2!=n3==n1)
    p3 = (n1!=n2!=n3!=n2!=n1)
    if p1:
        print("Todos iguales")
    elif p2:
        print("Dos iguales")
    elif p3:
        print("Todos distintos")

def  segundos(a):
    minuto= (a/60)
    hora= (minuto/60)
    print ("Segundos:", a)
    if (minuto):
        print ("Minutos:",minuto)
    if (hora):
        print("Horas:",hora)