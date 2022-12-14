import random
def tamlista(vector):
    tam=round(random.randrange(10,25))
    for i in range(tam):
        vector.append(round(random.randrange(100)))
    a=True
    while a:
        a=False
        for i in range(len(vector)-1):
            if vector[i]>vector[i+1]:
                vector[i],vector[i+1]=vector[i+1],vector[i]
                a=True
    return vector

vector=[]
print("ordenada: ", tamlista(vector))