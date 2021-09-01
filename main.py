import entering
import logic

# расчет типа загрузки по результатам анализа воды
values = entering.values_input()
result = logic.parameter_calculation(values)
print(result)
