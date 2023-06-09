from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def todosIguales(l: List[int]) -> bool:
  if len(l) == 0:
    return False

  primero = l[0]
  for item in l[1:]:
      if item != primero:
          return False

  return True

def restaListas(l1: List[int], l2: List[int]) -> List[int]:
   #a l1 le resta l2
   res: List[int] = l1.copy()
   if len(res) != len(l2): return []

   for i in range(len(l1)):
      res[i] = res[i] - l2[i]
   return res

def igualDiferencia(l1: List[int], l2: List[int]) -> bool:
    return todosIguales(restaListas(l1,l2))


def filasParecidas(m: List[List[int]]) -> bool :
    if len(m) == 0: return False
    # Chequeo que la diferencia entre la primer y segunda fila sea igual. Si no lo es, ya no pueden ser filas parecidas
    # Luego, guardo la diferencia entre la primer y segunda fila. 
    dif1 = restaListas(m[1], m[0])
    if todosIguales(dif1):
        n = dif1[0]
    else:
       return False

    # Luego chequeo que esta diferencia se mantenga entre todas las filas
    for i in reversed(range(len(m))):
        #si i==0 ya devuelvo true porque ya chequee todas
        if (i == 0):
          return True
        #si la diferencia entre dos filas no es igual, devuelvo false
        elif not igualDiferencia(m[i], m[i-1]): 
          return False
        #si la diferencia entre dos filas es igual, pero es distinta a n, devuelvo false
        elif restaListas(m[i], m[i-1])[0] != n:
            return False

    return True


m = [[1],
     [9]]
print(filasParecidas(m))
