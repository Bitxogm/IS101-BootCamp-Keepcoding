class ClickCounter():
  #Hacer con argumentos en clase que sea el incrementador.
  def __init__(self):
    self.counter = 0

  def increase_counter(self):
    self.counter = self.counter +1
    return self.counter
    
  def decrement_counter(self):
    self.counter = self.counter -1
    return self.counter

  def reset_counter(self):
    self.counter = 0 
    print(f'Contador reseteado a : {self.counter}')
    # return self.counter
  

clicker = ClickCounter()
print(clicker.increase_counter())
print(clicker.increase_counter())
print(clicker.increase_counter())
print(clicker.increase_counter())
print(clicker.increase_counter())
print(clicker.increase_counter())
print(clicker.increase_counter())
print(clicker.increase_counter())
clicker.reset_counter()
print(clicker.decrement_counter())
print(clicker.decrement_counter())
print(clicker.decrement_counter())
print(clicker.decrement_counter())
print(clicker.decrement_counter())
print(clicker.decrement_counter())
print(clicker.decrement_counter())
clicker.reset_counter()