from calculatum.datos import OPERATION, rn

def input_romano(msg: str) -> rn:
    while True:
        cadena = input(msg)
        try:
            if cadena.isdigit():
                cadena = int(cadena)
            numero = rn(cadena)
            break
        except ValueError:
            print("Numero Romano/Entero no valido")

    return numero


def input_operaciones(msg: str) -> OPERATION:
    while True:
        cadena = input(msg)
        try:
            operacion = OPERATION(cadena)
            break
        except ValueError:
            print("Operacion incorrecta")
    
    return operacion

def continuar_o_salir(msg: str) -> bool:
    return input(msg).lower() == "s"