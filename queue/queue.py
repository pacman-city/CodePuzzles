"""
    Нужно написать класс Queue, который принимает параметр max_size,
    означающий максимально допустимое количество элементов в очереди.

    Входные данные:
    В первой строке записано одно число — количество команд.
    Во второй строке - максимально допустимый размер очереди.
    Далее идут команды по одной на строке. Команды могут быть следующих видов:
    push(x) — добавить число x в очередь;
    pop() — удалить число из очереди и вывести на печать;
    peek() — напечатать первое число в очереди;
    size() — вернуть размер очереди;
    При превышении допустимого размера очереди нужно вывести «error».
    При вызове операций pop() или peek() для пустой очереди нужно вывести «None».
"""


num_cmd = int(input())
size = int(input())


class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.current_size = 0
        self.head = 0
        self.tail = 0
        self.queue = [None] * max_size

    def is_empty(self):
        return self.current_size == 0

    def push(self, value):
        if self.current_size != self.max_size:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self.current_size += 1
            pass
        else:
            return 'error'

    def pop(self):
        if self.is_empty():
            return None
        index = self.head
        value = self.queue[index]
        self.queue[index] = None
        self.head = (self.head + 1) % self.max_size
        self.current_size -= 1
        return value

    def peek(self):
        if not self.is_empty():
            return self.queue[self.head]
        else:
            return None

    def size(self):
        return self.current_size


q = Queue(size)
for i in range(num_cmd):
    cmd = input().split()
    if cmd[0] == 'push':
        res = q.push(cmd[1])
        if res == 'error':
            print('error')
    elif cmd[0] == 'pop':
        print(q.pop())
    elif cmd[0] == 'peek':
        print(q.peek())
    else:
        print(q.size())
