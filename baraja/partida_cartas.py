from class_baraja import Baraja 
baraja_juego = Baraja()
baraja_juego.barajear()
manos =baraja_juego.repartir(1, 4)
mazo_restante = baraja_juego.cartas
class JuegoSieteYMedia:
  def __init__(self, mano_jugadores, cartas_restantes):
    self.manos = mano_jugadores
    self.mazo = cartas_restantes
    self.puntuaciones = [0] * len(self.manos)
    self.valores_cartas ={
    '🂡': 1,
    '🧝': 0.5,
    '🐴': 0.5,
    '👑': 0.5,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7
    }

  def calcular_valor_carta(self, carta):
    self.carta = carta
    self.valor_carta = carta[0]
    valor = self.valores_cartas[carta[0]]
    print(f'Carta: {carta} ---> Valor = {valor}')
    return valor

  def calcular_puntuacion_mano(self, mano):
    valor_total =  0
    for carta in  mano:
      valor_total += self.calcular_valor_carta(carta)
    return valor_total
  
  def mostrar_puntuaciones(self):
    puntuaciones_jugadores = {}
    for jugador, mano in enumerate(self.manos, 1):
      mano_jugador = self.calcular_puntuacion_mano(mano)
      print(f' Jugador : {jugador} tu valor de cartas es  {mano_jugador} ' )

      puntuaciones_jugadores[f'Jugador {jugador}'] = mano_jugador

      while mano_jugador < 7.5:
          decision = input("¿Quieres pedir otra carta? (s/n): ")
          if decision.lower() == 's':
            nueva_carta = self.mazo.pop(0)
            mano.append(nueva_carta)
            print(f"🃏 Recibes: {nueva_carta}")
            puntuacion_actual = self.calcular_puntuacion_mano(mano)
            print(f"➡ Puntos ahora: {puntuacion_actual}")
            puntuaciones_jugadores[f'Jugador {jugador}'] =puntuacion_actual
            if puntuacion_actual > 7.5:
              print("❌ ¡Te has pasado!.... Perdiste")
              break
          else:
            print("🛑 Te plantas.")
            break
    print(puntuaciones_jugadores)
    return puntuaciones_jugadores


juego = JuegoSieteYMedia(manos, mazo_restante)
juego.mostrar_puntuaciones()






  

