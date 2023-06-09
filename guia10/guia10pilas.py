from queue import LifoQueue as Pila
from random import randint
import numpy as np

def randomPile(length: int):
    p = Pila()
    for i in range(length):
        p.put(randint(0,100))
    return p

#ej10
def cantidadElementos(p: Pila) -> int:
    cant = 0
    while not p.empty():
        p.get()
        cant+=0
    return cant

#ej11
def buscarElMaximo(p: Pila) -> int:
    #el maximo es -inf pues no se si puede haber numeros negativos en la pila
    maximo = np.NINF

    while not p.empty():
        curr = p.get()
        if curr > maximo:
            maximo = curr
    return maximo

#ej12
#aux
def parsearAPila(s:str):
    p = Pila()
    for char in s[::-1]:
        p.put(char)
    return p


def estaBienBalanceada(s:str) -> bool:
    p = parsearAPila(s)
    open_parentesis = False
    closed_parentesis = True
    while not p.empty():
        curr = p.get()
        if curr=="(":
            if closed_parentesis:
                open_parentesis = True
                closed_parentesis = False
            else:
                return False
        elif curr ==")":
            if open_parentesis:
                open_parentesis = False
                closed_parentesis = True
            else:
                return False
    
    return ((not open_parentesis) and closed_parentesis)

print(estaBienBalanceada("1 + 3 x (())"))

