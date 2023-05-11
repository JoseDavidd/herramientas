import random
import pide_un_numero

def mostrar(lista):
    contador = 0
    for elemento in lista:
        print(f"{contador} {elemento}")
        contador += 1

def indice_valido_en(lista):
    indice = None
    invalido = False
    while indice not in range(len(lista)):
        if invalido:
            print("Elije una opción válida")
        invalido = True
        indice = pide_un_numero.pide_un_numero()

    return indice

def elegir_indice(lista):
    mostrar(lista)
    indice = indice_valido_en(lista)
    
    return indice

def elegir_valor(lista):
    indice = elegir_indice(lista)
    valor = lista[indice]
    
    return valor

def elegir_valor_aleatorio(lista):
    aleatorio = random.choice(lista)

    return(aleatorio)

if __name__ == "__main__":
    print(elegir_valor(["caca", "culo", "pedo", "pis"]))





#def eleccion_usuario(opciones):
#     usuario = int(input("Introduce 0 piedra, 1 para papel y 2 para tijera: "))
#     return usuario
# print(usuario)