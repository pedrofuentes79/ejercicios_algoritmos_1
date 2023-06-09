from typing import List


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




l = [1,1,1,1,1,2,2, 1, 1] #deberia devolver 5
print(mesetaMasLarga(l))

h = 7
print("hay meseta long: " + str(h))
print(hayMesetaDeLong(l,h))

