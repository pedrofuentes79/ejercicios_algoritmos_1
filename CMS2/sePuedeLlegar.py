from typing import List
from typing import Tuple

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista y Tupla, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# t: Tuple[str,str]  <--Este es un ejemplo para una tupla de strings.

def hayVuelosHacia(vuelos: List[Tuple[str, str]], destino) -> bool:
  for vuelo in vuelos:
    if destino == vuelo[1]:
      return True
  return False

def vueloDesde(vuelos: List[Tuple[str, str]], origen) -> List[Tuple[str, str]]:
  #acá asumo que como sale un solo vuelo de cada ciudad, hay un solo vuelo desde x ciudad.
  res: List[Tuple[str, str]] = []
  for vuelo in vuelos:
    if vuelo[0] == origen:
      res.append(vuelo)
  return res



def sePuedeLlegar(origen: str, destino: str, vuelos: List[Tuple[str, str]]) -> int :
  #caso directo
  if (origen, destino) in vuelos: return 1
  #caso en el que ningun vuelo llega al destino esperado, es obvio que no se puede llegar
  if not hayVuelosHacia(vuelos, destino): return -1

  curr = origen
  contador_vuelos = 0


  while len(vuelos) > 0:
    if (curr, destino) in vuelos:
      return contador_vuelos + 1
    v = vueloDesde(vuelos, curr)
    if v != []:
      #saco el vuelo de la lista pues ya lo tomé y no puede haber vuelos repetidos
      vuelos.pop(vuelos.index((curr,v[0][1])))
      #actualizo la ciudad actual
      curr = v[0][1]
      contador_vuelos +=1
    else: #llegue a un "vuelo sin salida"
      return -1
    

if __name__ == '__main__':
  origen = input()
  destino = input()
  vuelos = input()
  
  print(sePuedeLlegar(origen, destino, [tuple(vuelo.split(',')) for vuelo in vuelos.split()]))