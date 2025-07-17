from enum import Enum
from roman_number import RomanNumber as rn

class OPERATION(Enum):
    ADD = "+"
    SUB = "-"
    MUL = "x"
    DIV = "/"

    def calcular(self, num1, num2):
        if self == OPERATION.ADD:
            resultado = num1 + num2
        elif self == OPERATION.SUB:
            resultado = num1 - num2
        elif self == OPERATION.MUL:
            resultado =  num1 * num2    
        elif self == OPERATION.DIV:
            resultado =  num1 / num2
        return resultado
    


from enum import Enum

class Estado(Enum):
    ACTIVO = ("activo", 1)
    INACTIVO = ("inactivo", 0)
    SUSPENDIDO = ("suspendido", -1)

    def __init__(self, etiqueta, codigo):
        self.etiqueta = etiqueta
        self.codigo = codigo