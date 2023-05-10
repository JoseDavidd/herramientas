import random

def elige():
    opciones = ["Alpha", "Beta", "Gamma"]
    aleatorio = random.choice(opciones)
    print (aleatorio)
    return(aleatorio)
elige()