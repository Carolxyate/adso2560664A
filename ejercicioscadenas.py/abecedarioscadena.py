#- Cuantas letras del abecedario estan en la cadena, si estan repetidas cuentela solo una vez

def abecedario():
    abecedario2="abcdefghijklmnopqrstuvwxyzdkjavsfbailsdfllahidb"
    volver=[]
    tamaño=(len(abecedario2))
    for i in abecedario2:
        if i not in volver:
            volver.append(i)
    tamaño2=(len(volver))
    print("abecedario")
    print(volver)
    print("el abecedario tiene un tamaño de:",tamaño )
    print("el abecedario sin repetir tiene",tamaño2)

abecedario()