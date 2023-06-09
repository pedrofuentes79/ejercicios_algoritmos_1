def contarLineas(nombre_archivo:str) -> int:
    i:int = 0
    with open(nombre_archivo) as f:
        for line in f:
            i+=1
    return i

def existePalabra(palabra:str, nombre_archivo:str) -> bool:
    res: bool = False
    with open(nombre_archivo) as f:
        for line in f:
            if palabra in line:
                res = True
                break
        return res

def cantidadApariciones(palabra: str, nombre_archivo:str) -> bool:
    apariciones:int = 0
    with open(nombre_archivo) as f:
        for line in f:
            if palabra in line:
                apariciones += 1
    return apariciones

#Ej2
def clonarSinComentarios(nombre_archivo:str):
    nuevas_lineas = []
    f = open(nombre_archivo)
    lines = f.readlines()
    for line in lines:
        for char in line:
            if char=="#":
                break
            elif char==" " or char=="\t":
                pass
            else:
                nuevas_lineas.append(line)
                break
    
    with open("output.txt", "a+") as newfile:
        for line in nuevas_lineas:
            newfile.write(line)

    
def reverso(filename:str):
    f = open(filename)
    lines = f.readlines()
    with open("reverso.txt", "a+") as r:
        for line in reversed(lines): 
            r.write(line)
    
    

#ej6
'''
Ejercicio 6. Implementar una funci´on que lea un archivo en modo *binario* y devuelva la lista de ’palabras legibles’. Vamos a
definir una palabra legible como
secuencias de texto formadas por numeros, letras mayusculas/minusculas y los caracteres ’ ’(espacio) y ’_’(guion bajo)
que tienen longitud >= 5
'''
#Todo copilot este ejercicio.

def esLegible(palabra:str) -> bool:
    res:bool = True
    for char in palabra:
        if not char.isalnum() and char != " " and char != "_":
            res = False
            break
    return res

def palabrasLegibles(filename:str) -> list:
    palabras_legibles = []
    with open(filename, "rb") as f:
        for line in f:
            for palabra in line.split():
                if len(palabra) >= 5 and esLegible(palabra):
                    palabras_legibles.append(palabra)
    return palabras_legibles




#ej7
def promedioEstudiante(lu:str) -> float:
    notas: list[int] = []
    with open("ej7.csv") as f:
        for line in f:
            line_formatted = line.split(",")
            if lu == line_formatted[0]:
                notas.append(line_formatted[3])
    
    promedio: float = 0.0
    if notas:
        suma_total: int = 0
        for n in notas:
            suma_total += float(n)
        promedio: float = suma_total / len(notas)
    
    return promedio

