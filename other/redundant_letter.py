"""Найти добавленную букву."""

s1 = 'xtkpx'
s2 = 'xkctpx'

letters = list(set(s1 + s2))

for chr in letters:
    if s1.count(chr) != s2.count(chr):
        print(chr)
