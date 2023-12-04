print('Задача 2. Функция максимума')

# Юра пишет различные полезные функции для Python, чтобы остальным программистам стало проще работать. Он захотел написать функцию, которая будет находить максимум из перечисленных чисел. Функция для нахождения максимума из двух чисел у него уже есть. Юра задумался: может быть, её можно как-то использовать для нахождения максимума уже от трёх чисел?

# Помогите Юре написать программу, которая находит максимум из трёх чисел. Для этого используйте только функцию нахождения максимума из двух чисел.

# По итогу в программе должны быть реализованы две функции:
# 1) maximum_of_two — функция принимает два числа и возвращает одно (наибольшее из двух);
# 2) maximum_of_three — функция принимает три числа и возвращает одно (наибольшее из трёх); при этом она должна использовать для сравнений первую функцию maximum_of_two.



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
  return max2

def output():
  out = max_of_three()
  print('Наибольшее число из трех: ', out)

def main():
  output()

main()
  
  
  
