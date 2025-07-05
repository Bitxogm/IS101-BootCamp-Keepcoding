from random import randint
class Baraja:
  
  def __init__(self):
    self.numeros = ['A',  '2', '3', '4', '5', '6', '7', 'S', 'C', 'R']
    self.palos = ['O', 'C', 'E', 'B']
    self.cartas = self.crear_baraja()

  def  crear_baraja (self, ):
    baraja = []
    for palo in self.palos:
      for numero in self.numeros:
        carta = numero + palo
        baraja.append(carta)
    return baraja 
  
  def barajear(self):
    # for pos in range(len(self.cartas)):
    for pos, _  in enumerate(self.cartas):
      new_pos = randint(0, len(self.cartas) -1)
      self.cartas[pos], self.cartas[new_pos] = self.cartas[new_pos] , self.cartas[pos]
      # print(f'Mezclando cartas {self.cartas[pos]} con {self.cartas[new_pos]}')
    return self.cartas
    

  def repartir(self, mano: int, jugadores: int):
    cartas = mano * jugadores
    if cartas > len(self.cartas) :
      raise Exception ('Ya no hay mas cartas en la baraja')
    barajas_jugadores = [] 

    for _ in range(jugadores):
      barajas_jugadores.append(self.cartas[:mano]) #Slicing de 0 a mano -1 , pàra ir metiendo en cada baraja de cada jugador el numero de cartas por mano .
      self.cartas = self.cartas[mano:] # Slicing para seleccionar resto de cartas de mano que seria 40 - el numero  de mano seleccionado hasta el final

    for jugador  , mano in enumerate(barajas_jugadores, 1):
      print(f' Jugador {jugador} : estas son tus cartas {mano} !!! Buena suerte ')

    print(f' Las cartas que quedan en la baraja son : {self.cartas}')
    return barajas_jugadores

if __name__ == '__main__':
  print('Desde el fichero de de la clase')
    
  
  


























































