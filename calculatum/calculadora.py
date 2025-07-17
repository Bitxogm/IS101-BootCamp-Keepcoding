from roman_number import RomanNumber as rn
from calculatum.presentacion import input_romano, input_operaciones, continuar_o_salir
from calculatum.logica import calcular

total = rn(0)
while True:

    num1 = input_romano("Primer numero: ")
    num2 = input_romano("Segundo numero: ")
    operacion = input_operaciones("Operación (+, -, x , /): ")
    
    resultado = calcular(num1, num2, operacion)
    
    print(f"Resultado: {resultado}")

    total = total + resultado
    
    if not continuar_o_salir ("Otro calculo (s/n)? "):
       break

    print(f"Total acumulado = {total}")
    

print(f'El resultado total es : {total}')
print("Hasta luego")