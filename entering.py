def values_input():
    values_name = ['рН' , 'мутности' , 'цветности' , 'железа общего' , 'железа Fe2+' , 'общей жесткости' , 'марганца' , 'ПМО']
    print('Введите необходимые показатели состава воды')
    print('Если показатель отсутствует введите ноль')
    print()
    values = list()
    for name in values_name:
      value = input(f'Введите показатель {name}: ')
      values.append(digit_errors(value, name))
    return values


def digit_errors(value, name):
  while True:
    try:
      value = value.replace(',', '.', 1)
      value = float(value)
      if value < 0:
        print(f'Значение {name} не может быть меньше ноля')
        value = input(f'Введите не отрицательное значение {name}: ')
    except ValueError:
      value = input(f'Введите правильное числовое значение {name}: ')
    except AttributeError:
      return value
  return value