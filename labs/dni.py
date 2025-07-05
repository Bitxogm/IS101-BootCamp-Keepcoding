
class Dni:
  """
    Clase Dni
    Representa un  numero de Dni español oficial.

    Atributos:
    -numbers (int) : Numeros del Dni.
    -letter (str) : La letra del Dni
    -letters (str): La cadena  de letars validas  oficiales 

    Metodos:
    check_numbers() : chequea que los  numeros sean 8 y solo sean numeros

    validate_letter(): comprueba que la letra  corresponda con el numero , siendoel resto de dividir elnumero entre23 , la posicion real en la cadena
    de letras validas .
  """
  letters = "TRWAGMYFPDXBNJZSQVHLCKE"  # -> Para usar como  atirbuto de clase ,

  def __init__(self, numbers : int, letter : str):
    # self.letters = "TRWAGMYFPDXBNJZSQVHLCKE"
    self.numbers = numbers
    self.letter =  letter.upper()
    self.check_numbers()
    self.validate_letter()
  
  def check_numbers(self):
    try:
      num =int(self.numbers)
      if len(str(num)) !=  8:
        raise ValueError ('El numero debe ser de 8 numeros ')
    except :  
      raise ValueError('El numero no puede  contener letras')

  def validate_letter(self):
    number = self.numbers % 23
    # if self.letter  != self.letters[number]:
    if self.letter  != Dni.letters[number]: # -> Si usamos el el atributo de  clase , aunque la opcion de arriba tambien es valida
      raise Exception ('La  letra no coincide con la esperada')
    
dni = Dni(12345678, 'Z')
print(dni.numbers)
print(dni.letter)
dni_mal =Dni(1234567, 'A')
# dni1 = Dni('1234567r' , 'yy')



    


