from queue import Queue as Cola
from random import randint, sample
#ej14
def generarColaAlAzar(n):
    c = Cola()
    for _ in range(n):
        c.put(randint(0,100))
    return c

def cantidadElementos(c: Cola) -> int:
    cant = 0
    while not c.empty():
        c.get()
        cant+=0
    return cant

def buscarMaximo(c: Cola) -> int:
    maximo = 0
    while not c.empty():
        curr = c.get()
        if curr > maximo:
            maximo = curr
    return maximo

def armarSecuenciaBingo() -> Cola:
    randlist = sample(range(0,100), 100)
    c = Cola()
    while randlist:
        c.put(randlist[0])
        randlist.pop(0)
    return c

def jugarCartonDeBingo(carton: list[int], bolillero: Cola[int]) -> int:
    cant_bolas = 0
    while carton and not bolillero.empty():
        bola = bolillero.get()
        cant_bolas += 1
        if bola in carton:
            carton.pop(carton.index(bola))
    return cant_bolas

#Ej 17
#cada paciente tiene una prioridad en la cola. También tiene nombre y especialidad medica.
def parsearCola(l: list) -> Cola:
    c: Cola = Cola()
    for elem in l:
        c.put(elem)
    return c


def nPacientesUrgentes(c: Cola[(int, str, str)]) -> int:
    #Devuelve la cantidad de pacientes de la cola con prioridad [1,3]
    cant_pacientes: int = 0
    curr: tuple[int, str, str]

    while not c.empty():
        curr = c.get()
        prioridad_curr = curr[0]
        if 1 <= prioridad_curr <= 3:
            cant_pacientes += 1

    return cant_pacientes

lista_pacientes = []

cola_pacientes = parsearCola(lista_pacientes)

print(nPacientesUrgentes(cola_pacientes))