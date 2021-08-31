import entering
import logic

values = entering.values_input()
logic.parameter_exception(values)
result = logic.parameter_calculation(values)
print(result)
