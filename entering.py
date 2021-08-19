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
        if float(value):
            break


        elif value.replace(',', '.', 1).isdigit():
            value = value.replace(',', '.', 1)
            break
        else:
            value = input(f'Введите верное число {name}: ')
    return value
