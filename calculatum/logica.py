from calculatum.datos import OPERATION, rn
from calculatum.presentacion import input_operaciones, input_romano, continuar_o_salir

def calcular(num1, num2, operacion):
    if operacion == OPERATION.ADD:
        resultado = num1 + num2
    elif operacion == OPERATION.SUB:
        resultado = num1 - num2
    elif operacion == OPERATION.MUL:
        resultado =  num1 * num2    
    elif operacion == OPERATION.DIV:
        resultado =  num1 / num2

    return resultado

def mainloop():
    total = rn(0)
    while True:

        num1 = input_romano("Primer numero: ")
        num2 = input_romano("Segundo numero: ")
        operacion = input_operaciones("Operación (+, -, x , /): ")
        
        resultado = calcular(num1, num2, operacion)
        #resultado = operacion.calcular(num1, num2)
        
        print(f"Resultado: {resultado}")

        total = total + resultado
        
        if not continuar_o_salir ("Otro calculo (s/n)? "):
            break

        print(f"Total acumulado = {total}")
        

    print(f'El resultado total es : {total}')
    print("Hasta luego")