#ej18

def agruparPorLongitud(nombre_archivo:str) -> dict:
    res: dict = {}
    lista_palabras:list[str] = []
    lista_longitudes: list[int] = []
    with open(nombre_archivo) as f:
        for line in f:
            # Uso list.extend() que appendea todos los elementos de una lista al final de la otra lista
            lista_palabras.extend(line.split())

    #Creo una nueva lista que solo contiene las longitudes de las palabras
    for palabra in lista_palabras:
        lista_longitudes.append(len(palabra))
    
    #Paso esta lista al diccionario mediante el método count, que devuelve 
    #La cantidad de apariciones de un elemento en una lista.
    for long in lista_longitudes:
        res[long] = lista_longitudes.count(long)
    

    return res


#ej19
def promedioEstudiante(filename: str) -> float:
    # Esta función recibe el nombre de un archivo csv con 4 columnas, id, fecha, materia y nota.
    # La función devuelve un diccionario con el promedio de notas de cada estudiante por id.
    res: dict = {}
    with open(filename) as f:
        for line in f:
            line_formatted = line.split(",")
            lu = line_formatted[0]
            nota = float(line_formatted[3])
            if lu not in res:
                #si no agregué ninguna nota de esa lu, creo una lista con solo esa nota
                res[lu] = [nota]
            else:
                #si ya hay una entrada para esa lu, sé que es una lista, y agrego la nueva nota.
                res[lu].append(nota)
    
    #Ahora que tengo un diccionario de esta pinta {lu1:[nota1, nota2, ...], lu2:[nota1, nota2...]}
    #Puedo calcular el promedio en base a esa lista de notas para cada lu.
    for lu in res:
        res[lu] = sum(res[lu]) / len(res[lu])
    return res


#ej20

def agruparPorApariciones(filename:str) -> str:
    res: dict = {}
    lista_palabras: list[str] = []

    with open(filename) as f:
        for line in f:
            # uso extend en vez de append para que todo sea una sola lista en vez de una lista de listas
            lista_palabras.extend(line.split(" "))

    for palabra in lista_palabras:
        if palabra not in list(res.keys()):
            res[palabra] = lista_palabras.count(palabra)
    
    return res



def laPalabraMasFrecuente(filename:str) -> str:
    ap = agruparPorApariciones(filename)
    # seteo la mas frecuente a la primera, si hay una mas frecuente se reemplazará
    mas_frecuente = list(ap.keys())[0]

    for palabra in ap:
        if ap[palabra] > ap[mas_frecuente]:
            mas_frecuente = ap[palabra]
    return mas_frecuente

#print(agruparPorApariciones("ej20.txt"))
print(laPalabraMasFrecuente("ej20.txt"))
