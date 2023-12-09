# Добавим комментарий в текст программы:
# Программа определяет наиболшее число из трех введенных пользователем.

def check_input(number):
  try:
    float(number)
  except ValueError:  
    return False
  else:
    return True
    
def input_param(text):
  while True:
    number = input(text)
    if check_input(number):
      return float(number)
    else:
      print('Ошибка ввода!')
  main()

def max_of_two(num1, num2):
  if num1 >= num2:
    max = num1
  else:
    max = num2
  return max

def max_of_three():
  text = 'Введите первое число: '
  num1 = input_param(text)
  text = 'Введите второе число: '
  num2 = input_param(text)
  text = 'Введите третье число: '
  num3 = input_param(text)
  max1 = max_of_two(num1, num2)
  max2 = max_of_two(max1, num3)
  print('Вы ввели три числа: ', num1', ', mum2', ', num3'.')   #изменение 1.
  return max2

def output():
  out = max_of_three()
  print('Наибольшее число из них: ', out)   #изменение 2.

def main():
  output()

main()
  
  
  
