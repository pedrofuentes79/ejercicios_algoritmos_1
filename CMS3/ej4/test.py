from Fila_Del_Banco import avanzarFila
from queue import Queue

tests = [
    {
        "fila_inicial": [1, 2, 3],
        "minutos": 0,
        "fila_esperada": [1, 2, 3, 4]
    },
    {
        "fila_inicial": [1, 2, 3],
        "minutos": 5,
        "fila_esperada": [4, 5, 2]
    },
    {
        "fila_inicial": [],
        "minutos": 0,
        "fila_esperada": [1]
    },
    {
        "fila_inicial": [],
        "minutos": 3,
        "fila_esperada": []
    },
    {
        "fila_inicial": [1, 2, 3],
        "minutos": 10,
        "fila_esperada": [6, 4]
    },
    {
        "fila_inicial": [1, 2, 3],
        "minutos": 11,
        "fila_esperada": []
    },
    {
        "fila_inicial": [1, 2, 3],
        "minutos": 12,
        "fila_esperada": [7]
    },
    {
        "fila_inicial": [1, 2, 3],
        "minutos": 13,
        "fila_esperada": [7, 2]
    },
    {
        "fila_inicial": [],
        "minutos": 15,
        "fila_esperada": []
    }]

fallos = []

for i, test in enumerate(tests):
    fila: Queue = Queue()
    [fila.put(p) for p in test["fila_inicial"]]
    avanzarFila(fila, test["minutos"])
    res = []
    while not fila.empty():
        res.append(fila.get())
    if res != test["fila_esperada"]:
        fallos.append(i+1)

if len(fallos):
    string = "Fallos --> "
    for fallo in fallos:
        string += "Test " + str(fallo) + ". "
    print(string)
else:
    print("Sin fallos, un capo ;)")
