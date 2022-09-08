"""
Проверить является ли скобочная последовательность правильно открытой/закрытой.
Пустая строка - правильная последовательность.
Скобки могут открываться и закрываться много раз
"""

str = '{[()]}()(){}'

current = []
for s in str:
    if len(current) == 0 and s in ')}]':
        print(False)
        break
    elif s in '({[':  # добавляем все открывающие скобки в current
        current.append(s)
    elif (s == ')' and current[-1] != '(' or  # проверка - если закрывающая скобка - неправильного типа
          s == '}' and current[-1] != '{' or
          s == ']' and current[-1] != '['):
        print(False)
        break
    else:
        current.pop(-1)  # если скобка правильно закрыта - убираем из current
else:
    if len(current):  # если остались незакрытые скобки
        print(False)
    else:
        print(True)  # если пустая строка
