from queue import Queue
from typing import List

# El tipo de fila debería ser Queue[int], pero la versión de python del CMS no lo soporta. Usaremos en su lugar simplemente "Queue"
def avanzarFila(fila: Queue, min: int):
  cantidad_personas: int = fila.qsize()
  caminando = {}
  curr: int = 0
  
  #las cajas, en el minuto 0, empiezan cerradas.
  caja1: bool = False
  caja2: bool = False
  caja3: bool = False
  
  #pongo este valor así no sirve de nada a menos que se reasigne cuando la caja3 atienda a alguien
  ultimo_atendido_caja_1: int = -99
  ultimo_atendido_caja_2: int = -99 
  ultimo_atendido_caja_3: int = -99




  while curr <= min:
    #APERTURA DE CAJAS  
    if   curr==1: 
      caja1 = True
    elif curr==2: 
      caja3 = True
    elif curr==3: 
      caja2 = True
    
    #LLEGA ALGUIEN NUEVO A LA FILA
    if curr % 4 == 0:
      cantidad_personas += 1
      fila.put(cantidad_personas)
    
    #CHEQUEO LOS QUE ESTABAN CAMINANDO 
      #si no hay nadie caminando, no hago nada
      #si hay alguien caminando, veo si ya caminaron 3 minutos
      #si ya caminaron 3 minutos, los meto en la fila y los saco de la lista de caminando
      #si no caminaron 3 minutos, aumento el tiempo que estuvieron caminando

    caminaron_3_minutos: List[int] = []
    for rechazado in caminando:
      if caminando[rechazado] == 3:
        fila.put(rechazado)
        caminaron_3_minutos.append(rechazado)

    #elimino los que ya caminaron 3 minutos de la lista de caminando
    for rechazado in caminaron_3_minutos:
      caminando.pop(rechazado)
    
    
    #LIBERO CAJAS
      #si pasaron x minutos desde que se atendio al ultimo de la caja, la caja se libera.
    if ultimo_atendido_caja_1 + 10 == curr: caja1 = True
    if ultimo_atendido_caja_2 + 4  == curr: caja2 = True
    if ultimo_atendido_caja_3 + 4  == curr: caja3 = True

    #ATIENDO AL SIGUIENTE DE LA FILA
    if not fila.empty():
        #VOY VIENDO QUE CAJAS ESTAN ABIERTAS Y ATIENDO EN ORDEN DE PRIORIDAD
        if caja1:
            fila.get()
            caja1 = False
            ultimo_atendido_caja_1 = curr

        if caja2 and not fila.empty():
            fila.get()
            caja2 = False
            ultimo_atendido_caja_2 = curr
        
        if caja3 and not fila.empty():
            rechazado: int = fila.get()
            caminando[rechazado] = 0
            caja3 = False
            ultimo_atendido_caja_3 = curr
    

    #AUMENTO MINUTO A LOS QUE ESTAN CAMINANDO
    for caminante in caminando:
        caminando[caminante] += 1
    #AUMENTO MINUTO
    curr += 1
    


if __name__ == '__main__':
  fila: Queue = Queue()
  fila_inicial: int = int(input())
  for numero in range(1, fila_inicial+1):
    fila.put(numero)
  min: int = int(input())
  avanzarFila(fila, min)
  res = []
  for i in range(0, fila.qsize()):
    res.append(fila.get())
  print(res)

