"""
    Генератор скобок

    Необходимо сделать генератор скобок для разных чисел n по шаблону:
    Для n = 3
    ((()))
    (()())
    (())()
    ()(())
    ()()()
"""


def gen_string(counter, s1, s2, string):
    if s1 == 0 and s2 == 0:
        print(string)
    else:
        if s1 > 0:
            gen_string(counter + 1, s1 - 1, s2, string + '(')
        if (counter > 0 and s2 > 0):
            gen_string(counter - 1, s1, s2 - 1, string + ')')


n = int(input())
gen_string(0, n, n, '')
