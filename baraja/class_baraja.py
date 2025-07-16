from random import randint


class Baraja:

  def __init__(self):
    self.numeros = ['🂡', '2', '3', '4', '5', '6', '7', '🧝', '🐴', '👑']
    self.palos = ['💰', '🍷', '⚔️', '🌵']
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
      print(f' \nJugador {jugador} : estas son tus cartas {mano} !!! Buena suerte\n ')

    # print(f' Las cartas que quedan en la baraja son : {self.cartas}')
    print("----------- Reparto completado -----------\n")
    print("-------------- Suma de puntuaciones ----------------\n")
    return barajas_jugadores

# if __name__ == '__main__':
#   print('Desde el fichero de de la clase')
    
  
  
b1 = Baraja()
b1.crear_baraja()
b1.barajear()
# b1.repartir(5 , 3)
























































