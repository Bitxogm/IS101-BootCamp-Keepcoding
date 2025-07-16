def click_counter():
  counter = 0
  def increase_clicker(reset_to_0 = 0):
    nonlocal counter 
    if reset_to_0 == 'reset':
      counter = 0
      print(f'Counter reset to : {counter  }')
      print(f'*' * 40 )
      # print(f'Star count  after reset ')
    else:
      counter +=1
      print(f'Counter at : {counter} clicks')
      if counter == 5:
        print(f'🤔 Llevas 5 clicks')
    return counter
  print(f'Start count ->>>>')
  return increase_clicker

click = click_counter()
click()
click()
click()
click()
click()
click()
click()
click('reset')
click()
click()
click()
click()
click('reset')
click()
click()
click()
click()
click('reset')
click()
click()
click('reset')
click()
click()
click()
click()
click('reset')












