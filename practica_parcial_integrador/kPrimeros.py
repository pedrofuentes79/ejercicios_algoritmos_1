def kPrimeros(a: list[tuple[str, int]], k:int) -> list[str]:
    res: list[str] = []
    #Como no puedo modificar la lista "a" hago una copia
    a_copy: list[tuple[str, int]] = a.copy()
