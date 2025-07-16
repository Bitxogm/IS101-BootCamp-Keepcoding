from random import randint

numeros = ['A',  '2', '3', '4', '5', '6', '7', 'S', 'C', 'R']
palos = ['o', 'c', 'e', 'b']
def  baraja_nueva ():
  baraja = []

  for palo in palos:
    for numero in numeros:
      carta = numero + palo
      baraja.append(carta)
  return baraja 


baraja = baraja_nueva()
print(baraja)
print(len(baraja))

def mix(baraja,actual_pos, next_pos):
  aux_pos = baraja[actual_pos]
  baraja[actual_pos] =   baraja[next_pos]
  baraja[next_pos] = aux_pos


def barajear(baraja):
  for pos, _ in enumerate(baraja):
    new_pos = randint(0, len(baraja) -1)
    mix(baraja,pos, new_pos)
  return baraja
b1 = barajear(baraja)
print(b1)
print(len(b1))

b2 =barajear(baraja)
print(b2)
print(len(b2))

  











