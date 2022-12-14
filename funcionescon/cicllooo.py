##Calcular la operación x n - ciclos
x = 0
y = 0
def operacion(x, y):
    x=int(input("Base"))
    y= int(input("Exponete"))
    i = 1
    potent = x
    while(i < y):
        i+=1
        potent*=x
    if y <= 0:
        potent=1
    print(potent)
    return" "

print(operacion(x,y))