from typing import List
from typing import Dict
import json

def unir_diccionarios(a_unir: List[Dict[str,str]]) -> Dict[str,List[str]]:
  res: Dict[str, List[str]] = {}
  for dictionary in a_unir:
    for key in dictionary:
      # Si ya tiene una entrada, le agrego a la lista el nuevo valor
      if key in res:
        res[key].append(dictionary[key])
      # Si no tiene entrada, creo una lista con ese único valor
      else:
        res[key] = [dictionary[key]]
  return res

if __name__ == '__main__':
  x = json.loads(input()) # Ejemplo de input: [{"a":2},{"b":3,"a":1}]
  print(unir_diccionarios(x))