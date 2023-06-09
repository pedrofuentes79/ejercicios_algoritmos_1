from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.


def mesetaMasLarga(l: List[int]) -> int :
  if len(l) == 0: return 0

  for i in reversed(range( len(l) + 1 )):
    if hayMesetaDeLong(l, i):
      return i
  return 1

def hayMesetaDeLong(l: List[int], n: int) -> bool:
  for i in range(len(l)):
    j: int = i + n
    if n == len(l):
      return todosIguales(l)
    elif j > len(l):
      return False
    elif todosIguales(l[i:j]): 
      return True

def todosIguales(l: List[int]) -> bool:
  if len(l) == 0:
    return False

  primero = l[0]
  for item in l[1:]:
      if item != primero:
          return False

  return True





if __name__ == '__main__':
  x = input()
  print(mesetaMasLarga([int(j) for j in x.split()]))