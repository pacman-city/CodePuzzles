"""
    Списочная очередь https://contest.yandex.ru/contest/23758/problems/J/
    Очередь, написанная с использованием связного списка.
    Поддерживает выполнение 3-х команд:
    get() — вывести элемент, находящийся в голове очереди, и удалить его. Если очередь пуста, то вывести «error».
    put(x) — добавить число x в очередь.
    size() — вывести текущий размер очереди.
"""


class Node:
    def __init__(self, value, prev):
        self.prev = prev
        self.value = value


class Queue:
    def __init__(self):
        self.current_size = 0
        self.head = None
        self.tail = None

    def put(self, value):
        self.current_size += 1

        node = Node(value, None)
        if not self.head:
            self.head = node
        elif not self.tail and self.head:
            self.tail = node
            self.head.prev = node
        else:
            self.tail.prev = node
            self.tail = node

    def get(self):
        if self.current_size == 0:
            return 'error'
        self.current_size -= 1

        value = self.head.value
        self.head = self.head.prev
        if self.tail == self.head:
            self.tail = None
        return value

    def size(self):
        return self.current_size


count = int(input())
q = Queue()
for i in range(count):
    cmd = input().split()
    if cmd[0] == 'put':
        q.put(cmd[1])
    elif cmd[0] == 'get':
        print(q.get())
    else:
        print(q.size())
