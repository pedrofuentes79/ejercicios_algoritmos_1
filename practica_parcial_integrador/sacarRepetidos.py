def sacarRepetidos(l:list) -> list:
    res: list = []
    for i in range(len(l)):
        if l[i] not in res:
            res.append(l[i])
    return res        

def apariciones(elem: int, l: list[int]) -> int:
    res: int = 0
    for i in range(len(l)):
        if l[i] == elem:
            res += 1
    return res 


def eliminarYContarRepetidos(l:list[int]) -> tuple[list[int],list[(int, int)]]:
    res0: list = sacarRepetidos(l)
    res1: list = []

    for i in range(len(res0)):
        ap: int = apariciones(res0[i], l)
        if ap > 1:
            res1.append((res0[i], ap - 1))
    
    res = (res0, res1)
    return res

print(eliminarYContarRepetidos([1]))