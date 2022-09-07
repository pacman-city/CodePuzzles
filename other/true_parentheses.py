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
    elif s in '({[':
        current.append(s)
    elif (s == ')' and current[-1] != '(' or
          s == '}' and current[-1] != '{' or
          s == ']' and current[-1] != '['):
        print(False)
        break
    else:
        current.pop(-1)
else:
    if len(current):
        print(False)
    else:
        print(True)
