from queue import LifoQueue as Pila

def notacionPolacaInversa(s:str) -> float:
    pila: Pila = Pila()
    opers = ['+', '-', '*', '/']
    for c in s:
        if c not in opers:
            pila.put(float(c))
        else:
            top1 =  pila.get()
            top2 =  pila.get()
            if c == '+':
                pila.put(float(top2 + top1))
            elif c == '-':
                pila.put(float(top2 - top1))
            elif c == '*':
                pila.put(float(top2 * top1))
            elif c == '/':
                pila.put(float(top2 / top1))
        print(list(pila.queue))
    return  pila.get()
 
if __name__ == '__main__':
    s = input().split()
    print(notacionPolacaInversa(s))