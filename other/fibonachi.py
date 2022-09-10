def fibonachi(n):
    if n == 1 or n == 0:
        return 1
    return fibonachi(n - 1) + fibonachi(n - 2)


print(fibonachi(20))


def f():
    n = 50
    p = 1
    c = 1
    for _ in range(n - 1):
        p, c = (c, c + p)
    return c


print(f())
