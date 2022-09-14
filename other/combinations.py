"""
    Дана клавиатура мобильного телефона.
    На ней 9 кнопок, и буквы на кнопках расположены в таком порядке:
    2:'abc',
    3:'def',
    4:'ghi',
    5:'jkl',
    6:'mno',
    7:'pqrs',
    8:'tuv',
    9:'wxyz'

    На вход подается строка из нажатых кнопок формата: 233
    Необходимо отобразить все возможные комбинации букв для данной строки
"""


def get_combination(n, arr, prefix):
    if n == len(arr):
        print(prefix, end=' ')
    else:
        for ltr in arr[n]:
            get_combination(n + 1, arr, prefix + ltr)


if __name__ == '__main__':
    string = input()
    d = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
    buttons_array = [[*d[int(num)]] for num in string]

    get_combination(0, buttons_array, '')
