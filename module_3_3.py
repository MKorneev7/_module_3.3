def print_params (a = 1, b = 'строка', c = True):
    print(a, b, c)
#Функция с параметрами по умолчанию:
print_params()
print_params(1, "строка", True)
print_params(b = 25)
print_params(c = [1,2,3])
#Распаковка параметров:
values_list = ['Mikhail', 210, True]
print_params(*values_list)
values_dict = {'a': 'car', 'b': False, 'c': 31}
print_params(**values_dict)
#Распаковка + отдельные параметры:
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)


