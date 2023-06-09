from typing import List
'''
1. problema perteneceACadaUno (in s:seq<seq<Z>>, in e:Z, out res: seq<Bool>) {
    requiere: { True }
    asegura: { (∀i : Z)(0 ≤ i < |res| → (res[i] = true ↔ pertenece(s[i],e)) ) }
    }
'''
def pertenece(l: List, a):
    return a in l


def perteneceACadaUno(l: List[List[int]], e: int) -> List[bool]:
    res: List[bool] = []
    for i in range(len(l)):
        res.append(pertenece(l[i], e))
    return res
'''
2. problema esMatriz (in s:seq<seq<Z>>) : Bool {
requiere: { True }
asegura: { res = true ↔ (|s| > 0) ∧ (|s[0]| > 0) ∧ (∀i : Z)(0 ≤ i < |s| → |s[i]| = |s[0]|)) }
}
'''

def ordenados(l: List[int]) -> bool:
    for i in range(len(l) - 1):
        if l[i] >= l[i+1]:
            return False
    return True



def esMatriz(m : List[List[int]]) -> bool:
    if len(m) == 0 or len(m[0]) == 0: return False
    row_length: int = len(m[0])
    
    for i in range(len(m)):
        if len(m[i]) != row_length:
            return False
    return True

'''
3. problema filasOrdenadas (in m:seq<seq<Z>>, out res: seq<Bool>) {
requiere: { esMatriz(m)}
asegura: { (∀i : Z)(0 ≤ i < |res| → (res[i] = true ↔ ordenados(s[i]) ) ) }
}
'''

def filasOrdenadas(m: List[List[int]]) -> List[bool]:
    #asumo que lo que se ingresa es una matriz
    res: List[bool] = []
    for i in range(len(m)):
        res.append(ordenados(m[i]))
    return res


f = [[1,2,3],
     [2,3,4],
     [-2, -1, 0]]

print(esMatriz(f))



