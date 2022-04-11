#Investigar la función enumerate
#El método get de los diccionarios puede servir
#La sentencia os.system("cls") sirve para limpiar pantalla
from itertools import count
import os
import random
from turtle import pu


def read(palabras):
    palabras = []
    with open("./Archivos/datos.txt","r",encoding="utf-8") as f:
        for lines in f:
            palabras.append(lines)
            list(enumerate(palabras, start=1))
    return random.choice(palabras)

def replace_at(text, pos, car):
    lista = list(text)
    pos = pos -1
    lista[pos] = car
    return "".join(lista)


def run():
    palabras = []
    palabras = read(palabras)
    palabras = palabras.strip()
    cantidadletras = len(palabras)
    ahorcado = "-"*cantidadletras
    punteo = 110
    #######
    while ahorcado != palabras:    
        os.system("cls")
        print("¡Adivina la palabra!")
        print(ahorcado)
        #print(palabras)
        letra = input("Ingrese una letra: ")
        assert letra.isalpha or letra.isspace, "Debe ingresar una letra"
        n = 0
        punteo = punteo - 10
        for i in palabras:
            n = n + 1
            if i == letra:
                #ahorcado = ahorcado[:n] + i + ahorcado[n+1:]
                ahorcado = replace_at(ahorcado, n, i)
                punteo = punteo + 10
    print("")
    if punteo > 100:
        punteo = 100
        print("Felicidades ganaste!!!")
    elif punteo > 0:
        print("Felicidades ganaste!!!")
    else:
        print("Mejor suerte a la próxima")
    print("La palabra correcta es: " + palabras)
    print("Tu punteo es: " + str(punteo))    


if __name__ == "__main__":
    os.system("cls")
    run()