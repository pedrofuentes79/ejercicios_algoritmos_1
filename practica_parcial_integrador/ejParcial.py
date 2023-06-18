def devolverListaSnd(listaTuplas: list[tuple[str, str]], listaFst: list[str]) -> list[str]:
    listaSnd: list[str] = []
    for i in range(len(listaFst)):
        index: int = buscarEnPrimerosElementos(listaFst[i], listaTuplas)
        listaSnd.append(listaTuplas[index][1])
    return listaSnd

def buscarEnPrimerosElementos(char: str, l:list[tuple[str, str]]) -> int:
    index: int = 0
    for i in range(len(l)):
        if l[i][0] == char:
            index = i
            break
    return index

b = [("a", "b"), ("c", "d"), ("e", "f")]
l1 = ["a", "e", "c"]

print(devolverListaSnd(b, l1))