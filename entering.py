def values_input():
    values_name = ['рН', 'мутности', 'цветности', 'железа']
    print('Введите необходимые показатели состава воды')
    print()
    values = list()
    for name in values_name:
        value = input(f'Введите показатель {name}: ')
        values.append(digit_errors(value, name))
    return values


def digit_errors(value, name):
    while True:
        if value.isdigit():
            value = float(value)
            print(type(value))
            break
        elif float(value.replace(',', '.', 1)):
            print(type(value))
            value = float(value.replace(',', '.', 1))
            print(type(value))
            break
        else:
            value = input(f'Введите верное число {name}: ')
    return value
