from queue import Queue
from typing import List
from typing import Dict
from typing import Union
import json

# ACLARACIÓN: El tipo de "pedidos" debería ser: pedidos: Queue[Dict[str, Union[int, str, Dict[str, int]]]]
# Por no ser soportado por la versión de CMS, usamos simplemente "pedidos: Queue"
def procesamiento_pedidos(pedidos: Queue,
                          stock_productos: Dict[str, int],
                          precios_productos: Dict[str, float]) -> List[Dict[str, Union[int, str, float, Dict[str, int]]]]:
  
  res = []
  
  while not pedidos.empty():
    #Obtengo los datos para cada pedido
    pedido = pedidos.get()
    productos:Dict[str, int] = pedido["productos"]

    #Inicializo el pedido procesado
    pedido_procesado ={"id": pedido["id"],
                       "cliente": pedido["cliente"],
                       "productos": productos,
                       "precio_total": 0.0,
                       "estado": "completo"}

    for prod in productos:
      # Para cada producto, actualizo el pedido_procesado

      # inicializo los valores del producto que estoy iterando.
      stock: int = stock_productos[prod]
      cantidad_pedida: int = productos[prod]
      precio: float = precios_productos[prod]

      # si alcanzó el stock
      if stock - cantidad_pedida >= 0:
        #actualizo stock
        stock_productos[prod] = stock - cantidad_pedida

        #cambio el pedido procesado
        #cantidad vendida de ese producto. En este caso, como alcanzó el stock, es la cantidad que se pidió
        pedido_procesado["productos"][prod] = cantidad_pedida
        #sumo el precio de estos productos al total
        pedido_procesado["precio_total"] += cantidad_pedida * precio

      # si no alcanzó el stock (osea, se llevo todo lo que tenía y quería llevarse más)
      else:
        #actualizo stock
        stock_productos[prod] = 0

        #cambio el pedido procesado
        #cada producto del nuevo pedido procesado tendrá como valor la cantidad de productos de ese tipo que se llevó.
        # ej: si pidio 3 panes y había 3 panes, en el pedido procesado va a decir 3
        # ej: si pidio 3 panes y habia 2 panes, en el pedido procesado va a decir 2
        pedido_procesado["productos"][prod] = stock
        pedido_procesado["precio_total"] += stock * precio
        pedido_procesado["estado"] = "incompleto"

    res.append(pedido_procesado) 

  return res


pedidos_list_1 = [{"id": 21,
                   "cliente": "Gabriela",
                   "productos": {"Manzana": 2}}, 
                  {"id": 1,
                   "cliente": "Juan",
                   "productos": {"Manzana": 2, "Pan": 4, "Factura": 6}}]

pedidos_list_2 = []
pedidos_list_3 = [{"id": 1,
                   "cliente": "Juan",
                   "productos": {"Manzana": 2, "Pan": 4, "Factura": 6}}]

pedidos: Queue = Queue()
[pedidos.put(p) for p in pedidos_list_3]


stock_productos = {"Manzana": 0, "Leche": 5, "Pan": 90, "Factura": 1}
precio_productos = {"Manzana": 3.5, "Leche": 5.5, "Pan": 3.0, "Factura": 2.75}

print(procesamiento_pedidos(pedidos, stock_productos, precio_productos))