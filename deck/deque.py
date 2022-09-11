"""
    Реализовать структуру данных Дек с методами:
    push_back(value) – добавить элемент в конец | «error» если переполнен
    push_front(value) – добавить элемент в начало | «error» если переполнен
    pop_front() – вывести первый элемент дека и удалить его | «error» если дек пустой
    pop_back() – вывести последний элемент дека и удалить его | «error» если дек пустой
"""


# id 86756729

class DequeEmptyError(Exception):
    def __init__(self):
        super().__init__('error')


class DequeFullError(Exception):
    def __init__(self):
        super().__init__('error')


class Deque:
    """Класс deck aka list, дек, double-queue"""

    def __init__(self, max_size):
        self.max_size = max_size
        self.current_size = 0
        self.back = 0
        self.front = 1
        self.__list = [None] * max_size

    def check_empty(self):
        if self.current_size == 0:
            raise DequeEmptyError

    def check_full(self):
        if self.current_size == self.max_size:
            raise DequeFullError

    def pop(self, step, is_step_front=False):
        self.check_empty()

        self.current_size -= 1
        index = step % self.max_size
        value = self.__list[index]
        self.__list[index] = None
        if is_step_front:
            self.front = index
        else:
            self.back = index

        return value

    def push(self, value, is_step_front=False):
        self.check_full()

        self.current_size += 1
        if is_step_front:
            self.__list[self.front] = value
            self.front = (self.front + 1) % self.max_size
        else:
            self.__list[self.back] = value
            self.back = (self.back - 1) % self.max_size

    def push_front(self, value):
        return self.push(value, is_step_front=True)

    def push_back(self, value):
        return self.push(value)

    def pop_front(self):
        return self.pop(step=self.front - 1, is_step_front=True)

    def pop_back(self):
        return self.pop(step=self.back + 1)


def get_data():
    """return (number:количество команд, number: размер очереди)"""
    return int(input()), int(input())


def test_deque():
    """Создает экземпляр двусторонней очереди и запускает тесовые команды"""
    count, max_size = get_data()
    deque = Deque(max_size)
    for _ in range(count):
        try:
            command = input().split()
            if command[0].startswith('push'):
                getattr(deque, command[0])(command[1])
            else:
                print(getattr(deque, command[0])())
        except (DequeEmptyError, DequeFullError) as error:
            print(error)


if __name__ == '__main__':
    test_deque()
