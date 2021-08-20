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
        digit_value = value.replace(',', '.', 1)
        digit_value = digit_value.replace('.', '', 1)
        for char in digit_value:
            if not char.isdigit():
                value = input(f'Введите числовое значение {name}: ')

        if value.isdigit():
            value = float(value)
            print(type(value))
            break
        elif float(value.replace(',', '.', 1)):
            print(type(value))
            value = float(value.replace(',', '.', 1))
            print(type(value))
            break

    return value
