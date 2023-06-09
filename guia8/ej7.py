def tieneUnaMinuscula(pwd:str) -> bool:
    for char in pwd:
        if "a" <= char <= "z":
            return True
    return False

def tieneUnaMayuscula(pwd: str) -> bool:
    for char in pwd: 
        if "A" <= char <= "Z":
            return True
    return False

def tieneUnDigito(pwd: str) -> bool:
    for char in pwd:
        if "0" <= char <= "9":
            return True
    return False


def password(pwd: str) -> str:
    if len(pwd) < 5:
        return "ROJA"
    elif len(pwd) > 8 and tieneUnaMinuscula(pwd) and tieneUnaMayuscula(pwd) and tieneUnDigito(pwd):
        return "VERDE"
    else: 
        return "AMARILLA"   


print(password("Ae2009"))