def parameter_exception():
    print('Показатели состава воды имеют большие отклонения от допустимых значений.'
          'Для индивидуального расчета системы очистки обратитесь к сотрудникам технического отдела.')


def parameter_calculation(value):
    if value[0] > 9 or value[0] < 6:
        parameter_exception()
        return
    elif value[3] <= 2 and value[7] < 2 and value[5] <= 8 and value[1] <= 3:
        return ('катионит PC002')
    if 2 > value[3] <= 15 and value[7] <= 5 and value[5] <= 10 and value[1] <= 3 and value[6] <= 3:
        return ('Экотар В')
    if 10 >= value[3] <= 30 and value[7] <= 5 and value[5] <= 10 and value[1] <= 3 and value[6] <= 5:
        return ('Экотар В30')
    if value[3] <= 2 and 10 >= value[7] <= 30 and value[5] <= 2 and value[1] <= 3 and value[6] <= 2:
        return ('Экотар С')
    if value[3] <= 8 and value[7] <= 10 and value[5] <= 10 and value[1] <= 3 and value[6] <= 2:
        return ('Экотар А')
    if value[0] >= 7.5 and value[3] <= 3 and value[7] <= 2 and value[5] <= 1 and value[1] <= 3 and value[6] <= 0.3:
        return ('Birm')
